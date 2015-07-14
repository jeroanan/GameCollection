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

	 var ajaxFunctions = null;

	 if (this.ajaxFunctions === undefined) {
		  ajaxFunctions =  new Ajax();
	 } else {
		  ajaxFunctions =  this.ajaxFunctions;
	 }
	 
	 ajaxFunctions.addNameDescription(this.urls.addgenre, name, description);
};

/**
*Add a genre.
*/
Genres.prototype.addNewGenre = function() {
	 this.ajaxFunctions.addNewNameDescription(this.addGenre);
};

/**
* Delete a genre
*/
Genres.prototype.deleteGenre = function() {
	 this.ajaxFunctions.ajaxDelete(this.urls.deletegenre, this.ajaxFunctions.getIdJson(), this.urls.genres);
};

/**
* Update a genre
*/
Genres.prototype.updateGenre = function () {

	 var ajaxFunctions = null;

	 if (this.ajaxFunctions === undefined) {
		  ajaxFunctions =  new Ajax();
	 } else {
		  ajaxFunctions = this.ajaxFunctions;
	 }
	 
	 ajaxFunctions.updateNameDescription(urls.updategenre, urls.genres);
};

$(function () {	  
	 var genres = new Genres(new Ajax(), urls);

	 $('.addnewgenre').on('click', function () {		  		  
		  genres.addNewGenre();
		  document.location.reload();
		  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  genres.deleteGenre();
		  return false;
	 });		 
	 
	 $('button.addSuggestedGenre').on('click', function(e) {
		  var index = e.currentTarget.attributes['data-index'].value;
		  var genreName = $('td.genreName-' + index).text();
		  var genreDescription = $('td.genreDescription-' + index).text();
		  genres.addGenre(genreName, genreDescription);		  
		  document.location.reload();
		  return false;
	 });

	 $('input.saveButton').on('click', function(e) {
		  e.preventDefault();
		  genres.updateGenre();
	 });
});

