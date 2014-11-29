'use strict';

angular.module('users').factory('getBuddies', ['$resource',
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