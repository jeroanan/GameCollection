// Copyright (c) 2015 David Wilson
// Icarus is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// Icarus is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with Icarus.  If not, see <http://www.gnu.org/licenses/>.


var Genres = function(ajaxFunctions, urls) {
	 this.ajaxFunctions = ajaxFunctions;
	 this.urls = urls;
};

/**
* Add a genre.
*
* @param {string} name The name of the new genre
* @param {string} description The description of the new genre
*/
Genres.prototype.addGenre = function(name, description) {	 

	 var def = $.Deferred();
	 var ajaxFunctions = this.ajaxFunctions || new Ajax();
	 
	 var nameDescription = {
		  'name': name,
		  'description': description
	 };

	 var validationResult = ajaxFunctions.validateNameDescription(nameDescription);

	 if (validationResult.result === 'fail') {
		  def.reject(validationResult.fields);
	 } else {
		  ajaxFunctions.addNameDescription(this.urls.addgenre, name, description)
				.done(function(r) { def.resolve(r); })
				.fail(function(r) { def.reject(r); });
	 }

	 return def;
};

/**
*Add a genre.
*/
Genres.prototype.addNewGenre = function() {

	 var def = $.Deferred();
	 
	 var j = { 
		  'name': $('#name').val(),
		  'description': $('#description').val()
	 };
				  
	 var validation = this.ajaxFunctions.validateNameDescription(j);

	 if (validation.result === 'fail') {
		  def.reject({'fields': validation.fields});
	 } else {
		  this.ajaxFunctions.addNewNameDescription(this.addGenre)
				.done(function(r) { def.resolve(r); })
				.fail(function(r) { def.reject(r); });
	 }

	 return def;
};

/**
* Delete a genre
*/
Genres.prototype.deleteGenre = function() {
	 
	 var def = $.Deferred();

	 this.ajaxFunctions.ajaxDelete(this.urls.deletegenre, this.ajaxFunctions.getIdJson())
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
* Update a genre
*/
Genres.prototype.updateGenre = function () {

	 var def = $.Deferred();
	 var ajaxFunctions = this.ajaxFunctions || new Ajax();
	 
	 ajaxFunctions.updateNameDescription(urls.updategenre)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

$(function () {
	 var ajax = new Ajax();
	 var genres = new Genres(ajax, urls);

	 var loadingEnded = function(loadingGifClass, disabledElements) {
		  $('.' + loadingGifClass).remove(); 
		  disabledElements.removeAttr('disabled');
	 };

	 $('.addnewgenre').on('click', function (e) {
		  var button = $('.addnewgenre');
		  var loadingGifClass = 'add-new-genre-lonading-gif';
		  var inputs = $('form').find('input');

		  e.preventDefault();

		  addLoadingGif(button, loadingGifClass);
		  inputs.attr('disabled', 'true');

 		  genres.addNewGenre()
		  		.done(function() { 
					 document.location.reload(); 
				})
				.fail(function(r) {
					 if (r.fields) showFailure(r.fields, 'genre');					 
				})
				.always(function() { 
					 loadingEnded(loadingGifClass, inputs);
				});

		  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {

		  var link = $('a.yesDelete');
		  var loadingGifClass = 'delete-genre-loading-gif';
		  var inputs = $('form').find('input');

		  e.preventDefault();

		  addLoadingGif(link, loadingGifClass);
		  inputs.attr('disabled', 'true');

		  genres.deleteGenre()
		  		.done(function() { 
					 document.location = urls.genres; 
				})
				.always(function() {
					 loadingEnded(loadingGifClass, inputs);
				});

		  return false;
	 });		 
	 
	 $('button.addSuggestedGenre').on('click', function(e) {
		  var index = e.currentTarget.attributes['data-index'].value;
		  var genreName = $('td.genreName-' + index).text();
		  var genreDescription = $('td.genreDescription-' + index).text();
		  var button = $('button.addSuggestedGenre-' + index);
		  var loadingGifClass = 'add-suggested-genre-loading-gif-' + index;

		  addLoadingGif(button, loadingGifClass);
		  button.attr('disabled', 'true');

		  genres.addGenre(genreName, genreDescription)
		  		.done(function() { 
					 document.location.reload(); 
				})
				.always(function() {
					 loadingEnded(loadingGifClass, button);
				});

		  return false;
	 });

	 $('input.saveButton').on('click', function(e) {
		  e.preventDefault();
		  hideValidationFailure();

		  var button = $('input.saveButton');
		  var loadingGifClass = 'save-button-loading-gif';
		  var inputs = $('form').find('input');
		  
		  addLoadingGif(button, loadingGifClass);
		  inputs.attr('disabled', 'true');

		  genres.updateGenre()
		  		.done(function() { 
		  			 document.location = urls.genres; 
		  		})
		  		.fail(function(r) { 
		  			 if (r.fields) showFailure(r.fields, 'genre');
		  		})
				.always(function(r) {
					 loadingEnded(loadingGifClass, inputs);
				});
	 });

	 if (document.location.pathname === '/editgenre') $('#name').focus();
});
