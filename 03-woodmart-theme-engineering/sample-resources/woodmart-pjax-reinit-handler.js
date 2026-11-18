/**
 * Comprehensive WoodMart PJAX & AJAX Lifecycle Re-initializer
 */
(function($) {
    'use strict';

    var WoodmartLifecycleController = {
        init: function() {
            this.bindEvents();
            this.onReady();
        },

        bindEvents: function() {
            var self = this;

            // 1. PJAX events (catalog filter, pagination, orderby)
            $(document).on('pjax:start', function() {
                $('.wd-page-content').addClass('wd-loading');
            });

            $(document).on('pjax:complete wdShopPageInit woodmart_ajax_success', function() {
                $('.wd-page-content').removeClass('wd-loading');
                self.reinitCustomModules();
                self.stabilizeStickySidebar();
            });

            // 2. WoodMart Quick View Modal
            $(document).on('woodmart-quick-view-displayed', function() {
                self.initInsideModal($('.wd-quick-view'));
            });

            // 3. Window resize / scroll
            $(window).on('resize scroll', function() {
                self.stabilizeStickySidebar();
            });
        },

        onReady: function() {
            this.reinitCustomModules();
            this.stabilizeStickySidebar();
        },

        reinitCustomModules: function() {
            // Idempotent custom badge or swatch bindings
            $('[data-custom-enhanced]:not([data-initialized])').each(function() {
                $(this).attr('data-initialized', 'true');
            });
        },

        stabilizeStickySidebar: function() {
            var $col = $('.woodmart-shop-sidebar-column');
            if ($col.length) {
                var width = $col.outerWidth();
                $col.find('.elementor-sticky--active').css('width', width + 'px');
            }
        },

        initInsideModal: function($modal) {
            // Modal-scoped initializers
        }
    };

    $(document).ready(function() {
        WoodmartLifecycleController.init();
    });

})(jQuery);
