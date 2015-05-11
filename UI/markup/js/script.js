// Copyright (c) 20115 David Wilson
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

function cancelEdit() {
    window.history.back();
}

function cancelEditPlatform() {
    navigate("/platforms");
}

function showDeleteConfirm() {
    $("#deleteConfirm").fadeIn();
}

function hideDeleteConfirm() {
    $("#deleteConfirm").fadeOut();
}

function deleteGame() {
    var j = {
        gameid: $("#id").val()
    };

    ajaxDelete("/deletegame", j);
}

function deletePlatform() {
    var j = {
            platformid: $("#id").val()
    };

    ajaxDelete("/deleteplatform", j);
}

function ajaxDelete(url, data) {
    $.ajax({
        url: url,
        data: data,
        success: deletionSuccessful,
        error: deletionFailed
    })
}

function deletionSuccessful() {
    showValidationSuccess("Deletion successful");
    setTimeout(function() {
        hideValidationSuccess();
        window.history.back();
    }, 3000)
}

function deletionFailed() {
    showValidationFailure("Deletion failed");
}
function deleteHardware() {
    navigate("/deletehardware?hardwareid=" + $("#id").val());
}

function editGame(id) {
    navigate("/editgame?gameid=" + id);
}

function editHardware(id) {
    navigate("/edithardware?hardwareid=" + id);
}

function editPlatform(id) {
    navigate("/editplatform?platformid=" + id);
}

function addSuggestedPlatform(name, description) {
    navigate("/addplatform?name=" + name + "&description=" + description);
}

function deleteGenre(id) {
    navigate("/deletegenre?genreid=" + id)
}

function navigate(url) {
    window.location = url;
}

function updateGame() {
    var j = getGameNoId();
    j.id = $("#id").val();

    if (!validateSaveGame(j)) return;
    ajaxSave("/updategame", j);
}

function saveGame() {
    var j = getGameNoId();
    if (!validateSaveGame(j)) return;
    ajaxSave("/savegame", j);
}

function getGameNoId() {
    return {
        title: $("#title").val(),
        platform: $("#platform").val(),
        numcopies: $("#numcopies").val(),
        numboxed: $("#numboxed").val(),
        nummanuals: $("#nummanuals").val(),
        datepurchased: $("#datepurchased").val(),
        approximatepurchaseddate: $("#approximatepurchaseddate").is(":checked"),
        notes: $("#notes").val()
    };
}

function validateSaveGame(j) {
    hideValidationFailure();

    var failureText = "";
    if (j.title=="") failureText = "Please enter a title";
    if (j.numcopies=="") failureText = appendText(failureText, "Please enter a number of copies");
    if (j.numboxed=="") failureText = appendText(failureText, "Please enter a number of boxes");
    if (j.nummanuals=="") failureText = appendText(failureText, "Please enter a number of manuals");

    var validatedSuccessfully = failureText == "";

    if (!validatedSuccessfully) showValidationFailure(failureText);
    return validatedSuccessfully;
}

function addHardware() {
    var j = getHardwareNoId();
    if (!validateSaveHardware(j)) return;
    ajaxSave("/savehardware", j);
}

function appendText(t, a) {
    if (t!="") t+="<br />";
    return t + a;
}

function updateHardware() {
    var j = getHardwareNoId();
    j.id = $("#id").val();
    if (!validateSaveHardware(j)) return;
    ajaxSave("/updatehardware", j);
}

function getHardwareNoId() {
    return {
        name: $("#name").val(),
        platform: $("#platform").val(),
        numcopies: $("#numowned").val(),
        numboxed: $("#numboxed").val(),
        notes: $("#notes").val()
    };
}

function validateSaveHardware(j) {
    hideValidationFailure();

    var failureText = "";
    if (j.name == "") failureText = "Please enter a name";
    if (j.numowned == "") failureText = appendText(failureText, "Please enter number owned");
    if (j.numboxed == "") failureText = appendText(failureText, "Please enter number boxed");

    var validationSuccessful = failureText == "";
    if (!validationSuccessful) showValidationFailure(failureText);
    return validationSuccessful;
}

function updatePlatform() {
    var j = {
        id: $("#id").val(),
        name: $("#name").val(),
        description: $("#description").val()
    };
    if (!validateSavePlatform(j)) return;
    ajaxSave("/updateplatform", j);
}

function validateSavePlatform(j) {
    hideValidationFailure();
    var failureText = "";
    if (j.name == "") failureText = "Please enter a name";
    if (j.description == "") failureText = appendText(failureText, "Please enter a deacription")

    var validationSuccessful = failureText == "";
    if (!validationSuccessful) showValidationFailure(failureText);
    return validationSuccessful;
}

function ajaxSave(url, data) {
    $.ajax({
        url: url,
        data: data,
        success: saveSuccess,
        error: saveError
    });
}

function saveSuccess() {
    showValidationSuccess("Save Successful");
    setTimeout(function() {
        hideValidationSuccess();
        window.history.back();
    }, 3000)
}

function saveError() {
    showValidationFailure("Save Failed!");
}

function sortGames(field) {
    var hdnSort = $('#gamesortfield');
    var hdnDir = $('#gamesortdir');
    var hdnRows = $('#gamerows');

    var oldSortDir = hdnDir.val();
    var newSortDir = "asc";

    var numRows = hdnRows.val() == null ? 999999 : hdnRows.val();

    if (hdnSort.val() == field) newSortDir = toggleSortDirection(oldSortDir);

    hdnSort.val(field);
    hdnDir.val(newSortDir);

    $("#games").load("/sortgames", {
        field: field,
        sortdir: newSortDir,
        numrows: numRows
    });
}

function sortHardware(field) {
    var hdnSort = $('#hwsortfield');
    var hdnDir = $('#hwsortdir');
    var hdnRows = $('#gamerows');

    var oldSortDir = hdnDir.val();
    var newSortDir = "asc";
    var numRows = hdnRows.val() == null ? 999999 : hdnRows.val();

    if (hdnSort.val() == field) newSortDir = toggleSortDirection(oldSortDir);

    hdnSort.val(field);
    hdnDir.val(newSortDir);

    $("#hardware").load("/sorthardware", {
        field: field,
        sortdir: newSortDir,
        numrows: numRows
    });
}

function toggleSortDirection(oldSortDir) {
    return oldSortDir == "asc" ? "desc": "asc";
}

$(function() {
	 var sessionStatus = $.cookie("session_status");
	 if (sessionStatus == "1") {
		  setLoginText();
	 } else {
		  $(".authenticated-header").hide();
	 }
})

function setLoginText() {
	 var userid = $.cookie("user_id");
	 $("#logintext").html("Logged in as " + userid + " | <a href='logout'>(Log out)</a>");
	 
}
