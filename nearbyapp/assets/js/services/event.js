angular.module('MyApp')
    .factory('Event', ['$resource', function($resource) {
        return $resource('/api/events/:id', {
            id: '@id'
        },
        {
           'get': { method:'GET' }
       });
    }]);