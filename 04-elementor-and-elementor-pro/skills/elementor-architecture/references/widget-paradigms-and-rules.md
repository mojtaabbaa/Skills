# قوانین ساختار ویجت‌ها و ۳ پارادایم توسعه در المنتور (Widget Paradigms & Rules)

این سند راهنمای مهندسی کالبدشکافی ویجت‌ها، الگوهای کدنویسی و قوانین ساختاری آن‌ها در **Elementor Core** و **Elementor Pro** است.

---

## ۱. پارادایم‌های سه‌گانه ساخت ویجت

المنتور از سه کلاس والد پایه برای ویجت‌ها استفاده می‌کند:

```
Element_Base
 ├── Widget_Base (کلاسیک - نسخه‌های ۱ تا ۳)
 │    ├── Widget_Nested_Base (تودرتو - پذیرش کانتینرهای فرزند)
 │    └── Atomic_Widget_Base (اتومیک نسل ۴ - Twig + Schemas + بدون register_controls سنتی)
 └── Base_Widget (کلاس اختصاصی المنتور پرو مشتق از Widget_Base)
```

---

### ۱.۱. پارادایم اول: ویجت کلاسیک (`\Elementor\Widget_Base`)

این الگو ساختار ۹۰٪ ویجت‌های موجود تا قبل از نسخه ۴ را تشکیل می‌دهد.

#### متدهای اجباری و استاندارد:
1. `get_name(): string`: شناسه منحصر‌به‌فرد المان (حروف کوچک و خط فاصله؛ مثال: `'custom-card'`).
2. `get_title(): string`: نام نمایشی ویجت در پنل المنتور با ترجمه (`esc_html__( 'کارت سفارشی', 'textdomain' )`).
3. `get_icon(): string`: آیکون ویجت از فونت اختصاصی المنتور (`'eicon-post-title'`) یا FontAwesome (`'fa fa-star'`).
4. `get_categories(): array`: آرایه دسته‌بندی‌هایی که ویجت در آن نمایش داده می‌شود (`['basic']`، `['general']`، `['pro-elements']`، `['theme-elements-single']`، `['woocommerce-elements']`).
5. `get_keywords(): array`: کلمات کلیدی برای جستجو در سرچ‌باکس المنتور (`['card', 'box', 'post']`).
6. `get_script_depends(): array`: آرایه شناسه‌های اسکریپت‌های وابسته ثبت‌شده در وردپرس (`['swiper', 'my-script']`).
7. `get_style_depends(): array`: آرایه هندل‌های استایل‌های وابسته.
8. `register_controls(): void`: ثبت تب‌ها، سکشن‌ها و کنترل‌های UI (از نسخه ۳.۱ جایگزین متد قدیمی `_register_controls` شد).
9. `render(): void`: منطق رندر سمت سرور به زبان PHP هنگام مشاهده صفحه در فرانت‌اند.
10. `content_template(): void`: قالب Underscore.js جهت پیش‌نمایش آنی بدون بارگذاری مجدد در ادیتور زنده.

#### نمونه کد کامل ویجت کلاسیک استاندارد:
```php
namespace MyAddon\Widgets;

use Elementor\Widget_Base;
use Elementor\Controls_Manager;
use Elementor\Group_Control_Typography;
use Elementor\Group_Control_Border;

class Feature_Box_Widget extends Widget_Base {

    public function get_name(): string {
        return 'my-feature-box';
    }

    public function get_title(): string {
        return esc_html__( 'باکس ویژگی', 'my-addon' );
    }

    public function get_icon(): string {
        return 'eicon-info-box';
    }

    public function get_categories(): array {
        return [ 'general' ];
    }

    public function get_keywords(): array {
        return [ 'feature', 'box', 'service' ];
    }

    protected function register_controls(): void {
        // --- تب محتوا ---
        $this->start_controls_section(
            'section_content',
            [
                'label' => esc_html__( 'محتوای باکس', 'my-addon' ),
                'tab'   => Controls_Manager::TAB_CONTENT,
            ]
        );

        $this->add_control(
            'title',
            [
                'label'       => esc_html__( 'عنوان', 'my-addon' ),
                'type'        => Controls_Manager::TEXT,
                'default'     => esc_html__( 'عنوان پیش‌فرض', 'my-addon' ),
                'dynamic'     => [ 'active' => true ], // فعال‌سازی تگ‌های داینامیک
                'label_block' => true,
            ]
        );

        $this->add_control(
            'description',
            [
                'label'   => esc_html__( 'توضیحات', 'my-addon' ),
                'type'    => Controls_Manager::TEXTAREA,
                'rows'    => 4,
                'default' => esc_html__( 'توضیحات نمونه درباره این سرویس...', 'my-addon' ),
            ]
        );

        $this->end_controls_section();

        // --- تب استایل ---
        $this->start_controls_section(
            'section_style_title',
            [
                'label' => esc_html__( 'استایل عنوان', 'my-addon' ),
                'tab'   => Controls_Manager::TAB_STYLE,
            ]
        );

        $this->add_control(
            'title_color',
            [
                'label'     => esc_html__( 'رنگ متن', 'my-addon' ),
                'type'      => Controls_Manager::COLOR,
                'selectors' => [
                    '{{WRAPPER}} .my-box-title' => 'color: {{VALUE}};',
                ],
            ]
        );

        $this->add_group_control(
            Group_Control_Typography::get_type(),
            [
                'name'     => 'title_typography',
                'selector' => '{{WRAPPER}} .my-box-title',
            ]
        );

        $this->add_responsive_control(
            'title_alignment',
            [
                'label'     => esc_html__( 'تراز', 'my-addon' ),
                'type'      => Controls_Manager::CHOOSE,
                'options'   => [
                    'left'   => [ 'title' => 'چپ', 'icon' => 'eicon-text-align-left' ],
                    'center' => [ 'title' => 'وسط', 'icon' => 'eicon-text-align-center' ],
                    'right'  => [ 'title' => 'راست', 'icon' => 'eicon-text-align-right' ],
                ],
                'selectors' => [
                    '{{WRAPPER}} .my-box-title' => 'text-align: {{VALUE}};',
                ],
            ]
        );

        $this->end_controls_section();
    }

    protected function render(): void {
        $settings = $this->get_settings_for_display();
        ?>
        <div class="my-feature-box">
            <h3 class="my-box-title"><?php echo esc_html( $settings['title'] ); ?></h3>
            <p class="my-box-desc"><?php echo wp_kses_post( $settings['description'] ); ?></p>
        </div>
        <?php
    }

    protected function content_template(): void {
        ?>
        <div class="my-feature-box">
            <h3 class="my-box-title">{{{ settings.title }}}</h3>
            <p class="my-box-desc">{{{ settings.description }}}</p>
        </div>
        <?php
    }
}
```

