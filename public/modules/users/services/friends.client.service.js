'use strict';

//Articles service used for communicating with the articles REST endpoints
angular.module('users').factory('Friends', ['$resource',
	function($resource) {
		return $resource('getBuddies/:articleId', {
			articleId: '@_id'
		}, {
			update: {
				method: 'PUT'
			}
		});
	}
]);