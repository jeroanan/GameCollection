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
		  def.reject({'fields': validationResult.fields});
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

	 $('input.addnewplatform').on('click', function(e) {

		  var inputFields = $('form.new-platform-form').find('input');
		  var button = $('input.addnewplatform');

		  e.preventDefault();

		  addLoadingGif(button, 'new-platform-loading-gif');
		  inputFields.attr('disabled', 'true');

		  ajax.hideValidationFailure();

		  platforms.addNewPlatform()
				.done(function() {
					 document.location.reload();
				})
				.fail( function(r) {
					 if (r.fields) showFailure(r.fields, 'platform');
				})
				.always(function() {
					 $('.new-platform-loading-gif').remove();
					 inputFields.removeAttr('disabled');
				});
	 });

	 $('button.addsuggestedplatform').on('click', function(e) {
		  var index = e.currentTarget.attributes['data-index'].value;
		  var name = $('td.suggestedplatformname-' + index).text();
		  var description = $('td.suggestedplatformdescription-' + index).text();
		  var button = $('button.addsuggestedplatform-' + index);
		  var loadingGifClass = 'suggested-platform-loading-gif';

		  e.preventDefault();

		  addLoadingGif(button, loadingGifClass);

		  button.attr('disabled', 'true');
		  
		  platforms.addPlatform(name, description)
		  		.done(function() {
		  			 document.location.reload();
		  		})
		  		.always(function() {
		  			 $('.' + loadingGifClass).remove();
		  			 button.removeAttr('disabled');
		  		});

		  return false;
	 });

	 $('input.saveButton').on ('click', function(e) {
		  var button = $('.saveButton');
		  var loadingGifClass = 'save-platform-loading-gif';
		  var inputs = $('form').find('input');

		  e.preventDefault();

		  ajax.hideValidationFailure();
		  
		  addLoadingGif(button, loadingGifClass);
		  inputs.attr('disabled', 'true');

		  platforms.updatePlatform()
		  		.done(function() { 
		  			 document.location = urls.platforms; 
		  		})
		  		.fail(function(r) { 
		  			 if (r.fields) showFailure(r.fields);						  
		  		})
				.always(function() {
					 $('.' + loadingGifClass).remove();
					 inputs.removeAttr('disabled');
				});
		  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {
		  var inputs = $('form').find('input');
		  var link = $('a.yesDelete');
		  var loadingGifClass = 'delete-platform-loading-gif';

		  e.preventDefault();

		  addLoadingGif(link, loadingGifClass);
		  inputs.attr('disabled', 'true');

		  platforms.deletePlatform()
		  		.done(function() { 
					 document.location = urls.platforms; 
				})
				.always(function() {
					 $('.' + loadingGifClass).remove();
					 inputs.removeAttr('disabled');
				});

		  return false;
	 });
	 if (document.location.pathname === '/editplatform') $('#name').focus();
});
