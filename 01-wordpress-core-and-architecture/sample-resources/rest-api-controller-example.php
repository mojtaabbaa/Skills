<?php
/**
 * Sample Enterprise WordPress REST API Controller
 */
namespace MyPlugin\API;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Sample_REST_Controller extends \WP_REST_Controller {

    protected $namespace = 'myplugin/v1';
    protected $rest_base = 'items';

    public function register_routes() {
        register_rest_route( $this->namespace, '/' . $this->rest_base, [
            [
                'methods'             => \WP_REST_Server::READABLE,
                'callback'            => [ $this, 'get_items' ],
                'permission_callback' => [ $this, 'get_items_permissions_check' ],
                'args'                => $this->get_collection_params(),
            ],
            [
                'methods'             => \WP_REST_Server::CREATABLE,
                'callback'            => [ $this, 'create_item' ],
                'permission_callback' => [ $this, 'create_item_permissions_check' ],
            ],
        ] );
    }

    public function get_items_permissions_check( $request ) {
        // Public or capability check
        return true;
    }

    public function create_item_permissions_check( $request ) {
        return current_user_can( 'manage_options' );
    }

    public function get_items( $request ) {
        $data = [
            [ 'id' => 1, 'title' => 'Sample Item 1', 'status' => 'active' ],
            [ 'id' => 2, 'title' => 'Sample Item 2', 'status' => 'pending' ],
        ];
        return rest_ensure_response( $data );
    }

    public function create_item( $request ) {
        $params = $request->get_json_params();
        $title = isset( $params['title'] ) ? sanitize_text_field( $params['title'] ) : '';

        if ( empty( $title ) ) {
            return new \WP_Error( 'rest_invalid_param', 'Title is required.', [ 'status' => 400 ] );
        }

        return rest_ensure_response( [
            'id'      => 101,
            'title'   => $title,
            'message' => 'Created successfully.',
        ] );
    }
}
