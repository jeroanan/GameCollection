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
 * Delete the item of hardware being currently viewed. This is done using ajax and after the 
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
function deleteHardware() {
	 ajaxDelete(urls.deletehardware, getIdJson(), urls.allhardware);
}

/**
 * Add a new item of hardware. This is done using ajax and after the
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
function addHardware() {
    var j = getHardwareNoId();
    if (!validateSaveHardware(j)) return;
    ajaxSave(urls.savehardware, j, urls.allhardware);
}

/**
 * Update an item of hardware. This is done using ajax and after the
 * item of hardware has been saved the user will be redirected to the All Hardware page.
 */
function updateHardware() {
    var j = getHardwareNoId();
	 j.id = getIdJson().id;
    if (!validateSaveHardware(j)) return;
    ajaxSave(urls.updatehardware, j, urls.allhardware);
}

/**
 * Get the details of the item of hardware currently being viewed.
 * 
 * @return {object} The details of the current item of hardware as an object.
 */
function getHardwareNoId() 
{
    return {
        name: $("#name").val(),
        platform: $("#platform").val(),
        numcopies: $("#numcopies").val(),
        numboxed: $("#numboxed").val(),
        notes: $("#notes").val(),
		  hardwaretype: $("#hardwaretype").val()		  
    };
}

/**
 * Validate that various required fields of the item of hardware have been provided.
 *
 * @param {object} An object containing the details of the item of hardware from getHardwareNoId()
 * @return {bool} true if validation passes, otherwise false.
 */
function validateSaveHardware(j) {
    hideValidationFailure();

    var failureText = "";
    if (j.name === "") failureText = "Please enter a name";
    if (j.numowned === "") failureText = appendText(failureText, "Please enter number owned");
    if (j.numboxed === "") failureText = appendText(failureText, "Please enter number boxed");

    var validationSuccessful = failureText === "";
    if (!validationSuccessful) showValidationFailure(failureText);
    return validationSuccessful;
}

/**
 * Sort the list of items of hardware on screen.
 *
 * @param {field} The field to sort by
 */
function sortHardware(field) {
    var hdnSort = $('#hwsortfield');
    var hdnDir = $('#hwsortdir');
    var hdnRows = $('#gamerows');

    var oldSortDir = hdnDir.val();
    var newSortDir = "asc";
    var numRows = hdnRows.val() === null ? 999999 : hdnRows.val();

    if (hdnSort.val() == field) newSortDir = toggleSortDirection(oldSortDir);

    hdnSort.val(field);
    hdnDir.val(newSortDir);

    $("#hardware").load(urls.sorthardware, {
        field: field,
        sortdir: newSortDir,
        numrows: numRows
    });
}
