<?php
namespace CustomCommerceBoilerplate;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

final class Plugin {

    private static $instance = null;

    public static function instance() {
        if ( is_null( self::$instance ) ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->load_dependencies();
        $this->init_hooks();
    }

    private function load_dependencies() {
        require_once CCB_PATH . 'includes/class-ajax-handler.php';
        require_once CCB_PATH . 'includes/class-elementor-widgets.php';
        require_once CCB_PATH . 'includes/class-woodmart-compat.php';

        if ( is_admin() ) {
            require_once CCB_PATH . 'admin/class-admin-settings.php';
        }
    }

    private function init_hooks() {
        add_action( 'wp_enqueue_scripts', [ $this, 'enqueue_frontend_assets' ] );
        add_action( 'init', [ $this, 'load_textdomain' ] );
    }

    public function load_textdomain() {
        load_plugin_textdomain( 'custom-commerce-boilerplate', false, dirname( plugin_basename( CCB_FILE ) ) . '/languages' );
    }

    public function enqueue_frontend_assets() {
        wp_enqueue_style(
            'ccb-frontend-style',
            CCB_URL . 'assets/css/frontend.css',
            [],
            CCB_VERSION
        );

        wp_enqueue_script(
            'ccb-frontend-script',
            CCB_URL . 'assets/js/frontend.js',
            [ 'jquery' ],
            CCB_VERSION,
            true
        );

        wp_localize_script(
            'ccb-frontend-script',
            'ccbConfig',
            [
                'ajaxUrl' => admin_url( 'admin-ajax.php' ),
                'nonce'   => wp_create_nonce( 'ccb_ajax_nonce' ),
                'isRtl'   => is_rtl(),
            ]
        );
    }
}
