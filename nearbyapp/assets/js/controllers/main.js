angular.module('MyApp')
  .controller('MainCtrl', ['$scope', 'Event', function($scope, Event) {

    $scope.alphabet = ['0-9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
      'Y', 'Z'];

    $scope.genres = ['Business', 'IT', 'Technology', 'Investment', 'Banking',
      'Entertainment', 'Music', 'Concert', 'Drama', 'Camping', 'Nightout',
      'Talk Show', 'Thriller', 'Travel'];

    $scope.headingTitle = 'Nearby Events';

    $scope.events = Event.query();

    $scope.filterByGenre = function(genre) {
      $scope.events = Event.query({ 'category': genre });
      $scope.headingTitle = genre;
    };

    $scope.filterByAlphabet = function(char) {
      $scope.events = Event.query({ 'title': char });
      $scope.headingTitle = char;
    };
  }]);