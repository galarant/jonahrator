/*global angular */

//single controller to handle all front-end functionality
function HomeCtrl($http) {
  var self = this;
  self.color_schemes = [{light: '#0099FF', dark: '#007ACC'},
                        {light: '#009933', dark: '#007A29'},
                        {light: '#CC00CC', dark: '#A300A3'},
                        {light: '#9966FF', dark: '#7A52CC'},
                        {light: '#FF6666', dark: '#CC5252'},
                        {light: '#00CC99', dark: '#00A37A'}];

  self.getQuote = function () {
    $http.get('/quote').then(function(response) {
      self.quote = response.data.quote;
      self.changeColors();
    }, function(errResponse) {
      console.error('Error while fetching quote.');
    });
  };

  self.changeColors = function () {
    random_color_scheme = self.color_scheme;
    while (random_color_scheme === self.color_scheme) {
      random_color_scheme = self.color_schemes[Math.floor(Math.random() * self.color_schemes.length)];
    }
    self.color_scheme = random_color_scheme;
  };

  self.facebookShare = function () {
    var fbpopup = window.open("https://www.facebook.com/sharer/sharer.php?u=http://startup-ceo.io", "pop", "width=600, height=400, scrollbars=no");
      return false;
  };

  self.getQuote();
}

angular.module('Jonahrator').controller('HomeCtrl', ['$http', HomeCtrl]);
