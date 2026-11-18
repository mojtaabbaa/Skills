# هوک‌ها و APIهای توسعه‌دهندگان در المنتور (Elementor Developer Hooks & APIs)

این سند مرجع تمامی هوک‌های اکشن، فیلتر و APIهای فرانت‌اند جاوااسکریپت برای برنامه‌نویسان وردپرس و توسعه‌دهندگان افزونه‌های المنتور است.

---

## ۱. اکشن‌های ثبت و راه‌اندازی (Registration Action Hooks)

### ۱.۱. ثبت ویجت‌های جدید (`elementor/widgets/register`)
جایگزین استاندارد هوک منسوخ‌شده `widgets_registered` از نسخه ۳.۵ به بعد:
```php
add_action( 'elementor/widgets/register', function( \Elementor\Widgets_Manager $widgets_manager ) {
    require_once __DIR__ . '/widgets/my-widget.php';
    $widgets_manager->register( new \MyAddon\Widgets\My_Widget() );
} );
```

### ۱.۲. ثبت کنترل‌های سفارشی (`elementor/controls/register`)
برای اضافه کردن نوع جدیدی از کنترل به پنل ادیتور المنتور:
```php
add_action( 'elementor/controls/register', function( \Elementor\Controls_Manager $controls_manager ) {
    require_once __DIR__ . '/controls/my-control.php';
    $controls_manager->register( new \MyAddon\Controls\My_Control() );
} );
```

### ۱.۳. ثبت دسته‌بندی جدید در پنل ویجت‌ها (`elementor/elements/categories_registered`)
```php
add_action( 'elementor/elements/categories_registered', function( \Elementor\Elements_Manager $elements_manager ) {
    $elements_manager->add_category(
        'my-custom-category',
        [
            'title' => esc_html__( 'المان‌های سفارشی من', 'textdomain' ),
            'icon'  => 'fa fa-plug',
        ]
    );
} );
```

### ۱.۴. ثبت تگ داینامیک جدید (`elementor/dynamic_tags/register`)
```php
add_action( 'elementor/dynamic_tags/register', function( \Elementor\Core\DynamicTags\Manager $dynamic_tags_manager ) {
    require_once __DIR__ . '/tags/my-dynamic-tag.php';
    $dynamic_tags_manager->register( new \MyAddon\DynamicTags\My_Tag() );
} );
```

### ۱.۵. ثبت لوکیشن‌های جدید قالب پوسته (`elementor/theme/register_locations`)
برای تعریف موقعیت‌های جدیدی مثل هدر تبلیغاتی، مگامنو یا نوار کناری برای استفاده در Theme Builder:
```php
add_action( 'elementor/theme/register_locations', function( \ElementorPro\Modules\ThemeBuilder\Classes\Locations_Manager $location_manager ) {
    $location_manager->register_location(
        'custom_header_banner',
        [
            'label'           => esc_html__( 'بنر بالای هدر', 'textdomain' ),
            'multiple'        => false,
            'edit_in_content' => false,
        ]
    );
} );
```

---

## ۲. هوک‌های تزریق و دستکاری کنترل‌های ویجت‌های موجود (Control Injection)

### ۲.۱. افزودن کنترل به سکشن موجود در یک ویجت خاص
الگوی نام‌گذاری: `elementor/element/{element_name}/{section_id}/before_section_end`
```php
// افزودن کنترل جدید به انتهای سکشن محتوای ویجت تیتر (Heading)
add_action( 'elementor/element/heading/section_title/before_section_end', function( \Elementor\Widget_Base $element, $args ) {
    $element->add_control(
        'custom_badge',
        [
            'label'       => esc_html__( 'برچسب ویژه', 'textdomain' ),
            'type'        => \Elementor\Controls_Manager::TEXT,
            'placeholder' => esc_html__( 'جدید / تخفیف', 'textdomain' ),
        ]
    );
}, 10, 2 );
```

### ۲.۲. افزودن سکشن کامل جدید به یک ویجت خاص
الگوی نام‌گذاری: `elementor/element/{element_name}/{section_id}/after_section_end`
```php
add_action( 'elementor/element/button/section_style/after_section_end', function( \Elementor\Widget_Base $element, $args ) {
    $element->start_controls_section(
        'section_custom_effects',
        [
            'label' => esc_html__( 'جلوه‌های اختصاصی دکمه', 'textdomain' ),
            'tab'   => \Elementor\Controls_Manager::TAB_STYLE,
        ]
    );

    $element->add_control(
        'glow_effect',
        [
            'label'        => esc_html__( 'افکت درخشش نئونی', 'textdomain' ),
            'type'         => \Elementor\Controls_Manager::SWITCHER,
            'return_value' => 'yes',
            'selectors'    => [
                '{{WRAPPER}} .elementor-button' => 'box-shadow: 0 0 15px #00ffcc;',
            ],
        ]
    );

    $element->end_controls_section();
}, 10, 2 );
```