---

### ۱.۲. پارادایم دوم: ویجت‌های تودرتو (`\Elementor\Modules\NestedElements\Base\Widget_Nested_Base`)

این الگو امکان ساخت ویجت‌هایی نظیر **Nested Tabs**، **Nested Accordion** و **Mega Menu** را فراهم می‌کند که در آنها کاربر می‌تواند کانتینرهای فلکس‌باکس کامل را به عنوان فرزند درون آیتم‌ها بکشد و رها کند.

#### الزامات معماری ویجت تودرتو:
1. ارث‌بری از `Widget_Nested_Base`.
2. پیاده‌سازی متد `get_default_children_elements()`:
   ```php
   protected function get_default_children_elements(): array {
       return [
           [
               'elType'   => 'container',
               'settings' => [
                   '_title' => __( 'تب شماره ۱', 'elementor' ),
               ],
           ],
           [
               'elType'   => 'container',
               'settings' => [
                   '_title' => __( 'تب شماره ۲', 'elementor' ),
               ],
           ],
       ];
   }
   ```
3. پیاده‌سازی متد `get_default_repeater_title_setting_key()` برای نگاشت نام آیتم ریپیتر به کانتینر فرزند.
4. در رندرینگ، فرزندان با متد `$this->print_child( $child_index )` داخل تگ والد چاپ می‌شوند.

---

### ۱.۳. پارادایم سوم: المان‌های اتمیک نسل ۴ (`\Elementor\Modules\AtomicWidgets\Elements\Base\Atomic_Widget_Base`)

انقلاب نسخه ۴ المنتور برای افزایش سرعت لود و استانداردسازی کامل:

#### اصول معماری اتمیک:
1. **عدم استفاده از `register_controls()`**: کنترل‌ها به روش زنجیره‌ای (Fluent API) در متد `define_atomic_controls()` ثبت می‌شوند.
2. **پروپ‌های تایپ‌شده قوی (`define_props_schema()`):**
   - به جای آرایه‌های متنی بدون تایپ، تک‌تک پروپ‌ها اسکیما دارند:
     - `String_Prop_Type`: رشته متنی
     - `Color_Prop_Type`: متغیر رنگ و کد رنگ
     - `Dimensions_Prop_Type`: ابعاد ۴ جهته
     - `Link_Prop_Type`: لینک با وضعیت new-tab و nofollow
     - `Classes_Prop_Type`: کلاس‌های CSS اختصاصی
3. **موتور رندر Twig (`.html.twig`)**: تفکیک مطلق لایه View از کنترلر با استفاده از موتور تمپلیت Twig.
4. **استایل‌های پایه و توکن‌های CSS (`define_base_styles()`):** تعریف مقادیر پیش‌فرض استایل به عنوان توکن‌های CSS بدون هاردکد کردن در HTML.
5. **خروجی بومی هوش مصنوعی (`render_markdown()`):** تولید مارک‌داون اختصاصی برای تغذیه تمیز به مدل‌های زبانی هوش مصنوعی.

---

## ۲. سیستم کنترل‌ها (Controls Manager Reference)

