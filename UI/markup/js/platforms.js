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

var Platforms = function(ajax, urls) {
	 this.ajax = ajax;
	 this.urls = urls;
};

/**
* Add a new platform (currently used from suggested platforms).
*
* @param {string} name The name of the new platform
* @param {string} description The description of the new platform
*/
Platforms.prototype.addPlatform = function(name, description) {
	 var def = $.Deferred();

	 var ajax = this.ajax || new Ajax();

	 var nameDescription = {
		  'name': name,
		  'description': description
	 };

	 var validationResult = this.ajax.validateNameDescription(nameDescription);
	 
	 if (validationResult.result === 'fail') {
		  def.reject(validationResult.fields);
	 } else {
		  ajax.addNameDescription(urls.addplatform, name, description)
				.done(function(r) { def.resolve(r); })
				.fail(function(r) { def.reject(r); }); 
	 }

	 return def;
};

/**
* Add a new platform by entering one manually.
*/
Platforms.prototype.addNewPlatform = function () {

	 var def = $.Deferred();

	 var nameDescription = {
		  'name': $('#name').val(),
		  'description': $('#description').val()
	 };

	 var validationResult = this.ajax.validateNameDescription(nameDescription);
	 if (validationResult.result === 'fail') {
		  def.reject(validationResult.fields);
	 } else {
		  this.ajax.addNewNameDescription(this.addPlatform)
				.done(function(r) { def.resolve(r); })
				.fail(function(r) { def.reject(r); });	  
	 }	 

	 return def;
};

/**
* Delete a platform.
*/
Platforms.prototype.deletePlatform = function() {
	 var def = $.Deferred();
	 
	 this.ajax.ajaxDelete(urls.deleteplatform, this.ajax.getIdJson())
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
* Update a platform.
*/
Platforms.prototype.updatePlatform = function() {

	 var def = $.Deferred();
	 
	 this.ajax.updateNameDescription(urls.updateplatform)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

$(function() {
	 var ajax = new Ajax();
	 var platforms = new Platforms(ajax, urls);

	 $('button.addnewplatform').on('click', function(e) {
		  e.preventDefault();
		  platforms.addNewPlatform()
				.done(function() {
					 document.location.reload();
				})
				.fail( function(r) {
					 console.log(r);
				});
	 });

	 $('button.addsuggestedplatform').on('click', function(e) {
		  e.preventDefault();
		  var index = e.currentTarget.attributes['data-index'].value;
		  var name = $('td.suggestedplatformname-' + index).text();
		  var description = $('td.suggestedplatformdescription-' + index).text();
		  
		  platforms.addPlatform(name, description)
				.done(function() {
					 document.location.reload();
				})
				.fail(function(r) {
					 console.log(r);
				});
		  return false;
	 });

	 $('input.saveButton').on ('click', function(e) {
		  e.preventDefault();

		  ajax.hideValidationFailure();

		  platforms.updatePlatform()
				.done(function() { 
					 document.location = '/platforms'; 
				})
				.fail(function(r) { 
					 if (r.fields) {
						  var failureText = '';
						  
						  for (var f in r.fields) {
								failureText = ajax.appendText(failureText, 'Please enter a platform ' + r.fields[f]);
						  }

						  ajax.showValidationFailure(failureText);
					 }
				});
		  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  platforms.deletePlatform()
				.done(function() { document.location = '/platforms'; });

		  return false;
	 });
});
