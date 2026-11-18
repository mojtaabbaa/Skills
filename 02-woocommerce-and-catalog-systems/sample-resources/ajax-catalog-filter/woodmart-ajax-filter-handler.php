<?php
/**
 * WoodMart-Compatible AJAX Catalog Filter Backend Handler
 */

namespace CustomCommerceBoilerplate\WoodMartFilter;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Filter_Handler {

    public function __construct() {
        add_action( 'wp_ajax_woodmart_custom_ajax_filter', [ $this, 'handle_filter_request' ] );
        add_action( 'wp_ajax_nopriv_woodmart_custom_ajax_filter', [ $this, 'handle_filter_request' ] );
    }

    public function handle_filter_request() {
        // Nonce check
        check_ajax_referer( 'woodmart_filter_nonce', 'security' );

        $category = isset( $_POST['category'] ) ? sanitize_text_field( wp_unslash( $_POST['category'] ) ) : '';
        $brand    = isset( $_POST['brand'] ) ? sanitize_text_field( wp_unslash( $_POST['brand'] ) ) : '';
        $season   = isset( $_POST['season'] ) ? sanitize_text_field( wp_unslash( $_POST['season'] ) ) : '';
        $page     = isset( $_POST['page'] ) ? absint( $_POST['page'] ) : 1;
        $orderby  = isset( $_POST['orderby'] ) ? sanitize_key( wp_unslash( $_POST['orderby'] ) ) : 'menu_order';

        $args = [
            'post_type'      => 'product',
            'post_status'    => 'publish',
            'posts_per_page' => apply_filters( 'loop_shop_per_page', 12 ),
            'paged'          => $page,
            'orderby'        => $orderby,
            'tax_query'      => [ 'relation' => 'AND' ],
        ];

        // Ensure catalog visibility
        $args['tax_query'][] = [
            'taxonomy' => 'product_visibility',
            'field'    => 'name',
            'terms'    => [ 'exclude-from-catalog', 'exclude-from-search' ],
            'operator' => 'NOT IN',
        ];

        if ( ! empty( $category ) ) {
            $args['tax_query'][] = [
                'taxonomy' => 'product_cat',
                'field'    => 'slug',
                'terms'    => explode( ',', $category ),
                'operator' => 'IN',
            ];
        }

        if ( ! empty( $brand ) ) {
            $args['tax_query'][] = [
                'taxonomy' => 'product_brand',
                'field'    => 'slug',
                'terms'    => explode( ',', $brand ),
                'operator' => 'IN',
            ];
        }

        if ( ! empty( $season ) ) {
            $args['tax_query'][] = [
                'taxonomy' => 'pa_season',
                'field'    => 'slug',
                'terms'    => explode( ',', $season ),
                'operator' => 'IN',
            ];
        }

        $query = new \WP_Query( $args );

        ob_start();
        if ( $query->have_posts() ) {
            woocommerce_product_loop_start();
            while ( $query->have_posts() ) {
                $query->the_post();
                wc_get_template_part( 'content', 'product' );
            }
            woocommerce_product_loop_end();
        } else {
            wc_get_template( 'loop/no-products-found.php' );
        }
        $loop_html = ob_get_clean();
        wp_reset_postdata();

        wp_send_json_success( [
            'content'     => $loop_html,
            'count'       => $query->found_posts,
            'max_pages'   => $query->max_num_pages,
            'current_page'=> $page,
        ] );
    }
}

new Filter_Handler();
