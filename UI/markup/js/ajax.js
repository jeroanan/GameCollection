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
	 var thing = null;
};

/**
 * Do an ajax call to the given url with a json object containing name and description.
 * When the call has beeen made the current page reloads.
 * 
 * @param {string} url - The url to be called
 * @param {string} name - The value of the name attribute in the passed object
 * @param {string} description - The value of the description attribute in the passed object
 */
Ajax.prototype.addNameDescription = function (url, name, description) {
	 $.ajax({
		  url: url,
		  data: {"name": name,
					"description": description}});
};

/**
 * Call function f with the values of the name and description elments
 *
 * @param {function} f - The function to call
 */ 
Ajax.prototype.addNewNameDescription = function (f) {
	 f($("#name").val(), $("#description").val());
};

/**
 * Delete an item using Ajax
 *
 * @param {string} url - The url to be called by ajax to do the deletion
 * @param {object} data - the details of the item to be deleted
 * @param {string} successUri the uri to redirect the user to when the deletion is successful
 */
Ajax.prototype.ajaxDelete = function (url, data, successUri) {

	 /**
	  * Called when deletion is successful. It displays a deletion successful message for a few 
	  * seconds and then, if one has been provided, reidrects the user to the uri provided in
	  * successUri
	  */
	 function deletionSuccessful() {
		  showValidationSuccess("Deletion successful");
		  setTimeout(function() {
				hideValidationSuccess();				
				if (successUri) navigate(successUri);
		  }, 3000);
	 }

	 /**
	  * Called when deletion failes. It displays a deletion failed message.
	  */
	 function deletionFailed() {
		  showValidationFailure("Deletion failed");
	 }
	 
    $.ajax({
        url: url,
        data: data,
        success: deletionSuccessful,
        error: deletionFailed
    });
};

/**
 * Call the giveen uri with the values of the id, name and description elements. If the uri is successful then redirect 
 * to successUri.
 *
 * @param {string} updateUri - The uri to call
 * @param {string} successUri - The uri to redirect the user to if the call to updateUri is successful
 */
Ajax.prototype.updateNameDescription = function(updateUri, successUri) {

	 /**
	  * Get the values of the id, name and description elements.
	  *
	  * @return {object} An object containing id, name and description attributes
	  */
	 function getIdNameDescriptionJson() {
		  return {
				id: getIdJson().id,
				name: $("#name").val(),
				description: $("#description").val()
		  };
	 }
	 
	 /**
	  * Validates that the name and description fields of the screen have been entered.
	  *
	  * @param {object} j - An object returned from getIdNameDescriptionJson()
	  * @return {bool} true if validation passes. false otherwise.
	  */
	 function validateSaveNameDescriptionJson(j) {		  
		  hideValidationFailure();
		  var failureText = "";
		  if (j.name === "") failureText = "Please enter a name";
		  if (j.description === "") failureText = appendText(failureText, "Please enter a description");
		  
		  var validationSuccessful = failureText === "";
		  if (!validationSuccessful) showValidationFailure(failureText);
		  return validationSuccessful;
	 }
	 
	 var j = getIdNameDescriptionJson();
    if (!validateSaveNameDescriptionJson(j)) return;
    ajaxSave(updateUri, j, successUri);
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
	 /**
	  * Called when a save operation succeeds. A success message is displayed for a few seconds.
	  * If successUri has a value then the uri it contains is then redirected to.
	  */
	 function saveSuccess() {
		  showValidationSuccess("Save Successful");
		  setTimeout(function() {
				hideValidationSuccess();
				if (successUri) navigate(successUri);
		  }, 3000);
	 }

	 /**
	  * Called when a save operation fails. Display a save failed message.
	  */
	 function saveError() {
		  showValidationFailure("Save Failed!");
	 }

    $.ajax({
		  type: 'post',
        url: url,
        data: data,
        success: saveSuccess,
        error: saveError
    });
};
