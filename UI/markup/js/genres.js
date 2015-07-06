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

/**
* Add a genre. This is done by calling script.js's addNameDescription function
*
* @param {string} name The name of the new genre
* @param {string} description The description of the new genre
*/
function addGenre(name, description) {
	 addNameDescription(urls.addgenre, name, description);
}


/**
*Add a genre. This is done by calling script.js's addNewNameDescription function
*/
function addNewGenre() {
	 addNewNameDescription(addGenre);
}

/**
* Delete a genre by id. This is done using ajax.
*
* @param {string} id The uuid of the genre to be deleted
*/
function deleteGenre(id) {
	 //todo: id param unneeded
	 ajaxDelete(urls.deletegenre, getIdJson(), urls.genres);
}

function updateGenre() {
	 updateNameDescription(urls.updategenre, urls.genres);
}
