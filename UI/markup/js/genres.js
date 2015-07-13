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
	 this.ajaxFunctions.addNameDescription(this.urls.addgenre, name, description);
};

/**
*Add a genre.
*/
Genres.prototype.addNewGenre = function(name, description) {
	 this.ajaxFunctions.addNewNameDescription(this.addGenre);
};

/**
* Delete a genre by id.
*/
Genres.prototype.deleteGenre = function() {
	 this.ajaxFunctions.deleteGenre(this.urls.deletegenre, this.ajaxFunctions.getIdJson(), this.urls.genres);
};

Genres.prototype.updateGenre = function () {
	 this.ajaxFunctions.updateNameDescription(urls.updategenre, urls.genres);
};

/**
* Add a genre. This is done by calling script.js's addNameDescription function
*
* @param {string} name The name of the new genre
* @param {string} description The description of the new genre
*/
function addGenre(name, description) {
	 this.ajaxFunctions.addNameDescription(urls.addgenre, name, description);
}


/**
*Add a genre. This is done by calling script.js's addNewNameDescription function
*/
function addNewGenre() {
	 addNewNameDescription(addGenre);
}

/**
* Delete a genre by id. This is done using ajax.
*/
function deleteGenre() {
	 ajaxDelete(urls.deletegenre, getIdJson(), urls.genres);
}

/**
* Update a genre
*/
function updateGenre() {
	 updateNameDescription(urls.updategenre, urls.genres);
}
