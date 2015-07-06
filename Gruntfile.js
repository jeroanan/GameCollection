module.exports = function(grunt) {
	 
	 // Project configuration.
	 grunt.initConfig({
		  pkg: grunt.file.readJSON('package.json'),
		  jshint: {
				all: ['UI/markup/js/script.js', 'UI/markup/js/editgame.js', 'UI/markup/js/init.js',
						'UI/markup/js/login.js', 'UI/markup/js/require/urls.js',	'UI/markup/js/validation.js',
						'UI/markup/js/platforms.js', 'UI/markup/js/hardwaretypes.js', 'UI/markup/js/genres.js']
		  },
		  uglify: {
				script_min : {
					 options: {
						  sourceMap: true,
						  sourceMapName: 'UI/markup/js/script.min.js.map'
					 },
					 files: {
						  'UI/markup/js/init.min.js': ['UI/markup/js/init.js'],
						  'UI/markup/js/script.min.js': ['UI/markup/js/script.js', 'UI/markup/js/validation.js',
																	'UI/markup/js/login.js', 'UI/markup/js/editgame.js',
																	'UI/markup/js/urls.js', 'UI/markup/js/platforms.js',
																	'UI/markup/js/hardwaretypes.js', 'UI/markup/js/genres.js']
					 }
				}
		  },
		  cssmin: {
				target: {
					 files: [{
						  src: 'UI/markup/css/style.css',
						  dest: 'UI/markup/css/style.min.css'
					 }]
				}
		  },
		  replace: {
				requireJsCacheBuster: {
					 src: 'UI/markup/js/init.js',
					 overwrite: true,
					 replacements: [{
						  from: /bust=.*\"/g,
						  to: 'bust=<%= grunt.template.today("yyyymmddHHMMss") %>\"'
					 }]
				}
		  }
	 });
	 
	 grunt.loadNpmTasks('grunt-contrib-uglify');
	 grunt.loadNpmTasks('grunt-contrib-cssmin');
	 grunt.loadNpmTasks('grunt-contrib-jshint');
	 grunt.loadNpmTasks('grunt-text-replace');
	 
	 // Default task(s).
	 grunt.registerTask('default', ['replace', 'jshint', 'uglify', 'cssmin']);
};
