requirejs.config({
	 baseUrl: '/static/js',
	 paths: {
		  jquery: 'jquery-2.1.4.min',
		  jqueryui: 'jquery-ui.min',
		  jquerycookie: 'jquery.cookie-1.4.1.min',
		  'bootstrap.min': 'bootstrap.min'
	 },
	 shim: {
		  jqueryui: ['jquery'],
		  jquerycookie: ['jquery'],
		  'bootstrap.min': 'jquery',
		  'script.min': ['jqueryui', 'jquerycookie'],
		  'login.min': ['jquery', 'script.min']
	 }
});

require(['jquery'], function () {
	 require(['jqueryui', 'jquerycookie', 'bootstrap.min'], function () {
		  require(['script.min'], function () {
				require(['login.min']);
		  });
	 });
});
