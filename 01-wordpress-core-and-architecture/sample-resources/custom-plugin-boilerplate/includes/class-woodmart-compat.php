<?php
namespace CustomCommerceBoilerplate;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Woodmart_Compatibility {

    public function __construct() {
        add_action( 'wp_enqueue_scripts', [ $this, 'enqueue_woodmart_compat_assets' ], 20 );
        add_filter( 'woodmart_product_element_classes', [ $this, 'add_custom_card_classes' ] );
    }

    public function enqueue_woodmart_compat_assets() {
        // Only enqueue if WoodMart is active
        if ( ! function_exists( 'woodmart_get_opt' ) ) {
            return;
        }

        wp_add_inline_script(
            'ccb-frontend-script',
            "jQuery(document).on('pjax:complete wdShopPageInit woodmart_ajax_success', function() {
                if (window.ccbFrontend && typeof window.ccbFrontend.reinit === 'function') {
                    window.ccbFrontend.reinit();
                }
            });",
            'after'
        );
    }

    public function add_custom_card_classes( $classes ) {
        $classes[] = 'ccb-enhanced-card';
        return $classes;
    }
}

new Woodmart_Compatibility();
