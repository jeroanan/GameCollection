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
* Add a new platform by entering one manually.
* This is done by calling script.js's addNewNameDescription function
*/
function addNewPlatform() {
	 addNewNameDescription(addPlatform);
}

/**
* Add a new platform (currently used from suggested platforms).
* This is done by calling script.js's addNameDescription function
*
* @param {string} name The name of the new platform
* @param {string} description The description of the new platform
*/
function addPlatform(name, description) {
	 addNameDescription(urls.addplatform, name, description);
}

/**
* Delete a platform. This is done by calling script.js's ajaxDelete function
*/
function deletePlatform() {
    ajaxDelete(urls.deleteplatform, getIdJson(), urls.platforms);
}

/**
* Update a platform. This is done by calling script.js's updateNameDescription function
*/
function updatePlatform() {
	 updateNameDescription(urls.updateplatform, urls.platforms);
}
