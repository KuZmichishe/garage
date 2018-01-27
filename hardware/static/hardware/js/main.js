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
                if (result.success) {
                    self.html(result.message);
                    self.toggleClass('active');
                }
            });
            return false;
        });
    }
}


var AlbumsListPage = {
    init: function() {
        this.$container = $('.albums-container');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        $('.btn-favorite', this.$container).on('click', function(e) {
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.success) {
                    $('.glyphicon-star', self).toggleClass('active');
                }
            });

            return false;
        });
    }
};

var SongsListPage = {
    init: function() {
        this.$container = $('.songs-container');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        $('.btn-favorite', this.$container).on('click', function(e) {
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.success) {
                    $('.glyphicon-star', self).toggleClass('active');
                }
            });

            return false;
        });
    }
};

$(document).ready(function() {
    //AlbumsListPage.init();
    //SongsListPage.init();
    AjaxLinks.init();
});