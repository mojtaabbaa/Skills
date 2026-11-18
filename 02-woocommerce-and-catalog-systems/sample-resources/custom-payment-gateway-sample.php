<?php
/**
 * Sample WooCommerce Custom Payment Gateway Skeleton
 */
namespace MyPlugin\Commerce;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

add_action( 'plugins_loaded', function() {
    if ( ! class_exists( 'WC_Payment_Gateway' ) ) {
        return;
    }

    class WC_Gateway_Sample_Custom extends \WC_Payment_Gateway {

        public function __construct() {
            $this->id                 = 'custom_gateway';
            $this->icon               = '';
            $this->has_fields         = false;
            $this->method_title       = __( 'Custom Secure Gateway', 'woocommerce' );
            $this->method_description = __( 'Allows custom payments with offsite redirection and IPN callback.', 'woocommerce' );

            $this->init_form_fields();
            $this->init_settings();

            $this->title       = $this->get_option( 'title', 'Custom Gateway' );
            $this->description = $this->get_option( 'description', 'Pay securely through custom portal.' );

            add_action( 'woocommerce_update_options_payment_gateways_' . $this->id, [ $this, 'process_admin_options' ] );
        }

        public function init_form_fields() {
            $this->form_fields = [
                'enabled' => [
                    'title'   => __( 'Enable/Disable', 'woocommerce' ),
                    'type'    => 'checkbox',
                    'label'   => __( 'Enable Custom Gateway', 'woocommerce' ),
                    'default' => 'no',
                ],
                'title' => [
                    'title'       => __( 'Title', 'woocommerce' ),
                    'type'        => 'text',
                    'description' => __( 'Payment method title that the customer will see on checkout.', 'woocommerce' ),
                    'default'     => __( 'Custom Gateway', 'woocommerce' ),
                ],
            ];
        }

        public function process_payment( $order_id ) {
            $order = wc_get_order( $order_id );

            // Process order or get payment URL
            $order->update_status( 'pending', __( 'Awaiting custom gateway payment confirmation.', 'woocommerce' ) );
            wc_reduce_stock_levels( $order_id );
            WC()->cart->empty_cart();

            return [
                'result'   => 'success',
                'redirect' => $this->get_return_url( $order ),
            ];
        }
    }
} );
