<?php
/**
 * Plugin Name: Custom Commerce & Elementor Integration Boilerplate
 * Plugin URI:  https://example.com/
 * Description: High-performance, production-ready WordPress plugin boilerplate supporting WooCommerce HPOS, Elementor Pro widgets, and WoodMart theme PJAX lifecycle.
 * Version:     1.0.0
 * Author:      Antigravity Engineering
 * Author URI:  https://example.com/
 * Text Domain: custom-commerce-boilerplate
 * Domain Path: /languages
 * Requires at least: 6.0
 * Requires PHP:      8.0
 */

namespace CustomCommerceBoilerplate;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Define Plugin Constants
define( 'CCB_VERSION', '1.0.0' );
define( 'CCB_FILE', __FILE__ );
define( 'CCB_PATH', plugin_dir_path( __FILE__ ) );
define( 'CCB_URL', plugin_dir_url( __FILE__ ) );

// Declare WooCommerce HPOS (High-Performance Order Storage) Compatibility
add_action( 'before_woocommerce_init', function() {
    if ( class_exists( \Automattic\WooCommerce\Utilities\FeaturesUtil::class ) ) {
        \Automattic\WooCommerce\Utilities\FeaturesUtil::declare_compatibility(
            'custom_order_tables',
            CCB_FILE,
            true
        );
    }
} );

// Autoloader or manual require
require_once CCB_PATH . 'includes/class-plugin.php';

// Bootstrap the plugin
function ccb_init() {
    return Plugin::instance();
}

add_action( 'plugins_loaded', 'CustomCommerceBoilerplate\\ccb_init' );
