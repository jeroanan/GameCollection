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

var Ajax = function() {
};

Ajax.prototype.sendAjax = function(uri, data, successFunc, errorFunc) {
	 
	 var d = $.Deferred();

	 var ajaxParams = {
		  url: uri,
		  data: data,
		  type: 'POST'
	 };
	 if (successFunc) ajaxParams.success = successFunc;
	 if (errorFunc) ajaxParams.error = errorFunc;
	 
	 $.ajax(ajaxParams)
		  .done(function (r) {
				d.resolve(r); 
		  })
		  .fail(function(r) {
				d.reject(r);
		  });

	 return d;
};

Ajax.prototype.loadAjax = function(identifier, loadUrl, data, completeFunc) {
	 $(identifier).load(loadUrl, data, completeFunc);
};

/**
 * Do an ajax call to the given url with a json object containing name and description.
 * 
 * @param {string} uri - The url to be called
 * @param {string} name - The value of the name attribute in the passed object
 * @param {string} description - The value of the description attribute in the passed object
 */
Ajax.prototype.addNameDescription = function (uri, name, description) {
	 var def = $.Deferred();
	 var data = {"name": name,	"description": description};

	 this.sendAjax(uri, data)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });
	 
	 return def;
};

/**
 * Call function f with the values of the name and description elments
 *
 * @param {function} f - The function to call
 */ 
Ajax.prototype.addNewNameDescription = function (f) {
	 var def = $.Deferred();
	 
 	 f($("#name").val(), $("#description").val())
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
 * Delete an item using Ajax
 *
 * @param {string} url - The url to be called by ajax to do the deletion
 * @param {object} data - the details of the item to be deleted
 * @param {string} successUri the uri to redirect the user to when the deletion is successful
 */
Ajax.prototype.ajaxDelete = function (url, data, successUri) {
	 
	 var def = $.Deferred();
	 var ajax = this;
	 if (!this.sendAjax) ajax = new Ajax();
	 ajax.sendAjax(url, data, this.deletionSuccessful, this.deletionFailed)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });
	 
	 return def;
};

/**
 * Called when deletion is successful. It displays a deletion successful message for a few 
 * seconds and then, if one has been provided, reidrects the user to the uri provided in
 * successUri
 */
 Ajax.prototype.deletionSuccessful = function(successUri) {

	  var ajax = this;

	  if(!this.showValidationSuccess) ajax = new Ajax();

 	  ajax.showValidationSuccess("Deletion successful");
	  
 	  setTimeout(function() {
 			ajax.hideValidationSuccess();				
 			if (successUri) navigate(successUri);
 	  }, 3000);
};

/**
 * Called when deletion failes. It displays a deletion failed message.
//  */
Ajax.prototype.deletionFailed = function() {
 	 this.showValidationFailure("Deletion failed");
};

/**
 * Get the values of the id, name and description elements.
 *
 * @return {object} An object containing id, name and description attributes
 */
Ajax.prototype.getIdNameDescriptionJson = function() {
	 return {
		  id: this.getIdJson().id,
		  name: $("#name").val(),
		  description: $("#description").val()
	 };
};

/**
 * Validates that the name and description fields of the screen have been entered.
 *
 * @param {object} j - An object returned from getIdNameDescriptionJson()
 * @return {bool} true if validation passes. false otherwise.
 */
Ajax.prototype.validateSaveNameDescriptionJson = function(j) {

	 var fields = [];

	 if (!j.name) fields.push('name');
	 if (!j.description) fields.push('description');

	 return {
		  'result': fields.length === 0 ? 'ok': 'fail',
		  'fields': fields
	 };
};

/**
 * Append t with a. If t is not empty then place an html linebreak between t and a.
 *
 * @param {string} t - The string to concatenate to
 * @param {string} a - The string to concatenate t with
 * @return {string} The concatenation of t with a, with an html linebreak as necessary
 */
Ajax.prototype.appendText =  function(t, a) {
    if (t !== "") t += "<br />";
    return t + a;
};

