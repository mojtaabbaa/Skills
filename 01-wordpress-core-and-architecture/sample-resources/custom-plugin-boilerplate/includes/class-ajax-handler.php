<?php
namespace CustomCommerceBoilerplate;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Ajax_Handler {

    public function __construct() {
        add_action( 'wp_ajax_ccb_filter_products', [ $this, 'filter_products' ] );
        add_action( 'wp_ajax_nopriv_ccb_filter_products', [ $this, 'filter_products' ] );
    }

    public function filter_products() {
        // 1. Verify Nonce
        if ( ! isset( $_POST['nonce'] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['nonce'] ) ), 'ccb_ajax_nonce' ) ) {
            wp_send_json_error( [ 'message' => __( 'Security check failed.', 'custom-commerce-boilerplate' ) ], 403 );
        }

        // 2. Validate & Sanitize Input
        $page = isset( $_POST['page'] ) ? absint( $_POST['page'] ) : 1;
        $category = isset( $_POST['category'] ) ? sanitize_text_field( wp_unslash( $_POST['category'] ) ) : '';
        $orderby = isset( $_POST['orderby'] ) ? sanitize_key( wp_unslash( $_POST['orderby'] ) ) : 'date';

        // 3. Build Query
        $args = [
            'post_type'      => 'product',
            'post_status'    => 'publish',
            'posts_per_page' => 12,
            'paged'          => $page,
            'orderby'        => $orderby,
            'order'          => 'DESC',
        ];

        if ( ! empty( $category ) ) {
            $args['tax_query'] = [
                [
                    'taxonomy' => 'product_cat',
                    'field'    => 'slug',
                    'terms'    => $category,
                ],
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
            echo '<p class="woocommerce-info">' . esc_html__( 'No products found matching your selection.', 'custom-commerce-boilerplate' ) . '</p>';
        }
        $html = ob_get_clean();
        wp_reset_postdata();

        wp_send_json_success( [
            'html'        => $html,
            'total'       => $query->found_posts,
            'max_pages'   => $query->max_num_pages,
            'currentPage' => $page,
        ] );
    }
}

new Ajax_Handler();
