/**
 * Custom Commerce Frontend Scripts
 */
(function($) {
    'use strict';

    window.ccbFrontend = {
        init: function() {
            this.bindEvents();
            this.initComponents();
        },

        bindEvents: function() {
            var self = this;

            // Handle filter clicks using event delegation
            $(document).on('click', '.ccb-filter-btn', function(e) {
                e.preventDefault();
                var category = $(this).data('category');
                self.applyFilter(category, 1);
            });
        },

        initComponents: function() {
            // Idempotent initialization
            $('.ccb-product-card:not([data-ccb-initialized])').each(function() {
                var $card = $(this);
                $card.attr('data-ccb-initialized', 'true');
                // Card specific JS enhancements
            });
        },

        reinit: function() {
            this.initComponents();
        },

        applyFilter: function(category, page) {
            var $target = $('.ccb-products-container');
            $target.addClass('ccb-loading');

            $.ajax({
                url: ccbConfig.ajaxUrl,
                type: 'POST',
                data: {
                    action: 'ccb_filter_products',
                    nonce: ccbConfig.nonce,
                    category: category,
                    page: page
                },
                success: function(response) {
                    if (response.success) {
                        $target.html(response.data.html);
                        window.ccbFrontend.reinit();
                        // If Elementor is active, trigger scoped ready trigger
                        if (window.elementorFrontend && window.elementorFrontend.elementsHandler) {
                            window.elementorFrontend.elementsHandler.runReadyTrigger($target);
                        }
                    }
                },
                complete: function() {
                    $target.removeClass('ccb-loading');
                }
            });
        }
    };

    $(document).ready(function() {
        window.ccbFrontend.init();
    });

})(jQuery);
