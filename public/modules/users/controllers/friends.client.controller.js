'use strict';

angular.module('users').controller('FriendsController', ['$scope', '$http', '$location', 'Socket', 'Friends', 'Authentication',
	function($scope, $http, $location, Socket, Friends, Authentication) {
		$scope.user = Authentication.user;
		$scope.chat = [];
		this.find = function() {
			$scope.friends = Friends.query();
		};

		$scope.emit = function(buddy, msg) {
			var data = {
				from: $scope.user._id,
				fromName: $scope.user.firstName + ' ' +$scope.user.lastName.slice(0,1)+'.',
				to: buddy._id,
				toName: buddy.displayName,
				load: msg
			}
			Socket.emit('message', JSON.stringify(data));
		};

		Socket.on('message', function(message) {

			var data = JSON.parse(message);
			// console.log(data);
			//if (data.from != $scope.user._id && data.to != $scope.user._id) return;
			$scope.chat.push(data);
		});


		
	}
	]);

angular.module('users').filter('filterMsg', function(){
	return function(msgs, user, friend){
			var filtered = [];
			for(var msg in msgs){
				console.log(msgs[msg])
				if (msgs[msg].from === user._id && msgs[msg].to === friend._id || msgs[msg].from === friend._id && msgs[msg].to === user._id){
					if(msgs[msg].from === user._id ){
						filtered.push('You: '+msgs[msg].load);
					} else {
						filtered.push(msgs[msg].fromName+': '+msgs[msg].load);
					}
				}
			}
			filtered.reverse();
			return filtered.join('\n');
	};
});