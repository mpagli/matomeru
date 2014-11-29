'use strict';

angular.module('users').controller('UsersController', ['$scope', '$http', '$location', 'Users', 'Authentication',
	function($scope, $http, $location, Users, Authentication) {
		$scope.user = Authentication.user;
		console.log($scope.user);
	}
]);