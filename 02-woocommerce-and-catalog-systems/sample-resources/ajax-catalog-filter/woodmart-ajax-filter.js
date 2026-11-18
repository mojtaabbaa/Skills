/**
 * WoodMart PJAX-Compatible AJAX Catalog Filter Client
 */
(function($) {
    'use strict';

    var WoodmartCustomFilter = {
        init: function() {
            this.bindEvents();
            this.bindWoodmartEvents();
        },

        bindEvents: function() {
            var self = this;

            // Desktop immediate apply
            $(document).on('change', '.woodmart-desktop-filter input[type="checkbox"]', function() {
                self.runQuery();
            });

            // Mobile Apply Button
            $(document).on('click', '.woodmart-mobile-filter-apply', function(e) {
                e.preventDefault();
                // Close WoodMart off-canvas filter drawer
                if ($('body').hasClass('wd-off-canvas-opened')) {
                    $('.wd-close-side').trigger('click');
                }
                self.runQuery();
            });
        },

        bindWoodmartEvents: function() {
            var self = this;

            // Re-sync after WoodMart PJAX navigation
            $(document).on('pjax:complete wdShopPageInit woodmart_ajax_success', function() {
                self.onPjaxComplete();
            });
        },

        onPjaxComplete: function() {
            // Stabilize sticky columns in Elementor flexbox containers
            var $col = $('.woodmart-filter-sidebar-col');
            if ($col.length) {
                var width = $col.outerWidth();
                $col.find('.elementor-sticky--active').css('width', width + 'px');
            }
        },

        collectState: function() {
            var categories = [];
            $('.woodmart-filter-cat:checked').each(function() {
                categories.push($(this).val());
            });

            var brands = [];
            $('.woodmart-filter-brand:checked').each(function() {
                brands.push($(this).val());
            });

            return {
                category: categories.join(','),
                brand: brands.join(','),
                page: 1
            };
        },

        runQuery: function() {
            var state = this.collectState();
            var $container = $('.wd-page-content');
            $container.addClass('wd-loading');

            $.ajax({
                url: woodmartFilterConfig.ajaxUrl,
                type: 'POST',
                data: $.extend({
                    action: 'woodmart_custom_ajax_filter',
                    security: woodmartFilterConfig.nonce
                }, state),
                success: function(res) {
                    if (res.success) {
                        $container.find('.products').replaceWith(res.data.content);
                        // Trigger WoodMart native reinit events
                        $(document).trigger('wdShopPageInit');
                        $(document).trigger('woodmart_ajax_success');
                    }
                },
                complete: function() {
                    $container.removeClass('wd-loading');
                }
            });
        }
    };

    $(document).ready(function() {
        WoodmartCustomFilter.init();
    });

})(jQuery);