/**
 * Call the given uri with the values of the id, name and description elements. If the uri is successful then redirect 
 * to successUri.
 *
 * @param {string} updateUri - The uri to call
 * @param {string} successUri - The uri to redirect the user to if the call to updateUri is successful
 */
Ajax.prototype.updateNameDescription = function(updateUri, successUri) {
	 var def = $.Deferred();
	 
	 var j = this.getIdNameDescriptionJson();

	 var validationResult = this.validateSaveNameDescriptionJson(j);

    if (validationResult.result === 'ok') {		  
		  this.ajaxSave(updateUri, j)
				.done(function(r) { 
					 def.resolve(r);
				})
				.fail(function(r) {  
					 def.reject(r);
				});
	 } else {
		  def.reject({
				'fields': validationResult.fields 
		  });
	 }

	 return def;
};

/**
 * Get the value of the #id element
 *
 * @return {object} An object with an "id" attribute containing the id
 */
Ajax.prototype.getIdJson = function() {
	 return { id: $("#id").val() };
};

/**
 * Saves an item by calling url with data. If a successUri is provided then it is redirected to if the save succeeds.
 *
 * @param {string} url - The url to call in order to perform the save
 * @param {object] data - The details of the items to be saved
 * @param {string} successUri - The uri to be redirected to if the save succeeds
*/
Ajax.prototype.ajaxSave = function(url, data, successUri) {
	 var def = $.Deferred();
	 
	 function getAjax() {
		  if (!this.showValidationSuccess) return new Ajax();
		  return this;
	 }

	 /**
	  * Called when a save operation succeeds. A success message is displayed for a few seconds.
	  * If successUri has a value then the uri it contains is then redirected to.
	  */
	 function saveSuccess() {
		  var ajax = getAjax();

		  ajax.showValidationSuccess("Save Successful");
		  setTimeout(function() {
				ajax.hideValidationSuccess();
				if (successUri) navigate(successUri);
		  }, 3000);
	 }

	 /**
	  * Called when a save operation fails. Display a save failed message.
	  */
	 function saveError() {
		  var ajax = getAjax();
		  ajax.showValidationFailure("Save Failed!");
	 }

	 this.sendAjax(url, data)
		  .done(function(r) {
				saveSuccess();
				def.resolve(r);
		  })
		  .fail(function(r) {
				saveError();
				def.reject(r);
		  });

	 return def;
};

Ajax.prototype.hideValidationBox = function(box) {
    box.fadeOut();
};

Ajax.prototype.hideValidationFailure = function() {
    this.hideValidationBox($("#failure"));
};

Ajax.prototype.showValidationFailure = function(failureText) {
	 this.showValidationMessage($("#failure"), $("#failureText"), failureText);
};

Ajax.prototype.showValidationMessage = function(box, boxTextCtrl, boxTextContent) {    
    boxTextCtrl.html(boxTextContent);
	 box.fadeIn();
};

Ajax.prototype.hideValidationSuccess = function() {
	 this.hideValidationBox($("#success"));
};

Ajax.prototype.showValidationSuccess = function(successText) {
	 this.hideValidationFailure();
    this.showValidationMessage($("#success"), $("#successText"), successText);
};

/**
 * Sets the logged in as/logout text. The user id to display is retrieved from the user_id cookie.
 */
Ajax.prototype.setLoginText = function()
{
	 var userid = $.cookie("user_id");
	 $("#logintext").html("Logged in as " + userid + " | <a href='logout'>(Log out)</a>");	 
};

Ajax.prototype.hideValidationMessages = function() {
	 this.hideValidationSuccess();
	 this.hideValidationFailure();
};

Ajax.prototype.validateNameDescription = function(j)
{
	 var fields = [];

	 if (!j.name || j.name.trim() === '') fields.push('name');
	 if (!j.description || j.description.trim() === '') fields.push('description');

	 return {
		  'result': fields.length === 0 ? 'ok': 'fail',
		  'fields': fields
	 };
};
