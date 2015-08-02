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

	 var def = $.Deferred();

	 this.ajax.ajaxDelete(urls.deletehardwaretype,  this.ajax.getIdJson())
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });
	 
	 return def;
};

/**
* Add a hardware type.
*
* @param {string} name the name of the new hardware type
* @param {string} description of the new hardware type
*/
HardwareTypes.prototype.addHardwareType = function(name, description) {

	 var def = $.Deferred();
	 var ajax = this.ajax || new Ajax();

	 ajax.addNameDescription(urls.addhardwaretype, name, description)
		  .done(function(r) { def.resolve(r); } )
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
* Add a hardware type.
*/
HardwareTypes.prototype.addNewHardwareType = function() {

	 var def = $.Deferred();
	 
	 this.ajax.addNewNameDescription(this.addHardwareType)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
* Update a hardware type.
*/
HardwareTypes.prototype.updateHardwareType = function() {

	 var def = $.Deferred();

	 this.ajax.updateNameDescription(urls.updatehardwaretype)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });
	 
	 return def;
};

$(function() {
	 var hardwareTypes = new HardwareTypes(new Ajax(), urls);

	 $('button.addnewhardwaretype').on('click', function(e) {		  
	 	  hardwareTypes.addNewHardwareType()
				.done(function(r) { document.location.reload(); });
	 	  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  hardwareTypes.deleteHardwareType()
				.done(function(r) { document.location = urls.hardwaretypes; });
		  return false;
	 });

	 $('input.saveButton').on('click', function(e) {
		  e.preventDefault();
		  hardwareTypes.updateHardwareType()
				.done(function() { document.location = urls.hardwaretypes; });
		  return false;
	 });

	 $('button.addsuggestedhardwaretype').on('click', function(e) {
		  e.preventDefault();
		  var index = e.currentTarget.attributes['data-index'].value;
		  var name = $('td.hardwareTypeName-' + index).text();
		  var description = $('td.hardwareTypeDesription-' + index).text();
		  hardwareTypes.addHardwareType(name, description)
				.done(function() { document.location.reload(); });
		  return false;
	 });
});
