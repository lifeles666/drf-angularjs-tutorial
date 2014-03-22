'use strict';

/* App Module */

var restApp = angular.module('restApp', [
  'ngRoute',
  'restAppController'
]);

restApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/news', {
        templateUrl: 'news/templates/category-list.html',
        controller: 'CategoryListCtrl'
      }).
      when('/news/:categorySlug', {
        templateUrl: 'news/templates/category-detail.html',
        controller: 'CategoryDetailCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
