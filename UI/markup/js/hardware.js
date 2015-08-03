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

var Hardware = function(ajax, urls) {
	 this.ajax = ajax;
	 this.urls = urls;
};

/**
 * Get the details of the item of hardware currently being viewed.
 * 
 * @return {object} The details of the current item of hardware as an object.
 */
Hardware.prototype.getHardwareNoId = function() {
	 return {
        name: $("#name").val(),
        platform: $("#platform").val(),
        numcopies: $("#numcopies").val(),
        numboxed: $("#numboxed").val(),
        notes: $("#notes").val(),
		  hardwaretype: $("#hardwaretype").val()		  
    };
};

/**
 * Delete the item of hardware being currently viewed. This is done using ajax and after the 
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
Hardware.prototype.deleteHardware = function() {

	 var def = $.Deferred();

	 this.ajax.ajaxDelete(urls.deletehardware, this.ajax.getIdJson())
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
 * Add a new item of hardware. This is done using ajax and after the
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
Hardware.prototype.addHardware = function() {
	 var def = $.Deferred();

	 var j = this.getHardwareNoId();

    if (this.validateSaveHardware(j)) {
		  this.ajax.ajaxSave(urls.savehardware, j)
				.done(function(r) { def.resolve(r); })
				.fail(function(r) { def.reject(r); });		  
	 } else {
		  def.reject();
	 }

	 return def;
};

/**
 * Update an item of hardware. This is done using ajax and after the
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
Hardware.prototype.updateHardware = function() {
	 var def = $.Deferred();

	 var j = this.getHardwareNoId();
	 j.id = this.ajax.getIdJson().id;

    if (this.validateSaveHardware(j)) {
		  this.ajax.ajaxSave(urls.updatehardware, j)
				.done(function(r) { def.resolve(r); })
				.fail(function(r) { def.reject(r); });
	 } else {
		  def.reject();
	 }

	 return def;
};

/**
 * Validate that various required fields of the item of hardware have been provided.
 *
 * @param {object} An object containing the details of the item of hardware from getHardwareNoId()
 * @return {bool} true if validation passes, otherwise false.
 */
Hardware.prototype.validateSaveHardware = function(j) {
    this.ajax.hideValidationFailure();

    var failureText = "";
    if (j.name === "") failureText = "Please enter a name";
    if (j.numowned === "") failureText = this.ajax.appendText(failureText, "Please enter number owned");
    if (j.numboxed === "") failureText = this.ajax.appendText(failureText, "Please enter number boxed");

    var validationSuccessful = failureText === "";
    if (!validationSuccessful) this.ajax.showValidationFailure(failureText);
    return validationSuccessful;
};

/**
 * Sort the list of items of hardware on screen.
 *
 * @param {field} The field to sort by
 */
Hardware.prototype.sortHardware = function(field) {
    var hdnSort = $('#hwsortfield');
    var hdnDir = $('#hwsortdir');
    var hdnRows = $('#gamerows');

    var oldSortDir = hdnDir.val();
    var newSortDir = "asc";
    var numRows = hdnRows.val() === null ? 999999 : hdnRows.val();

    if (hdnSort.val() == field) newSortDir = toggleSortDirection(oldSortDir);

    hdnSort.val(field);
    hdnDir.val(newSortDir);
	
	 var loadData = {
        field: field,
        sortdir: newSortDir,
        numrows: numRows
    };

	 this.ajax.loadAjax('#hardware', urls.sorthardware, loadData, this.initSorting);
};

Hardware.prototype.initSorting = function(hardware, status) {
	 if (status!=='1') hardware = new Hardware(new Ajax(), urls);

	 $('a.sorthardwarename').on('click', function(e) {
	 	  hardware.sortHardware('name');
	 });

	 $('a.sorthardwareplatform').on('click', function(e) {
	 	  hardware.sortHardware('platform');
	 });

	 $('a.sorthardwarenumowned').on('click', function(e) {
	 	  hardware.sortHardware('numowned');
	 });
};

$(function() {
	 var h = new Hardware(new Ajax(), urls);
	 
	 h.initSorting(h, '1');

	 $('input.saveButton').on('click', function() {
		  if (document.location.pathname === urls.edithardware) {
				h.updateHardware()
					 .done(function() { document.location = urls.allhardware; });
		  }
		  if (document.location.pathname === urls.addhardware) {
				h.addHardware()
					 .done(function() { document.location = urls.allhardware; });
		  }
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  h.deleteHardware()
				.done(function() { document.location = urls.allhardware; });
		  return false;
	 });
});
