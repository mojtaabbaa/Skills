<?php
namespace CustomCommerceBoilerplate\Forms;

use ElementorPro\Modules\Forms\Classes\Action_Base;
use Elementor\Controls_Manager;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Custom_Form_Webhook_Action extends Action_Base {

    public function get_name() {
        return 'ccb_custom_webhook';
    }

    public function get_label() {
        return esc_html__( 'Custom Secure Webhook', 'custom-commerce-boilerplate' );
    }

    public function register_settings_section( $widget ) {
        $widget->start_controls_section(
            'section_ccb_webhook',
            [
                'label'     => esc_html__( 'Custom Webhook Settings', 'custom-commerce-boilerplate' ),
                'condition' => [
                    'submit_actions' => $this->get_name(),
                ],
            ]
        );

        $widget->add_control(
            'ccb_webhook_url',
            [
                'label'       => esc_html__( 'Webhook URL', 'custom-commerce-boilerplate' ),
                'type'        => Controls_Manager::TEXT,
                'placeholder' => 'https://api.example.com/v1/lead',
                'description' => esc_html__( 'Endpoint where form data will be transmitted via secure POST.', 'custom-commerce-boilerplate' ),
            ]
        );

        $widget->add_control(
            'ccb_auth_token',
            [
                'label'       => esc_html__( 'Bearer / Secret Token', 'custom-commerce-boilerplate' ),
                'type'        => Controls_Manager::TEXT,
                'description' => esc_html__( 'Optional Authorization header token.', 'custom-commerce-boilerplate' ),
            ]
        );

        $widget->end_controls_section();
    }

    public function run( $record, $ajax_handler ) {
        $settings = $record->get( 'form_settings' );
        $webhook_url = ! empty( $settings['ccb_webhook_url'] ) ? esc_url_raw( $settings['ccb_webhook_url'] ) : '';

        if ( empty( $webhook_url ) ) {
            return;
        }

        $raw_fields = $record->get( 'fields' );
        $payload = [
            'form_name'   => sanitize_text_field( $settings['form_name'] ),
            'submitted_at'=> current_time( 'mysql' ),
            'fields'      => [],
        ];

        foreach ( $raw_fields as $field_id => $field ) {
            $payload['fields'][ $field_id ] = sanitize_text_field( $field['value'] );
        }

        $headers = [
            'Content-Type' => 'application/json',
        ];

        if ( ! empty( $settings['ccb_auth_token'] ) ) {
            $headers['Authorization'] = 'Bearer ' . sanitize_text_field( $settings['ccb_auth_token'] );
        }

        $response = wp_remote_post( $webhook_url, [
            'method'  => 'POST',
            'timeout' => 12,
            'headers' => $headers,
            'body'    => wp_json_encode( $payload ),
        ] );

        if ( is_wp_error( $response ) || 200 !== wp_remote_retrieve_response_code( $response ) ) {
            $ajax_handler->add_error_message( esc_html__( 'External integration error. Submission saved locally.', 'custom-commerce-boilerplate' ) );
        }
    }

    public function on_export( $element ) {
        unset( $element['settings']['ccb_auth_token'] );
        return $element;
    }
}
