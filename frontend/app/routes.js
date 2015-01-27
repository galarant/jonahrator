/* global angular */
function appRoutes($routeProvider) {
  $routeProvider.
    when('/home', {
      templateUrl: 'static/app/views/home.html',
    }).
    when('/about', {
      templateUrl: 'static/app/views/about.html',
    }).
    otherwise({
      redirectTo: '/home'
    });
}

angular.module('Jonahrator').config(['$routeProvider', appRoutes]);
