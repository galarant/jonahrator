/* global angular */
function appRoutes($routeProvider) {
  $routeProvider.
    when('/quote', {
      templateUrl: 'static/app/views/quote.html',
      controller: 'QuoteCtrl as quote',
    }).
    when('/about', {
      templateUrl: 'static/app/views/about.html',
    }).
    otherwise({
      redirectTo: '/quote'
    });
}

angular.module('Jonahrator').config(['$routeProvider', appRoutes]);
