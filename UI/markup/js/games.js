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

var Games = function(ajax, urls) {
	 this.ajax = ajax;
	 this.urls = urls;
};

/**
 * Delete the game being currenlty viewed. The game is deleted by getting the value of the id control
 * on the page and calling script.js's ajaxDelete() on it. Afterwards the user is redirected to the
 * All Games page.
 */
Games.prototype.deleteGame = function() {
	 this.ajax.ajaxDelete(this.urls.deletegame, this.ajax.getIdJson(), this.urls.allgames);
};

/**
 * Update the game being currenlty viewed. It is updated with the details entered by the user
 * into the screen. The game is updated by calling script.js's ajaxSave() and then the user
 * is redirected to the All Games page.
 */
Games.prototype.updateGame = function() {
	 var j = this.getGameNoId();
    j.id = this.ajax.getIdJson().id;

    if (!this.validateSaveGame(j)) return;
    this.ajax.ajaxSave(urls.updategame, j, urls.allgames);
};

/**
 * Save a new game using the details entered into the screen. The game is saved by calling 
 * script.js's ajaxSave(). After saving the user is redirected to the All Games page.
 */
Games.prototype.saveGame = function() {
	 var j = this.getGameNoId();
    if (!this.validateSaveGame(j)) return;
    this.ajax.ajaxSave(urls.savegame, j, urls.allgames);
};

/**
 * Get the details of the currently viewed game from the page.
 *
 * @return {object} The details of the game as an object.
 */
Games.prototype.getGameNoId = function() {
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
};

/**
 * Validate that various required fields of the game have been provided.
 *
 * @param {object} An object containing the details of the game from getGameNoId()
 * @return {bool} true if validation passes, otherwise false.
 */
Games.prototype.validateSaveGame = function(j) {
	 this.ajax.hideValidationFailure();
	 
	 var failureText = "";
    if (j.title === "") failureText = "Please enter a title";
	 if (j.numcopies === "") failureText = this.ajax.appendText(failureText, "Please enter a number of copies");
    if (j.numboxed === "") failureText = this.ajax.appendText(failureText, "Please enter a number of boxes");
    if (j.nummanuals === "") failureText = this.ajax.appendText(failureText, "Please enter a number of manuals");

	 var validatedSuccessfully = failureText === "";

    if (!validatedSuccessfully) this.ajax.showValidationFailure(failureText);
    return validatedSuccessfully;
};

/**
 * Sort the list of games on screen.
 *
 * @param {field} The field to sort by
 */
Games.prototype.sortGames = function(field) {
	 var hdnSort = $('#gamesortfield');
    var hdnDir = $('#gamesortdir');
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

	 this.ajax.loadAjax('#games', urls.sortgames, loadData, this.initSorting);
};

Games.prototype.initSorting = function(games, status) {
	 if (status!=='1') games = new Games(new Ajax(), urls);

	 $('a.sortgamestitle').on('click', function() {
		  games.sortGames('title');
	 });

	 $('a.sortgamesplatform').on('click', function() {
		  games.sortGames('platform');
	 });

	 $('a.sortgamesnumcopies').on('click', function() {
		  games.sortGames('numcopies');
	 });
};

$(function() {
	 var pickers = $(".picker");
	 var val = pickers.val();
    pickers.datepicker();
    pickers.datepicker("option", "dateFormat", "dd/mm/yy");
	 pickers.val(val);

	 var g = new Games(new Ajax(), urls);
	 g.initSorting(g, '1');

	 $('input.saveButton').on('click', function() {
		  if (document.location.pathname === '/editgame') {
				g.updateGame();
		  }
		  if (document.location.pathname == '/addgame') {
				g.saveGame();
		  }
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  g.deleteGame();
	 });
});
