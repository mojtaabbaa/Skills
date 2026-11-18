"""Universal Persian RTL Markdown-to-DOCX Converter for SEO Projects.

Supports:
- Standard `IRANSansWeb` font (ascii, hAnsi, cs) + `<w:rtl/>` + `<w:bidi/>` + `fa-IR`
- Native RTL Word tables (`<w:bidiVisual/>`) with repeated shaded header row
- Fresh numbering contexts per list block (never continues prior numbered lists across sections)
- State-machine inline formatting (`**bold**` wrapping `[links](url)` without literal `**` leakage)
- Real clickable `<w:hyperlink>` objects with blue underline
- Optional `--strip-zwnj` (mandatory for zero-ZWNJ brands)
- Automatic parsing of Top Metadata (`### مشخصات سئو` OR 3-line top header `Title:` / `Meta Description:`),
  plus Bottom Metadata (`**متا تایتل:**` / `**متا دسکریپشن:**`) for bottom metadata style `.md` files.
- Optional `--meta-bottom` flag to render extracted metadata at the bottom of the DOCX instead of top.
"""

import argparse
import os
import re
import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

sys.stdout.reconfigure(encoding='utf-8')

FONT_NAME = 'IRANSansWeb'


def set_run_rtl(run, font_name=FONT_NAME, bold=False, italic=False, color_rgb=None, underline=False, size_pt=None):
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)

    if bold:
        run.bold = True
        if rPr.find(qn('w:bCs')) is None:
            rPr.append(OxmlElement('w:bCs'))
    if italic:
        run.italic = True
        if rPr.find(qn('w:iCs')) is None:
            rPr.append(OxmlElement('w:iCs'))
    if underline:
        run.underline = True
    if color_rgb is not None:
        run.font.color.rgb = color_rgb
    if size_pt is not None:
        run.font.size = Pt(size_pt)

    if rPr.find(qn('w:rtl')) is None:
        rPr.append(OxmlElement('w:rtl'))
    lang = rPr.find(qn('w:lang'))
    if lang is None:
        lang = OxmlElement('w:lang')
        rPr.append(lang)
    lang.set(qn('w:bidi'), 'fa-IR')


def set_para_rtl(p, align=WD_ALIGN_PARAGRAPH.RIGHT):
    p.alignment = align
    pPr = p._p.get_or_add_pPr()
    if pPr.find(qn('w:bidi')) is None:
        pPr.append(OxmlElement('w:bidi'))


def add_hyperlink(paragraph, url, text, bold=False, font_name=FONT_NAME):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    hyperlink.set(qn('w:history'), '1')

    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')

    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)
    rPr.append(rFonts)

    c = OxmlElement('w:color')
    c.set(qn('w:val'), '0563C1')
    rPr.append(c)

    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rPr.append(u)

    if bold:
        rPr.append(OxmlElement('w:b'))
        rPr.append(OxmlElement('w:bCs'))

    rPr.append(OxmlElement('w:rtl'))
    lang = OxmlElement('w:lang')
    lang.set(qn('w:bidi'), 'fa-IR')
    rPr.append(lang)

    new_run.append(rPr)
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def add_formatted_text(paragraph, text, default_bold=False, size_pt=None, color_rgb=None):
    token_re = re.compile(r'(\*\*|\[([^\]]+)\]\((https?://[^\s\)]+)\)|(https?://[^\s\)]+))')
    pos = 0
    bold_active = default_bold
    for m in token_re.finditer(text):
        if m.start() > pos:
            seg = text[pos:m.start()]
            if seg:
                r = paragraph.add_run(seg)
                set_run_rtl(r, bold=bold_active, size_pt=size_pt, color_rgb=color_rgb)
        tok = m.group(0)
        if tok == '**':
            bold_active = not bold_active
        elif m.group(2) is not None and m.group(3) is not None:
            raw_label = m.group(2)
            label = raw_label.replace('**', '')
            url = m.group(3)
            add_hyperlink(paragraph, url, label, bold=(bold_active or ('**' in raw_label)))
        elif m.group(4) is not None:
            url = m.group(4)
            add_hyperlink(paragraph, url, url, bold=bold_active)
        pos = m.end()
    if pos < len(text):
        tail = text[pos:]
        if tail:
            r = paragraph.add_run(tail)
            set_run_rtl(r, bold=bold_active, size_pt=size_pt, color_rgb=color_rgb)


