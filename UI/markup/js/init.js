requirejs.config({
	 baseUrl: '/static/js',
	 paths: {
		  jquery: ['//ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min', 
					  'jquery-2.1.4.min'],
		  jqueryui: 'jquery-ui.min',
		  jquerycookie: 'jquery.cookie-1.4.1.min',
		  bootstrap: ['//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min',
						  'bootstrap.min']
	 },
	 shim: {
		  jqueryui: ['jquery'],
		  jquerycookie: ['jquery'],
		  bootstrap: ['jquery'],
		  'script.min': ['jqueryui', 'jquerycookie'],
		  'login.min': ['jquery', 'script.min']
	 }
});

require(['bootstrap', 'script.min', 'login.min']);
