/*global angular */

//single controller to handle all front-end functionality
function QuoteCtrl($http, $scope) {
  var self = this;

  self.getQuote = function () {
    self.quote='';
    $scope.loading = true;
    $http.get('/quote').then(function(response) {
      self.quote = response.data.quote;
      $scope.home.changeColor();
      $scope.loading = false;
    }, function(errResponse) {
      console.error('Error while fetching quote.');
      $scope.loading = false;
    });
  };

  self.getQuote();
}

angular.module('Jonahrator').controller('QuoteCtrl', ['$http', '$scope', QuoteCtrl]);
