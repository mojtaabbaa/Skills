# Atomic Control Types: API Specifications & Data Structures

## 1. Text Control (`Controls_Manager::TEXT`)
- **Base Class**: `\Elementor\Control_Text` extends `Base_Data_Control`
- **PHP Registration**:
  ```php
  $this->add_control(
      'title',
      [
          'label' => esc_html__( 'Title', 'elementor' ),
          'type' => Controls_Manager::TEXT,
          'default' => esc_html__( 'Default Title', 'elementor' ),
          'placeholder' => esc_html__( 'Enter your title', 'elementor' ),
          'dynamic' => [ 'active' => true ],
          'label_block' => true,
      ]
  );
  ```
- **Stored Data Schema**: `"title": "String value"`

---

## 2. Slider Control (`Controls_Manager::SLIDER`)
- **Base Class**: `\Elementor\Control_Slider` extends `Base_Data_Control`
- **Supported Units**: `px`, `%`, `em`, `rem`, `vw`, `vh`, `custom`
- **PHP Registration**:
  ```php
  $this->add_responsive_control(
      'width',
      [
          'label' => esc_html__( 'Width', 'elementor' ),
          'type' => Controls_Manager::SLIDER,
          'size_units' => [ 'px', '%', 'vw' ],
          'range' => [
              'px' => [ 'min' => 0, 'max' => 1200, 'step' => 1 ],
              '%' => [ 'min' => 0, 'max' => 100 ],
          ],
          'default' => [
              'unit' => '%',
              'size' => 100,
          ],
          'selectors' => [
              '{{WRAPPER}} .target-element' => 'width: {{SIZE}}{{UNIT}};',
          ],
      ]
  );
  ```
- **Stored Data Schema**:
  ```json
  "width": { "unit": "%", "size": 80 },
  "width_tablet": { "unit": "%", "size": 90 },
  "width_mobile": { "unit": "%", "size": 100 }
  ```

---

## 3. Dimensions Control (`Controls_Manager::DIMENSIONS`)
- **Base Class**: `\Elementor\Control_Dimensions` extends `Base_Data_Control`
- **PHP Registration**:
  ```php
  $this->add_responsive_control(
      'padding',
      [
          'label' => esc_html__( 'Padding', 'elementor' ),
          'type' => Controls_Manager::DIMENSIONS,
          'size_units' => [ 'px', '%', 'em', 'rem' ],
          'selectors' => [
              '{{WRAPPER}}' => 'padding: {{TOP}}{{UNIT}} {{RIGHT}}{{UNIT}} {{BOTTOM}}{{UNIT}} {{LEFT}}{{UNIT}};',
          ],
      ]
  );
  ```
- **Stored Data Schema**:
  ```json
  "padding": {
    "unit": "px",
    "top": "48",
    "right": "32",
    "bottom": "48",
    "left": "32",
    "isLinked": false
  }
  ```

---

## 4. Choose Control (`Controls_Manager::CHOOSE`)
- **Base Class**: `\Elementor\Control_Choose` extends `Base_Data_Control`
- **PHP Registration**:
  ```php
  $this->add_responsive_control(
      'align',
      [
          'label' => esc_html__( 'Alignment', 'elementor' ),
          'type' => Controls_Manager::CHOOSE,
          'options' => [
              'left' => [ 'title' => esc_html__( 'Left', 'elementor' ), 'icon' => 'eicon-text-align-left' ],
              'center' => [ 'title' => esc_html__( 'Center', 'elementor' ), 'icon' => 'eicon-text-align-center' ],
              'right' => [ 'title' => esc_html__( 'Right', 'elementor' ), 'icon' => 'eicon-text-align-right' ],
          ],
          'default' => 'left',
          'selectors' => [
              '{{WRAPPER}}' => 'text-align: {{VALUE}};',
          ],
      ]
  );
  ```
- **Stored Data Schema**:
  ```json
  "align": "left",
  "align_tablet": "center",
  "align_mobile": "center"
  ```

---

## 5. Color Control (`Controls_Manager::COLOR`)
- **Base Class**: `\Elementor\Control_Color` extends `Base_Data_Control`
- **Features**: Alpha channel support, global color token binding.
- **PHP Registration**:
  ```php
  $this->add_control(
      'title_color',
      [
          'label' => esc_html__( 'Text Color', 'elementor' ),
          'type' => Controls_Manager::COLOR,
          'global' => [ 'active' => true ],
          'selectors' => [
              '{{WRAPPER}} .title' => 'color: {{VALUE}};',
          ],
      ]
  );
  ```
- **Stored Data Schema (Direct Value)**:
  `"title_color": "#2563eb"`
- **Stored Data Schema (Global Token)**:
  ```json
  "title_color": "",
  "__globals__": {
    "title_color": "globals/colors?id=primary"
  }
  ```

---

## 6. Repeater Control (`Controls_Manager::REPEATER`)
- **Base Class**: `\Elementor\Control_Repeater` extends `Base_Data_Control`
- **PHP Registration**:
  ```php
  $repeater = new \Elementor\Repeater();
  $repeater->add_control( 'tab_title', [ 'type' => Controls_Manager::TEXT ] );
  $repeater->add_control( 'tab_content', [ 'type' => Controls_Manager::WYSIWYG ] );

  $this->add_control(
      'tabs',
      [
          'label' => esc_html__( 'Tabs Items', 'elementor' ),
          'type' => Controls_Manager::REPEATER,
          'fields' => $repeater->get_controls(),
          'title_field' => '{{{ tab_title }}}',
      ]
  );
  ```
- **Stored Data Schema**:
  ```json
  "tabs": [
    {
      "_id": "item_101",
      "tab_title": "First Tab",
      "tab_content": "Content of tab 1"
    }
  ]
  ```
