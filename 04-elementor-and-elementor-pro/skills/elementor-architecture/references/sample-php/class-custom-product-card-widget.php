<?php
namespace CustomCommerceBoilerplate\Widgets;

use Elementor\Widget_Base;
use Elementor\Controls_Manager;
use Elementor\Group_Control_Typography;
use Elementor\Group_Control_Border;
use Elementor\Group_Control_Box_Shadow;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Custom_Product_Card_Widget extends Widget_Base {

    public function get_name() {
        return 'ccb_product_card';
    }

    public function get_title() {
        return esc_html__( 'Commerce Product Card', 'custom-commerce-boilerplate' );
    }

    public function get_icon() {
        return 'eicon-product-price';
    }

    public function get_categories() {
        return [ 'woocommerce-elements', 'general' ];
    }

    public function get_keywords() {
        return [ 'woocommerce', 'product', 'card', 'woodmart', 'shop' ];
    }

    protected function register_controls() {
        // CONTENT SECTION
        $this->start_controls_section(
            'section_content',
            [
                'label' => esc_html__( 'Product Settings', 'custom-commerce-boilerplate' ),
                'tab'   => Controls_Manager::TAB_CONTENT,
            ]
        );

        $this->add_control(
            'product_id',
            [
                'label'   => esc_html__( 'Select Product ID', 'custom-commerce-boilerplate' ),
                'type'    => Controls_Manager::NUMBER,
                'default' => '',
                'dynamic' => [
                    'active' => true,
                ],
            ]
        );

        $this->add_control(
            'show_en_title',
            [
                'label'        => esc_html__( 'Show English Title', 'custom-commerce-boilerplate' ),
                'type'         => Controls_Manager::SWITCHER,
                'label_on'     => esc_html__( 'Yes', 'custom-commerce-boilerplate' ),
                'label_off'    => esc_html__( 'No', 'custom-commerce-boilerplate' ),
                'return_value' => 'yes',
                'default'      => 'yes',
            ]
        );

        $this->end_controls_section();

        // STYLE SECTION
        $this->start_controls_section(
            'section_style_typography',
            [
                'label' => esc_html__( 'Typography & Colors', 'custom-commerce-boilerplate' ),
                'tab'   => Controls_Manager::TAB_STYLE,
            ]
        );

        $this->add_control(
            'title_color',
            [
                'label'     => esc_html__( 'Title Color', 'custom-commerce-boilerplate' ),
                'type'      => Controls_Manager::COLOR,
                'selectors' => [
                    '{{WRAPPER}} .ccb-card-title' => 'color: {{VALUE}};',
                ],
            ]
        );

        $this->add_group_control(
            Group_Control_Typography::get_type(),
            [
                'name'     => 'title_typography',
                'selector' => '{{WRAPPER}} .ccb-card-title',
            ]
        );

        $this->end_controls_section();
    }

    protected function render() {
        $settings = $this->get_settings_for_display();
        $product_id = ! empty( $settings['product_id'] ) ? absint( $settings['product_id'] ) : get_the_ID();

        if ( ! $product_id ) {
            return;
        }

        $product = wc_get_product( $product_id );
        if ( ! $product ) {
            return;
        }

        $full_title = $product->get_name();
        $persian_title = $full_title;
        $english_title = '';

        if ( strpos( $full_title, '|' ) !== false ) {
            $parts = explode( '|', $full_title, 2 );
            $persian_title = trim( $parts[0] );
            $english_title = trim( $parts[1] );
        }

        ?>
        <div class="ccb-product-card" data-product-id="<?php echo esc_attr( $product_id ); ?>">
            <div class="ccb-card-thumbnail">
                <?php echo $product->get_image( 'woocommerce_thumbnail' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
            </div>
            <div class="ccb-card-body">
                <h3 class="ccb-card-title">
                    <?php echo esc_html( $persian_title ); ?>
                    <?php if ( 'yes' === $settings['show_en_title'] && ! empty( $english_title ) ) : ?>
                        <span class="ccb-en-title" dir="ltr"><?php echo esc_html( $english_title ); ?></span>
                    <?php endif; ?>
                </h3>
                <div class="ccb-card-price">
                    <?php echo $product->get_price_html(); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
                </div>
            </div>
        </div>
        <?php
    }
}
