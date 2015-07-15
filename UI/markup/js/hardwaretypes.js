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

var HardwareTypes = function(ajaxFunctions, urls) {
	 this.ajax = ajaxFunctions;
	 this.urls = urls;
};

/**
* Delete a hardware type.
*/
HardwareTypes.prototype.deleteHardwareType = function() {
	 this.ajax.ajaxDelete(urls.deletehardwaretype,  this.ajax.getIdJson(), urls.hardwaretypes);
};

/**
* Add a hardware type.
*
* @param {string} name the name of the new hardware type
* @param {string} description of the new hardware type
*/
HardwareTypes.prototype.addHardwareType = function(name, description) {
	 ajax = this.ajax || new Ajax();
	 ajax.addNameDescription(urls.addhardwaretype, name, description);
};

/**
* Add a hardware type.
*/
HardwareTypes.prototype.addNewHardwareType = function() {
	 this.ajax.addNewNameDescription(this.addHardwareType);
};

/**
* Update a hardware type.
*/
HardwareTypes.prototype.updateHardwareType = function() {
	 this.ajax.updateNameDescription(urls.updatehardwaretype, urls.hardwaretypes);
};

$(function() {
	 var hardwareTypes = new HardwareTypes(new Ajax(), urls);

	 $('button.addnewhardwaretype').on('click', function(e) {		  
	 	  hardwareTypes.addNewHardwareType();
		  document.location.reload();
	 	  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  hardwareTypes.deleteHardwareType();
		  return false;
	 });

	 $('input.saveButton').on('click', function(e) {
		  e.preventDefault();
		  hardwareTypes.updateHardwareType();
		  return false;
	 });

	 $('button.addsuggestedhardwaretype').on('click', function(e) {
		  e.preventDefault();
		  var index = e.currentTarget.attributes['data-index'].value;
		  var name = $('td.hardwareTypeName-' + index).text();
		  var description = $('td.hardwareTypeDesription-' + index).text();
		  hardwareTypes.addHardwareType(name, description);
		  document.location.reload();
		  return false;
	 });
});
