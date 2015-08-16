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
Hardware.prototype.addHardware = function(h, a) {
	 var def = $.Deferred();

	 var j = h.getHardwareNoId();
	 
	 var validationResult = h.validateSaveHardwareJson(j);

	 if (validationResult.result === 'fail') {
		  def.reject({'fields': validationResult.fields});
		  return def;
	 }

	 a.ajaxSave(urls.savehardware, j)
		  .done(function(r) { 
				def.resolve(r); 
		  })
		  .fail(function(r) { 
				def.reject(r);
		  });		  

	 return def;
};

/**
 * Update an item of hardware. This is done using ajax and after the
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
Hardware.prototype.updateHardware = function(h, a) {
	 var def = $.Deferred();

	 var j = h.getHardwareNoId();
	 j.id = a.getIdJson().id;

	 var validationResult = h.validateSaveHardwareJson(j);

	 if (validationResult.result === 'fail') {
		  def.reject({'fields': validationResult.fields});
		  return def;
	 }

	 a.ajaxSave(urls.updatehardware, j)
		  .done(function(r) { 
				def.resolve(r); 
		  })
		  .fail(function(r) { 
				def.reject(r); 
		  });

	 return def;
};

Hardware.prototype.validateSaveHardwareJson = function(j) {
	 var requiredFields = ['name', 'numowned', 'numboxed'];

	 var missingFields = requiredFields.filter(function(f) {
		  return j[f] === '';
	 });

	 return {
		  'result': missingFields.length === 0? 'success': 'fail',
		  'fields': missingFields
	 };
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
	 var a = new Ajax();
	 var h = new Hardware(a, urls);
	 
	 h.initSorting(h, '1');

	 $('input.saveButton').on('click', function(e) {

		  var updateHardware = function() {
				if (document.location.pathname === urls.edithardware) return h.updateHardware;
				if (document.location.pathname === urls.addhardware) return h.addHardware;
		  };

		  var saveHardwareFunc = updateHardware();
		  
		  var button = $('input.saveButton');
		  var loadingGifClass = 'save-hardware-loading-gif';
		  var inputs = $('input, select, textarea');		  
		  
		  doLoading(button, loadingGifClass, inputs);

		  e.preventDefault();

		  saveHardwareFunc(h, a)
				.done(function() { 
					 document.location = urls.allhardware; 
				})
				.fail(function(r) {
					 if (r.fields) showFailure(r.fields, 'hardware');
				})
				.always(function() {
					 finishedLoading(loadingGifClass, inputs);
				});
	 });

	 $('a.yesDelete').on('click', function(e) {
		  
		  var link = $('a.yesDelete');
		  var loadingGifClass = 'delete-hardware-loading-gif';
		  var inputs = $('input, select, textarea');
		  
		  e.preventDefault();

		  doLoading(link, loadingGifClass, inputs);
		  h.deleteHardware()
		  		.done(function() { 
					 document.location = urls.allhardware; 
				})
				.always(function() {
					 finishedLoading(loadingGifClass, inputs);
				});
		  return false;
	 });
});