المنتور بیش از ۴۲ کنترل تک‌منظوره و ۸ کنترل گروهی دارد:

### ۲.۱. کنترل‌های تک‌منظوره پرکاربرد
| ثابت کنترل در `Controls_Manager` | تایپ | خروجی دیتا | نمونه کاربرد |
| :--- | :--- | :--- | :--- |
| `TEXT` | `text` | رشته تک‌خطی | عناوین، تگ‌ها، نام‌ها |
| `TEXTAREA` | `textarea` | رشته چندخطی | توضیحات، متن‌های متوسط |
| `WYSIWYG` | `wysiwyg` | کد HTML از TinyMCE | محتوای کامل بلاگ |
| `NUMBER` | `number` | عدد صحیح/اعشاری | ضخامت، سرعت انیمیشن، تعداد |
| `SELECT` | `select` | کلید انتخاب‌شده | انتخاب تگ H1-H6، نوع نمایش |
| `SELECT2` | `select2` | کلید یا آرایه چندتایی | انتخاب دسته‌بندی‌ها و تگ‌های وردپرس |
| `SWITCHER` | `switcher` | `'yes'` یا `''` | سوئیچ‌های فعال/غیرفعال |
| `COLOR` | `color` | کد هگز یا `var(--e-global-color-...)` | انتخاب رنگ المان |
| `CHOOSE` | `choose` | مقدار کلید با آیکون | تراز متن (راست/وسط/چپ/توجیه) |
| `SLIDER` | `slider` | آرایه `{unit, size}` | اسلایدر تغییر سایز با واحدهای px, %, rem |
| `DIMENSIONS` | `dimensions` | آرایه ۴ جهته | مارجین، پدینگ و شعاع کادر |
| `MEDIA` | `media` | آرایه `{id, url}` | انتخاب تصویر از مدیا لایبرری |
| `ICONS` | `icons` | آرایه آیکون SVG یا FontAwesome | انتخاب آیکون با قابلیت آپلود SVG |
| `URL` | `url` | آرایه `{url, is_external, nofollow}` | لینک با تنظیمات پنجره بازشو |
| `REPEATER` | `repeater` | آرایه از آرایه‌ها | آیتم‌های اسلایدر، تب‌ها، تعرفه‌ها |

### ۲.۲. کنترل‌های گروهی (`Group_Control`)
کنترل‌های ترکیبی استانداردی که با یک خط صدا زده می‌شوند:
1. **`Group_Control_Typography`**: فونت، سایز، وزن، استایل، ترنسفورم، لاین‌هایت و لترسپیسینگ.
2. **`Group_Control_Background`**: رنگ، گرادیان، تصویر، موقعیت، سایز و پس‌زمینه ویدیویی.
3. **`Group_Control_Border`**: نوع خط کادر (Solid, Dashed, Dotted, etc.)، ضخامت و رنگ.
4. **`Group_Control_Box_Shadow`**: سایه جعبه شامل آفست‌های X, Y، بلور، اسپرد و رنگ.
5. **`Group_Control_Text_Shadow`**: سایه متن برای افزایش خوانایی روی پس‌زمینه‌های شلوغ.
6. **`Group_Control_Image_Size`**: لیست اندازه‌های ثبت‌شده تصویر در وردپرس (thumbnail, medium, large, full).
7. **`Group_Control_Css_Filter`**: تنظیم بلور، روشنایی، کنتراست و اشباع رنگ.

---

## ۳. قوانین شرط‌گذاری و پاسخ‌دهی (Conditional Logic & Selectors)

### ۳.۱. قوانین شرطی (`condition` و `conditions`)
برای مخفی/ظاهر کردن هوشمند کنترل‌ها در پنل ادیتور:
```php
// شرط ساده (تک متغیر)
'condition' => [
    'show_icon' => 'yes',
],

// شرط پیشرفته چندگانه (ترکیب AND)
'conditions' => [
    'relation' => 'and',
    'terms'    => [
        [
            'name'     => 'layout_type',
            'operator' => '===',
            'value'    => 'grid',
        ],
        [
            'name'     => 'columns',
            'operator' => '!==',
            'value'    => '1',
        ],
    ],
],
```

### ۳.۲. قانون رپر و تزریق استایل (`{{WRAPPER}}`)
- هنگام نوشتن قوانین در آرایه `'selectors'`، حتماً از توکن `{{WRAPPER}}` استفاده شود.
- المنتور زمان تولید CSS، توکن `{{WRAPPER}}` را با کلاس یونیک المان (مانند `.elementor-element-7a2b4c1`) جایگزین می‌کند تا از نشت استایل‌ها به سایر بخش‌های سایت جلوگیری شود.
- متغیر `{{VALUE}}`: مقدار مستقیم فیلد را تزریق می‌کند (مثال: `'color: {{VALUE}};'`).
- متغیر `{{SIZE}}{{UNIT}}`: در کنترل‌های سایز و اسلایدر مقدار را با واحد درج می‌کند (مثال: `'width: {{SIZE}}{{UNIT}};'`).