def create_list_num_id(doc, fmt='decimal'):
    try:
        numbering_elm = doc.part.numbering_part.numbering_definitions._numbering
    except Exception:
        p = doc.add_paragraph(style='List Bullet')
        p._element.getparent().remove(p._element)
        numbering_elm = doc.part.numbering_part.numbering_definitions._numbering

    abs_ids = [
        int(el.get(qn('w:abstractNumId')))
        for el in numbering_elm.findall(qn('w:abstractNum'))
        if el.get(qn('w:abstractNumId')).isdigit()
    ]
    num_ids = [
        int(el.get(qn('w:numId')))
        for el in numbering_elm.findall(qn('w:num'))
        if el.get(qn('w:numId')).isdigit()
    ]
    next_abs = max(abs_ids + [0]) + 1
    next_num = max(num_ids + [0]) + 1

    if fmt == 'decimal':
        abs_xml = f'''
        <w:abstractNum {nsdecls("w")} w:abstractNumId="{next_abs}">
          <w:multiLevelType w:val="singleLevel"/>
          <w:lvl w:ilvl="0">
            <w:start w:val="1"/>
            <w:numFmt w:val="decimal"/>
            <w:lvlText w:val="%1."/>
            <w:lvlJc w:val="right"/>
            <w:pPr><w:ind w:left="0" w:right="540" w:hanging="360"/></w:pPr>
            <w:rPr><w:rFonts w:ascii="{FONT_NAME}" w:hAnsi="{FONT_NAME}" w:cs="{FONT_NAME}"/></w:rPr>
          </w:lvl>
        </w:abstractNum>'''
    else:
        abs_xml = f'''
        <w:abstractNum {nsdecls("w")} w:abstractNumId="{next_abs}">
          <w:multiLevelType w:val="singleLevel"/>
          <w:lvl w:ilvl="0">
            <w:start w:val="1"/>
            <w:numFmt w:val="bullet"/>
            <w:lvlText w:val="•"/>
            <w:lvlJc w:val="right"/>
            <w:pPr><w:ind w:left="0" w:right="540" w:hanging="360"/></w:pPr>
            <w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:cs="{FONT_NAME}"/></w:rPr>
          </w:lvl>
        </w:abstractNum>'''

    num_xml = f'''
    <w:num {nsdecls("w")} w:numId="{next_num}">
      <w:abstractNumId w:val="{next_abs}"/>
    </w:num>'''

    abs_el = parse_xml(abs_xml)
    num_el = parse_xml(num_xml)
    first_num = numbering_elm.find(qn('w:num'))
    if first_num is not None:
        idx = list(numbering_elm).index(first_num)
        numbering_elm.insert(idx, abs_el)
    else:
        numbering_elm.append(abs_el)
    numbering_elm.append(num_el)
    return next_num


def attach_num_id(p, num_id):
    pPr = p._p.get_or_add_pPr()
    numPr = pPr.find(qn('w:numPr'))
    if numPr is None:
        numPr = OxmlElement('w:numPr')
        pPr.append(numPr)
    ilvl = OxmlElement('w:ilvl')
    ilvl.set(qn('w:val'), '0')
    nid = OxmlElement('w:numId')
    nid.set(qn('w:val'), str(num_id))
    numPr.append(ilvl)
    numPr.append(nid)


