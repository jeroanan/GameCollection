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
* Delete a hardware type. This is done by calling script.js's ajaxDelete function
*/
function deleteHardwareType() {
	 ajaxDelete(urls.deletehardwaretype, getIdJson(), urls.hardwaretypes);
}

/**
* Add a hardware type. This is done by calling script.js's addNameDescription function
*
* @param {string} name the name of the new hardware type
* @param {string} description of the new hardware type
*/
function addHardwareType(name, description) {
	 addNameDescription(urls.addhardwaretype, name, description);
}

/**
* Add a hardware type. This is done by calling script.js's addNewNameDescription function
*/
function addNewHardwareType() {
	 addNewNameDescription(addHardwareType);
}

/**
* Update a hardware type. This is done by calling script.js's updateNameDescription function
*/
function updateHardwareType() {
	 updateNameDescription(urls.updatehardwaretype, urls.hardwaretypes);
}
