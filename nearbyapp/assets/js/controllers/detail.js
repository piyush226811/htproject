angular.module('MyApp')
  .controller('DetailCtrl', ['$scope', '$rootScope', '$routeParams', 'Event', 'Subscription',
    function($scope, $rootScope, $routeParams, Event, Subscription) {
        Event.get({ id: $routeParams.id }, function(event) {
            $scope.event = event;

      });
    }]);