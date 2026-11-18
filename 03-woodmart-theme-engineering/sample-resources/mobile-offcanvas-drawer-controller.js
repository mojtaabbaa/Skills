/**
 * WoodMart Mobile Off-Canvas Filter Drawer Controller
 * Handles Draft vs. Committed State and Sync with Mobile Toolbar
 */
(function($) {
    'use strict';

    window.WoodmartDrawerHelper = {
        openDrawer: function() {
            $('.wd-open-filter, .wd-off-canvas-btn').first().trigger('click');
        },

        closeDrawer: function() {
            if ($('body').hasClass('wd-off-canvas-opened')) {
                $('.wd-close-side').trigger('click');
            }
        },

        applyDraftFilters: function(callback) {
            this.closeDrawer();
            if (typeof callback === 'function') {
                callback();
            }
        }
    };
})(jQuery);