def extract_metadata(lines):
    """Extract SEO Title, Alt Title, Meta Description, and Focus Keyword from top or bottom."""
    meta = {'seo_title': '', 'alt_title': '', 'meta_desc': '', 'focus_kw': ''}
    body_lines = list(lines)

    # Case 1: Top block `### مشخصات سئو` ending with `---`
    if lines and 'مشخصات سئو' in lines[0]:
        body_start_idx = 0
        for idx, ln in enumerate(lines[1:], start=1):
            s = ln.strip()
            if s.startswith('* **عنوان اصلی سئو') or s.startswith('**عنوان اصلی سئو'):
                meta['seo_title'] = s.split(':', 1)[1].replace('**', '').strip()
            elif s.startswith('* **عنوان جایگزین') or s.startswith('**عنوان جایگزین'):
                meta['alt_title'] = s.split(':', 1)[1].replace('**', '').strip()
            elif s.startswith('* **متا دیسکریپشن') or s.startswith('* **متا دسکریپشن') or s.startswith('**متا دیسکریپشن'):
                meta['meta_desc'] = s.split(':', 1)[1].replace('**', '').strip()
            elif s == '---':
                body_start_idx = idx + 1
                break
        if body_start_idx > 0:
            body_lines = lines[body_start_idx:]
            return meta, body_lines

    # Case 2: 3-line top header (`Title:` / `Meta Description:` / `Focus Keyword:`)
    if len(lines) >= 2 and re.match(r'^(?:\*\*)?Title(?:\*\*)?:', lines[0].strip(), re.I):
        idx = 0
        while idx < len(lines) and idx < 6:
            s = lines[idx].strip()
            if not s or s == '---':
                idx += 1
                break
            if re.match(r'^(?:\*\*)?Title(?:\*\*)?:', s, re.I):
                meta['seo_title'] = s.split(':', 1)[1].replace('**', '').strip()
            elif re.match(r'^(?:\*\*)?Meta Description(?:\*\*)?:', s, re.I):
                meta['meta_desc'] = s.split(':', 1)[1].replace('**', '').strip()
            elif re.match(r'^(?:\*\*)?Focus Keyword(?:\*\*)?:', s, re.I):
                meta['focus_kw'] = s.split(':', 1)[1].replace('**', '').strip()
            else:
                break
            idx += 1
        body_lines = lines[idx:]
        return meta, body_lines

    # Case 3: Bottom `**متا تایتل:**` / `**متا دسکریپشن:**` (bottom metadata style — inline OR next-line value)
    tail_idx = None
    i = len(lines) - 1
    while i >= max(0, len(lines) - 20):
        s = lines[i].strip()
        if '**متا تایتل:**' in s or '**عنوان سئو:**' in s:
            val = s.split(':', 1)[1].replace('**', '').strip()
            if not val and i + 1 < len(lines):
                val = lines[i + 1].strip()
            meta['seo_title'] = val
            tail_idx = i if tail_idx is None else min(tail_idx, i)
        elif '**متا دسکریپشن:**' in s or '**متا دیسکریپشن:**' in s:
            val = s.split(':', 1)[1].replace('**', '').strip()
            if not val and i + 1 < len(lines):
                val = lines[i + 1].strip()
            meta['meta_desc'] = val
            tail_idx = i if tail_idx is None else min(tail_idx, i)
        i -= 1
    if tail_idx is not None:
        cut = tail_idx
        while cut > 0 and lines[cut - 1].strip() in ('', '---'):
            cut -= 1
        body_lines = lines[:cut]
    return meta, body_lines


