/*global angular */

//single controller to handle all front-end functionality
function QuoteCtrl($http) {
  var self = this;

  self.getQuote = function () {
    $http.get('/quote').then(function(response) {
      self.quote = response.data.quote;
    }, function(errResponse) {
      console.error('Error while fetching quote.');
    });
  };

  self.getQuote();
}

angular.module('Jonahrator').controller('QuoteCtrl', ['$http', QuoteCtrl]);
