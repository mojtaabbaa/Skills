<?php
namespace CustomCommerceBoilerplate\DynamicTags;

use Elementor\Core\DynamicTags\Tag;
use Elementor\Modules\DynamicTags\Module as TagsModule;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Custom_Product_Brand_Tag extends Tag {

    public function get_name() {
        return 'ccb_product_brand';
    }

    public function get_title() {
        return esc_html__( 'Product Brand Name', 'custom-commerce-boilerplate' );
    }

    public function get_group() {
        return [ 'woocommerce' ];
    }

    public function get_categories() {
        return [ TagsModule::TEXT_CATEGORY ];
    }

    public function render() {
        $product_id = get_the_ID();
        if ( ! $product_id ) {
            return;
        }

        // Check common taxonomy names used in WooCommerce & WoodMart
        $taxonomies = [ 'product_brand', 'pa_brand', 'yith_product_brand' ];
        $brand_name = '';

        foreach ( $taxonomies as $tax ) {
            if ( taxonomy_exists( $tax ) ) {
                $terms = get_the_terms( $product_id, $tax );
                if ( ! empty( $terms ) && ! is_wp_error( $terms ) ) {
                    $brand_name = $terms[0]->name;
                    break;
                }
            }
        }

        if ( ! empty( $brand_name ) ) {
            echo esc_html( $brand_name );
        }
    }
}
