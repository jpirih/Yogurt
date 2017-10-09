var gulp = require('gulp');
var sass = require('gulp-sass');
var notify = require('gulp-notify');

gulp.task('sass', function () {
  return gulp.src('./resources/sass/**/*.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(gulp.dest('./assets/custom/css'))
      .pipe(notify("Sass compiled successfully!"));
});

gulp.task('sass:watch', function () {
  gulp.watch('./resources/sass/**/*.scss', ['sass']);
});