function cancelEdit() {
    window.history.back();
}

function cancelEditPlatform() {
    navigate(urls.platforms);
} 

function showDeleteConfirm() {
    $("#deleteConfirm").fadeIn();
}

function hideDeleteConfirm() {
    $("#deleteConfirm").fadeOut();
}

function getIdJson() {
	 return { id: $("#id").val() };
}

function deleteHardwareType() {
	 ajaxDelete(urls.deletehardwaretype, getIdJson(), urls.hardwaretypes);
}

function deleteGame() {
    ajaxDelete(urls.deletegame, getIdJson(), urls.allgames);
}

function deletePlatform() {
    ajaxDelete(urls.deleteplatform, getIdJson(), urls.platforms);
}

function ajaxDelete(url, data, successUri) {

	 function deletionSuccessful() {
		  showValidationSuccess("Deletion successful");
		  setTimeout(function() {
				hideValidationSuccess();				
				if (successUri) navigate(successUri);
		  }, 3000)
	 }

	 function deletionFailed() {
		  showValidationFailure("Deletion failed");
	 }
	 
    $.ajax({
        url: url,
        data: data,
        success: deletionSuccessful,
        error: deletionFailed
    })
}

function deleteHardware() {
	 ajaxDelete(urls.deletehardware, getIdJson(), urls.allhardware);
}

function editGame(id) {
	 //TODO: This should just be a hyperlink. No reason for it to be JavaScript.
    navigate("/editgame?gameid=" + id);
}

function editHardware(id) {
	 //TODO: This should just be a hyperlink. No reason for it to be JavaScript.
    navigate("/edithardware?hardwareid=" + id);
}

function editPlatform(id) {
	 //TODO: This should just be a hyperlink. No reason for it to be JavaScript.
    navigate("/editplatform?platformid=" + id);
}

function addNewPlatform() {
	 addNewNameDescription(addPlatform);
}

function addPlatform(name, description) {
	 addNameDescription(urls.addplatform, name, description);
}

function addNewGenre() {
	 addNewNameDescription(addGenre);
}

function addHardwareType(name, description) {
	 //TODO: This should just be a hyperlink. No reason for it to be JavaScript.
	 addNameDescription(urls.addhardwaretype, name, description);
}

function addNewHardwareType() {
	 addNewNameDescription(addHardwareType);
}

function editHardwareType(id) {
	 //TODO: This should just be a hyperlink. No reason for it to be JavaScript.
	 navigate("/edithardwaretype?id=" + id);
}

function addGenre(name, description) {
	 addNameDescription(urls.addgenre, name, description);
}

function addNewNameDescription(f) {
	 f($("#name").val(), $("#description").val());
}

function addNameDescription(url, name, description) {
	 $.ajax({
		  url: url,
		  data: {"name": name,
					"description": description}})
		  .always(function() { document.location.reload(); });
}

function editGenre(id) {
	 //TODO: This should just be a hyperlink. No reason for it to be JavaScript.
	 navigate("/editgenre?genreid=" + id);
}

//todo: id param unneeded
function deleteGenre(id) {
	 ajaxDelete(urls.deletegenre, getIdJson(), urls.genres);
}


function deleteUser(id) {
	 j = {"id": id}
	 ajaxDelete(urls.deleteuser, j, urls.users);
}

function navigate(url) {
    window.location = url;
}

function updateGame() {
    var j = getGameNoId();
    j.id = getIdJson().id;

    if (!validateSaveGame(j)) return;
    ajaxSave(urls.updategame, j, urls.allgames);
}

function saveGame() {
    var j = getGameNoId();
    if (!validateSaveGame(j)) return;
    ajaxSave(urls.savegame, j, urls.allgames);
}

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
    ajaxSave(urls.savehardware, j);
}

function appendText(t, a) {
    if (t!="") t+="<br />";
    return t + a;
}

function updateHardware() {
    var j = getHardwareNoId();
	 j.id = getIdJson().id;
    if (!validateSaveHardware(j)) return;
    ajaxSave(urls.updatehardware, j);
}

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
	 updateNameDescription(urls.updateplatform, urls.platforms);
}

function updateGenre() {
	 updateNameDescription(urls.updategenre, urls.genres);
}

function updateHardwareType() {
	 updateNameDescription(urls.updatehardwaretype, urls.hardwaretypes);
}

function updateNameDescription(updateUri, successUri) {
	 var j = getIdNameDescriptionJson();
    if (!validateSaveNameDescriptionJson(j)) return;
    ajaxSave(updateUri, j, successUri);
}

function updateUser(id) {
	 j  = {
		  "id": id,
		  "userid": $('#userid').val() 
	 };
	 ajaxSave(urls.updateuser, j, urls.users);
}

function getIdNameDescriptionJson() {
	 return {
        id: getIdJson().id,
        name: $("#name").val(),
        description: $("#description").val()
    };
}

function validateSaveNameDescriptionJson(j) {
    hideValidationFailure();
    var failureText = "";
    if (j.name == "") failureText = "Please enter a name";
    if (j.description == "") failureText = appendText(failureText, "Please enter a description")

    var validationSuccessful = failureText == "";
    if (!validationSuccessful) showValidationFailure(failureText);
    return validationSuccessful;
}

function ajaxSave(url, data, successUri) {
	 function saveSuccess() {
		  showValidationSuccess("Save Successful");
		  setTimeout(function() {
				hideValidationSuccess();
				if (successUri) navigate(successUri);
		  }, 3000)
	 }

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

    $("#games").load(urls.sortgames, {
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

    $("#hardware").load(urls.sorthardware, {
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

function setLoginText() 
{
	 var userid = $.cookie("user_id");
	 $("#logintext").html("Logged in as " + userid + " | <a href='logout'>(Log out)</a>");	 
}
