'use strict';

/* Controllers */

var restAppController = angular.module('restAppController', []);

restAppController.controller('CategoryListCtrl', ['$scope', '$http',
  function($scope, $http) {
    $http.get('/news.json').success(function(data) {
      $scope.categories = data;
    });
    
    $scope.orderProp = 'id';
    
  }]);

restAppController.controller('CategoryDetailCtrl', ['$scope','$http','$routeParams',
  function($scope,$http, $routeParams) {
	
	$http.get('/news/'+ $routeParams.categorySlug +'.json').success(function(data) {
	$scope.category = data;
	});
  }]);
