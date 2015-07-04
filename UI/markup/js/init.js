requirejs.config({
	 urlArgs: "bust=v41",
	 baseUrl: '/static/js',
	 paths: {
		  jquery: ['https://code.jquery.com/jquery-2.1.4.min', 'jquery-2.1.4.min'],
		  jqueryui: 'jquery-ui.min',
		  jquerycookie: 'jquery.cookie-1.4.1.min',
		  'bootstrap.min': 'bootstrap.min'
	 }
});

require(['jquery'], function () {
	 require(['jqueryui', 'jquerycookie', 'bootstrap.min'], function () {
		  require(['script.min']);
	 });
});