def render_meta_block(doc, meta):
    written = False
    if meta['seo_title']:
        pm = doc.add_paragraph()
        set_para_rtl(pm, WD_ALIGN_PARAGRAPH.RIGHT)
        add_formatted_text(pm, f'**عنوان سئو:** {meta["seo_title"]}')
        written = True
    if meta['alt_title']:
        pm = doc.add_paragraph()
        set_para_rtl(pm, WD_ALIGN_PARAGRAPH.RIGHT)
        add_formatted_text(pm, f'**عنوان جایگزین:** {meta["alt_title"]}')
        written = True
    if meta['meta_desc']:
        pm = doc.add_paragraph()
        set_para_rtl(pm, WD_ALIGN_PARAGRAPH.RIGHT)
        add_formatted_text(pm, f'**متا دیسکریپشن:** {meta["meta_desc"]}')
        written = True
    if meta['focus_kw']:
        pm = doc.add_paragraph()
        set_para_rtl(pm, WD_ALIGN_PARAGRAPH.RIGHT)
        add_formatted_text(pm, f'**کلیدواژه کانونی:** {meta["focus_kw"]}')
        written = True
    if written:
        sp = doc.add_paragraph()
        set_para_rtl(sp, WD_ALIGN_PARAGRAPH.RIGHT)


