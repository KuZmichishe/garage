var AjaxLinks = {
    init: function() {
        this.$container = $('.ajax-link');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        this.$container.on('click', function(e) {
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.message) {
                    self.html(result.message);
                    self.toggleClass('active');
                }
            });
            return false;
        });
    }
}

$(document).ready(function() {
    AjaxLinks.init();
});