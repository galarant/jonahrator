/*global angular */

//single controller to handle all front-end functionality
function HomeCtrl($http) {
  var self = this;
  self.testMessage = "Hello Jonah World";
  self.getQuote = function () {
    $http.get('/quote').then(function(response) {
      self.testMessage = response.data.quote;
    }, function(errResponse) {
      console.error('Error while fetching quote.');
    });
  };
}

angular.module('Jonahrator').controller('HomeCtrl', ['$http', HomeCtrl]);
