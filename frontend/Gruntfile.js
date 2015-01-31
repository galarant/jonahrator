// Configure grunt tasks and load grunt plugins.
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    browserify: {
      app: {
        src: ["app/main.js"],
        dest: "dist/main-built.js"
      }
    },
  });

  grunt.loadNpmTasks( "grunt-browserify" );

  // Tasks
  grunt.registerTask( "default", ["browserify"] );
};
