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
 * Delete the game being currenlty viewed. The game is deleted by getting the value of the id control
 * on the page and calling script.js's ajaxDelete() on it. Afterwards the user is redirected to the
 * All Games page.
 */
function deleteGame() {
    ajaxDelete(urls.deletegame, getIdJson(), urls.allgames);
}

/**
 * Update the game being currenlty viewed. It is updated with the details entered by the user
 * into the screen. The game is updated by calling script.js's ajaxSave() and then the user
 * is redirected to the All Games page.
 */
function updateGame() {
    var j = getGameNoId();
    j.id = getIdJson().id;

    if (!validateSaveGame(j)) return;
    ajaxSave(urls.updategame, j, urls.allgames);
}

/**
 * Save a new game using the details entered into the screen. The game is saved by calling 
 * script.js's ajaxSave(). After saving the user is redirected to the All Games page.
 */
function saveGame() {
    var j = getGameNoId();
    if (!validateSaveGame(j)) return;
    ajaxSave(urls.savegame, j, urls.allgames);
}

/**
 * Get the details of the currently viewed game from the page.
 *
 * @return {object} The details of the game as an object.
 */
function getGameNoId() {
    return {
        title: $("#title").val(),
		  genre: $("#genre").val(),
        platform: $("#platform").val(),
        numcopies: $("#numcopies").val(),
        numboxed: $("#numboxed").val(),
        nummanuals: $("#nummanuals").val(),
        datepurchased: $("#datepurchased").val(),
        approximatepurchaseddate: $("#approximatepurchaseddate").is(":checked"),
        notes: $("#notes").val()
    };
}

/**
 * Validate that various required fields of the game have been provided.
 *
 * @param {object} An object containing the details of the game from getGameNoId()
 * @return {bool} true if validation passes, otherwise false.
 */
function validateSaveGame(j) {
    hideValidationFailure();

    var failureText = "";
    if (j.title === "") failureText = "Please enter a title";
    if (j.numcopies === "") failureText = appendText(failureText, "Please enter a number of copies");
    if (j.numboxed === "") failureText = appendText(failureText, "Please enter a number of boxes");
    if (j.nummanuals === "") failureText = appendText(failureText, "Please enter a number of manuals");

    var validatedSuccessfully = failureText === "";

    if (!validatedSuccessfully) showValidationFailure(failureText);
    return validatedSuccessfully;
}

/**
 * Sort the list of games on screen.
 *
 * @param {field} The field to sort by
 */
function sortGames(field) {
    var hdnSort = $('#gamesortfield');
    var hdnDir = $('#gamesortdir');
    var hdnRows = $('#gamerows');

    var oldSortDir = hdnDir.val();
    var newSortDir = "asc";

    var numRows = hdnRows.val() === null ? 999999 : hdnRows.val();

    if (hdnSort.val() == field) newSortDir = toggleSortDirection(oldSortDir);

    hdnSort.val(field);
    hdnDir.val(newSortDir);

    $("#games").load(urls.sortgames, {
        field: field,
        sortdir: newSortDir,
        numrows: numRows
    });

	 var pickers = $(".picker");
	 var val = pickers.val();
    pickers.datepicker();
    pickers.datepicker("option", "dateFormat", "dd/mm/yy");
	 pickers.val(val);
}
