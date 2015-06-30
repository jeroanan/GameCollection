module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
		  script_min : {
				options: {
					 sourceMap: true,
					 sourceMapName: 'UI/markup/js/script.min.js.map'
				},
				files: {
					'UI/markup/js/init.min.js': ['UI/markup/js/init.js'],
					'UI/markup/js/script.min.js': ['UI/markup/js/script.js', 'UI/markup/js/validation.js',
															'UI/markup/js/login.js', 'UI/markup/js/editgame.js']
				}
		  }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['uglify']);

};
