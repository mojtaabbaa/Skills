<?php
namespace CustomCommerceBoilerplate;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Elementor_Widgets_Manager {

    public function __construct() {
        add_action( 'elementor/widgets/register', [ $this, 'register_widgets' ] );
    }

    public function register_widgets( $widgets_manager ) {
        if ( ! did_action( 'elementor/loaded' ) ) {
            return;
        }

        require_once CCB_PATH . 'templates/../elementor-widget-boilerplate/class-custom-product-card-widget.php';
        
        if ( class_exists( '\CustomCommerceBoilerplate\Widgets\Custom_Product_Card_Widget' ) ) {
            $widgets_manager->register( new \CustomCommerceBoilerplate\Widgets\Custom_Product_Card_Widget() );
        }
    }
}

new Elementor_Widgets_Manager();