### ۲.۳. افزودن کنترل به تمام ویجت‌ها یا کانتینرها (Global Controls)
```php
// افزودن کنترل به تب پیشرفته تمام المان‌ها
add_action( 'elementor/element/common/_section_style/before_section_end', function( \Elementor\Widget_Base $element, $args ) {
    $element->add_control(
        'custom_tracking_id',
        [
            'label' => esc_html__( 'شناسه گوگل آنالیتیکس', 'textdomain' ),
            'type'  => \Elementor\Controls_Manager::TEXT,
        ]
    );
}, 10, 2 );
```

---

## ۳. فیلترهای خروجی HTML و کوئری‌ها (Rendering Filters)

### ۳.۱. فیلتر محتوای رندر شده ویجت (`elementor/widget/render_content`)
دستکاری خروجی خام HTML قبل از چاپ در صفحه:
```php
add_filter( 'elementor/widget/render_content', function( $content, \Elementor\Widget_Base $widget ) {
    if ( 'heading' === $widget->get_name() ) {
        $settings = $widget->get_settings_for_display();
        if ( ! empty( $settings['custom_badge'] ) ) {
            $badge = '<span class="custom-badge">' . esc_html( $settings['custom_badge'] ) . '</span>';
            $content = $badge . $content;
        }
    }
    return $content;
}, 10, 2 );
```

### ۳.۲. فیلتر کوئری پست‌ها و لوپ‌ها (`elementor/query/{query_id}`)
شخصی‌سازی خروجی کوئری ویجت‌های Posts یا Loop Grid بر اساس شناسه `Query ID`:
```php
add_action( 'elementor/query/my_custom_query_id', function( \WP_Query $query ) {
    // محدود کردن مقالات به نویسنده جاری لاگین کرده
    if ( is_user_logged_in() ) {
        $query->set( 'author', get_current_user_id() );
    }
    // حذف مقالاتی با دسته خاص
    $query->set( 'category__not_in', [ 42 ] );
} );
```

---

## ۴. هوک‌های فرانت‌اند جاوااسکریپت (`elementorFrontend.hooks`)

برای فعال‌سازی و راه‌اندازی کتابخانه‌های کلاینت روی ویجت‌های داینامیک المنتور:

```javascript
jQuery(window).on('elementor/frontend/init', function() {
    // ۱. اجرای کد هنگام رندر شدن یک ویجت خاص
    elementorFrontend.hooks.addAction('frontend/element_ready/my-widget.default', function($scope, $) {
        // $scope رپر jQuery المان است
        const $slider = $scope.find('.my-custom-slider');
        if ($slider.length) {
            new Swiper($slider[0], {
                slidesPerView: 1,
                loop: true,
                autoplay: true
            });
        }
    });

    // ۲. اجرای کد هنگام رندر پوسته خاصی از ویجت
    elementorFrontend.hooks.addAction('frontend/element_ready/posts.cards', function($scope, $) {
        console.log('پوسته Cards ویجت Posts رندر شد.');
    });

    // ۳. اجرای کد روی تمامی المان‌ها (گلوبال)
    elementorFrontend.hooks.addAction('frontend/element_ready/global', function($scope, $) {
        // مثلا راه‌اندازی لایت‌باکس یا تول‌تیپ‌ها
    });
});
```

---

## ۵. توسعه اکشن‌های ایجکس اختصاصی (`elementor/ajax/register_actions`)

برای ارسال درخواست‌های سریع با ساختار ایمن المنتور بدون نوشتن هندلرهای سنتی `admin-ajax.php`:
```php
add_action( 'elementor/ajax/register_actions', function( \Elementor\Core\Common\Modules\Ajax\Module $ajax_manager ) {
    $ajax_manager->register_ajax_action( 'my_custom_action', function( $data ) {
        if ( ! current_user_can( 'edit_posts' ) ) {
            throw new \Exception( 'دسترسی غیرمجاز' );
        }

        // پردازش دیتا
        $post_id = intval( $data['post_id'] );
        $result = update_post_meta( $post_id, '_custom_field', sanitize_text_field( $data['value'] ) );

        return [
            'success' => (bool) $result,
            'message' => 'اطلاعات با موفقیت ذخیره شد.',
        ];
    } );
} );
```
