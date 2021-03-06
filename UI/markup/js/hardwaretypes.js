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
	 
	 var j = {
		  'name': $('#name').val(),
		  'description': $('#description').val()
	 };

	 var validationResult = this.ajax.validateNameDescription(j);

	 if (validationResult.result === 'fail') {
	 	  def.reject({'fields': validationResult.fields});
	 	  return def;
	 }

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
	 var ajax = new Ajax();
	 var hardwareTypes = new HardwareTypes(ajax, urls);
	 var itemName = 'hardware type';

	 var saveFailed = function(r) {
		  if (r.fields) {
				showFailure(r.fields, itemName);
		  } else {
				ajax.showValidationFailure('Internal error while saving');
		  }
	 };
	 
	 var saveDone = function(r) {
		  if (r==='ok') {
				document.location = urls.hardwaretypes;
		  } else if (r==='already_exists') {
				ajax.showValidationFailure('A hardware type with this name already exists.');
		  } else if (r==='validation_failed') {
				ajax.showValidationFailure('Please enter a hardware type name and description.');
		  } else {
				ajax.showValidationFailure('An error occurred while adding the hardware type.');
		  }
	 };

	 $('button.addnewhardwaretype').on('click', function(e) {		  
		  var button = $('button.addnewhardwaretype');
		  var loadingGifClass = 'add-new-hardware-type-loading-gif';
		  var inputs = $('input');

		  e.preventDefault();

		  doLoading(button, loadingGifClass, inputs);

	 	  hardwareTypes.addNewHardwareType()
		  		.done(function(r) { 
					 var json_result = JSON.parse(r);

					 if (json_result.result) 
						  saveDone(json_result.result);
		  		})
		  		.fail(function(r) {
					 saveFailed(r);
		  		})
				.always(function() {
					 finishedLoading(loadingGifClass, inputs);
				});

	 	  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {

		  var button = $('a.yesDelete');
		  var loadingGifClass = 'delete-hardware-type-loading-gif';
		  var inputs = $('input');
		  
		  e.preventDefault();
		
		  doLoading(button, loadingGifClass, inputs);
		  
		  hardwareTypes.deleteHardwareType()
		   	.done(function(r) { 

					 var json_result = JSON.parse(r);
					 
					 if (json_result.result) {
						  saveDone(json_result.result);
					 }
				})
				.always(function() {
					 finishedLoading(loadingGifClass, inputs);
				});

		  return false;
	 });

	 $('input.saveButton').on('click', function(e) {

		  var button = $('input.saveButton');
		  var loadingGifClass = 'save-hardware-type-loading-gif';
		  var inputs = $('input');

		  e.preventDefault();

		  doLoading(button, loadingGifClass, inputs);

		  hardwareTypes.updateHardwareType()
		  		.done(function(r) { 
					 var json_result = JSON.parse(r);
					 
					 if (json_result.result) {
						  saveDone(json_result.result);
					 }					 
				})
				.fail(function(r) {
					 saveFailed(r);
				})
				.always(function(r) {
					 finishedLoading(loadingGifClass, inputs);
				});

		  return false;
	 });

	 $('button.addsuggestedhardwaretype').on('click', function(e) {

		  var index = e.currentTarget.attributes['data-index'].value;
		  var name = $('td.hardwareTypeName-' + index).text();
		  var description = $('td.hardwareTypeDescription-' + index).text();
		  var button = $('button.addsuggestedhardwaretype-' + index);
		  var loadingGifClass = 'add-suggested-hardware-loading-gif-' + index;

		  e.preventDefault();

		  doLoading(button, loadingGifClass);
		  button.attr('disabled', 'true');

		  hardwareTypes.addHardwareType(name, description)
		  		.done(function(r) { 
					 json_result = JSON.parse(r);
					 
					 if (json_result.result)
						  saveDone(json_result.result);
				})
				.always(function() {
					 finishedLoading(loadingGifClass);
					 button.removeAttr('disabled');
				});

		  return false;
	 });
});