def build_docx_from_md(md_path, docx_path, strip_zwnj=False, meta_bottom=False):
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    if strip_zwnj:
        raw_text = raw_text.replace('\u200c', '')

    lines = raw_text.splitlines()
    meta, body_lines = extract_metadata(lines)

    doc = docx.Document()
    for section in doc.sections:
        section.top_margin = Inches(0.85)
        section.bottom_margin = Inches(0.85)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)
        sectPr = section._sectPr
        if sectPr.find(qn('w:bidi')) is None:
            sectPr.append(OxmlElement('w:bidi'))

    for st_name in ['Normal', 'Heading 1', 'Heading 2', 'Heading 3']:
        if st_name in doc.styles:
            st = doc.styles[st_name]
            st.font.name = FONT_NAME
            pPr = st.element.get_or_add_pPr()
            if pPr.find(qn('w:bidi')) is None:
                pPr.append(OxmlElement('w:bidi'))
            rPr = st.element.get_or_add_rPr()
            rf = rPr.find(qn('w:rFonts'))
            if rf is None:
                rf = OxmlElement('w:rFonts')
                rPr.insert(0, rf)
            for attr in list(rf.attrib.keys()):
                if 'Theme' in attr or 'theme' in attr:
                    del rf.attrib[attr]
            rf.set(qn('w:ascii'), FONT_NAME)
            rf.set(qn('w:hAnsi'), FONT_NAME)
            rf.set(qn('w:cs'), FONT_NAME)
            if rPr.find(qn('w:rtl')) is None:
                rPr.append(OxmlElement('w:rtl'))
            lang = rPr.find(qn('w:lang'))
            if lang is None:
                lang = OxmlElement('w:lang')
                rPr.append(lang)
            lang.set(qn('w:bidi'), 'fa-IR')

    h1_written = False
    in_table = False
    table_rows = []
    active_list_type = None
    active_num_id = None

    def flush_table():
        nonlocal in_table, table_rows
        if not (in_table and table_rows):
            return
        cols = max(len(r) for r in table_rows)
        tbl = doc.add_table(rows=len(table_rows), cols=cols)
        tbl.style = 'Table Grid'
        tblPr = tbl._tbl.tblPr
        if tblPr.find(qn('w:bidiVisual')) is None:
            tblPr.append(OxmlElement('w:bidiVisual'))
        tblW = tblPr.find(qn('w:tblW'))
        if tblW is None:
            tblW = OxmlElement('w:tblW')
            tblPr.append(tblW)
        tblW.set(qn('w:w'), '5000')
        tblW.set(qn('w:type'), 'pct')
        cellMar = parse_xml(
            f'<w:tblCellMar {nsdecls("w")}>'
            '<w:top w:w="90" w:type="dxa"/><w:left w:w="130" w:type="dxa"/>'
            '<w:bottom w:w="90" w:type="dxa"/><w:right w:w="130" w:type="dxa"/>'
            '</w:tblCellMar>'
        )
        old_cm = tblPr.find(qn('w:tblCellMar'))
        if old_cm is not None:
            tblPr.remove(old_cm)
        tblPr.append(cellMar)
        for r_idx, r_data in enumerate(table_rows):
            tr = tbl.rows[r_idx]._tr
            if r_idx == 0:
                trPr = tr.get_or_add_trPr()
                trPr.append(OxmlElement('w:tblHeader'))
            for c_idx, cell_text in enumerate(r_data):
                cell = tbl.cell(r_idx, c_idx)
                p = cell.paragraphs[0]
                p.text = ''
                set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
                add_formatted_text(p, cell_text, default_bold=(r_idx == 0))
                if r_idx == 0:
                    tcPr = cell._tc.get_or_add_tcPr()
                    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EDF4F8"/>')
                    tcPr.append(shd)
        doc.add_paragraph()
        table_rows = []
        in_table = False

    for line in body_lines:
        raw = line.strip()
        if not raw:
            if in_table:
                flush_table()
            active_list_type = None
            continue

        if raw.startswith('|') and raw.endswith('|'):
            active_list_type = None
            inner = raw.strip('|').strip()
            if all(ch in '-:| ' for ch in inner):
                continue
            cells = [c.strip() for c in raw.split('|')[1:-1]]
            table_rows.append(cells)
            in_table = True
            continue
        elif in_table:
            flush_table()

        if raw == '---':
            active_list_type = None
            continue

        if raw.startswith('# '):
            active_list_type = None
            p = doc.add_heading('', level=1)
            set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
            add_formatted_text(p, raw[2:].strip(), default_bold=True)
            if not h1_written:
                h1_written = True
                if not meta_bottom:
                    render_meta_block(doc, meta)
            continue

        if raw.startswith('## '):
            active_list_type = None
            p = doc.add_heading('', level=2)
            set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
            add_formatted_text(p, raw[3:].strip(), default_bold=True)
            continue

        if raw.startswith('### '):
            active_list_type = None
            p = doc.add_heading('', level=3)
            set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
            add_formatted_text(p, raw[4:].strip(), default_bold=True)
            continue

        if raw.startswith('> '):
            active_list_type = None
            p = doc.add_paragraph()
            set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
            add_formatted_text(p, raw[2:].strip(), color_rgb=RGBColor(0x2B, 0x4C, 0x7E))
            continue

        m_ord = re.match(r'^([0-9]+|[۰-۹]+)\.\s+(.*)$', raw)
        if m_ord:
            if active_list_type != 'decimal':
                active_list_type = 'decimal'
                active_num_id = create_list_num_id(doc, fmt='decimal')
            p = doc.add_paragraph()
            set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
            attach_num_id(p, active_num_id)
            add_formatted_text(p, m_ord.group(2).strip())
            continue

        if raw.startswith('* ') or raw.startswith('- '):
            if active_list_type != 'bullet':
                active_list_type = 'bullet'
                active_num_id = create_list_num_id(doc, fmt='bullet')
            p = doc.add_paragraph()
            set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
            attach_num_id(p, active_num_id)
            add_formatted_text(p, raw[2:].strip())
            continue

        active_list_type = None
        p = doc.add_paragraph()
        set_para_rtl(p, WD_ALIGN_PARAGRAPH.RIGHT)
        add_formatted_text(p, raw)

    flush_table()
    if meta_bottom:
        render_meta_block(doc, meta)

    doc.save(docx_path)
    print(f'Saved clean RTL DOCX: {docx_path}')


def main():
    parser = argparse.ArgumentParser(description='Convert Persian SEO Markdown files to clean RTL DOCX.')
    parser.add_argument('files', nargs='+', help='Markdown file path(s)')
    parser.add_argument('--strip-zwnj', action='store_true', help='Remove all U+200C ZWNJ characters (for zero-ZWNJ brands)')
    parser.add_argument('--meta-bottom', action='store_true', help='Place SEO metadata at bottom of DOCX instead of under H1')
    args = parser.parse_args()

    for md_p in args.files:
        out_p = os.path.splitext(md_p)[0] + '.docx'
        build_docx_from_md(md_p, out_p, strip_zwnj=args.strip_zwnj, meta_bottom=args.meta_bottom)


if __name__ == '__main__':
    main()
