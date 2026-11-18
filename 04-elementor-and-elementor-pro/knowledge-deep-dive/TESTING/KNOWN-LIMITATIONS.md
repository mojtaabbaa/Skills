# Verified Technical Limitations & Approved Exception Protocol

## 1. Verified Native Architecture Limitations

Through comprehensive static analysis of **Elementor Free 4.2.3** and **Elementor Pro 4.3.2**, the following technical boundaries have been confirmed:

### 1. Complex Geometric Clip-Paths
- **Limitation**: While Elementor provides native **Shape Dividers** (waves, curves, zigzags, triangles) and **Border Radius** controls, it does not provide an arbitrary CSS `clip-path: polygon(...)` generator inside standard container layout controls.
- **Native Alternatives**: Use Shape Dividers on top/bottom of containers, or insert custom SVG shapes via the Image widget.

### 2. Multi-Branch Conditional Form Logic
- **Limitation**: Elementor Pro's `form` widget supports multi-step forms and required field validation, but does not provide multi-condition dynamic branching (e.g. "If Field A == 'Corporate' AND Country == 'Canada', display Step 2B, else jump to Step 3").
- **Native Alternatives**: Split the flow across multiple focused forms or leverage the Elementor Display Conditions module on container blocks.

### 3. Dynamic Arithmetic Expressions
- **Limitation**: Dynamic Tags fetch raw or formatted scalar values (strings, dates, numbers, images), but do not execute runtime client-side arithmetic expressions (e.g. `[custom_field_price] * 1.20 - [discount]`).
- **Native Alternatives**: Compute derived business values server-side and persist them to custom postmeta before rendering, allowing Elementor to display the computed result via standard dynamic tags.

### 4. Custom Pseudo-Elements (`::before` / `::after` with Content)
- **Limitation**: Elementor provides Background Overlay (acting as `::before`) and Divider icons, but does not allow authoring arbitrary `content: '★'` pseudo-element strings on arbitrary widgets.
- **Native Alternatives**: Add an Icon widget or Text Path widget inside a child container.

---

## 2. Strict Exception Protocol

If a user explicitly requests a design or feature that falls into one of the verified technical limitations above:

1. **Step 1: Identify and Document the Exact Limitation**:
   State specifically which native control, widget, or setting is insufficient and cite the source architecture.
2. **Step 2: Investigate Native Alternative Configurations**:
   Attempt to re-architect the section using combinations of Containers, Shape Dividers, Transform controls, or Loop Builder.
3. **Step 3: User Notification & Authorization**:
   Report the limitation to the user in clear terms before introducing any non-native code. Request explicit authorization.
4. **Step 4: Strict Isolation of Authorized Exceptions**:
   If the user explicitly authorizes an exception:
   - Place the custom styling inside a single, dedicated, documented block.
   - Never inject arbitrary styles across the entire page.
   - Maintain the default of Zero Custom CSS across all other sections.
