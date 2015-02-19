global.jQuery = require('../bower_components/jquery/dist/jquery.js');
require('../bower_components/startbootstrap/templates/grayscale/js/jquery.easing.min.js');
require('../bower_components/bootstrap/dist/js/bootstrap.js');
require('../bower_components/angular/angular.js');
require('../bower_components/angular-route/angular-route.js');
require('./app.js');
require('./controllers/home.js');
require('./controllers/quote.js');


//core grayscale JS hacked in because it has a Google Maps dependency that we don't want

/*!
 * Start Bootstrap - Grayscale Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery to collapse the navbar on scroll
jQuery(window).scroll(function() {
    if (jQuery(".navbar").offset().top > 50) {
        jQuery(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        jQuery(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
jQuery(function() {
    jQuery('a.page-scroll').bind('click', function(event) {
        var jQueryanchor = jQuery(this);
        jQuery('html, body').stop().animate({
            scrollTop: jQuery(jQueryanchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

