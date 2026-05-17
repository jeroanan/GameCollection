module.exports = function(grunt) {
	 
	 // Project configuration.
	 grunt.initConfig({
		  pkg: grunt.file.readJSON('package.json'),
		  jshint: {
				all: ['ui/markup/js/script.js', 'ui/markup/js/editgame.js', 'ui/markup/js/init.js',
						'ui/markup/js/login.js', 'ui/markup/js/require/urls.js',	'ui/markup/js/validation.js',
						'ui/markup/js/platforms.js', 'ui/markup/js/hardwaretypes.js', 'ui/markup/js/genres.js',
						'ui/markup/js/games.js', 'ui/markup/js/hardware.js', 'ui/markup/js/users.js',
						'ui/markup/js/ajax.js', 'ui/markup/js/collection.js']
		  },
		  qunit: {
				all: ['ui/markup/tests/**/*.html']
		  },
		  uglify: {
				script_min : {
					 options: {
						  sourceMap: true,
						  sourceMapName: 'ui/markup/js/script.min.js.map'
					 },
					 files: {
						  'ui/markup/js/init.min.js': 'ui/markup/js/init.js',
						  'ui/markup/js/script.min.js': ['ui/markup/js/script.js', 'ui/markup/js/validation.js',
																	'ui/markup/js/urls.js'],

						  'ui/markup/js/ajax.min.js': 'ui/markup/js/ajax.js',
						  'ui/markup/js/genres.min.js': 'ui/markup/js/genres.js',
						  'ui/markup/js/hardwaretypes.min.js': 'ui/markup/js/hardwaretypes.js',
						  'ui/markup/js/platforms.min.js': 'ui/markup/js/platforms.js',
						  'ui/markup/js/users.min.js': 'ui/markup/js/users.js',
						  'ui/markup/js/failusers.min.js': 'ui/markup/js/failusers.js',
						  'ui/markup/js/hardware.min.js': 'ui/markup/js/hardware.js',
						  'ui/markup/js/games.min.js': 'ui/markup/js/games.js',
						  'ui/markup/js/login.min.js': 'ui/markup/js/login.js',
						  'ui/markup/js/faillogin.min.js': 'ui/markup/js/faillogin.js',
						  'ui/markup/js/collection.min.js': 'ui/markup/js/collection.js'
					 }
				}
		  },
		  cssmin: {
				target: {
					 files: [{
						  src: 'ui/markup/css/style.css',
						  dest: 'ui/markup/css/style.min.css'
					 }]
				}
		  },
		  replace: {
				requireJsCacheBuster: {
					 src: 'ui/markup/js/init.js',
					 overwrite: true,
					 replacements: [{
						  from: /bust=.*\"/g,
						  to: 'bust=<%= grunt.template.today("yyyymmddHHMMss") %>\"'
					 }]
				}
		  },
		  watch: {
				scripts: {
					 files: ['!ui/markup/js/*.min.js', '!ui/markup/js/init/.js', 'ui/markup/js/*.js'],
					 tasks: ['uglify', 'replace']
				}
		  }
	 });

	 grunt.loadNpmTasks('grunt-contrib-qunit');
	 grunt.loadNpmTasks('grunt-contrib-jshint');	 
	 grunt.loadNpmTasks('grunt-contrib-uglify');
	 grunt.loadNpmTasks('grunt-contrib-cssmin');
	 grunt.loadNpmTasks('grunt-text-replace');
	 grunt.loadNpmTasks('grunt-contrib-watch');
	 
	 // Default task(s).
	 grunt.registerTask('default', ['qunit', 'jshint',  'uglify', 'replace', 'cssmin']);
};
