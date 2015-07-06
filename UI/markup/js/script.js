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

function cancelEdit() {
    window.history.back();
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

function ajaxDelete(url, data, successUri) {

	 function deletionSuccessful() {
		  showValidationSuccess("Deletion successful");
		  setTimeout(function() {
				hideValidationSuccess();				
				if (successUri) navigate(successUri);
		  }, 3000);
	 }

	 function deletionFailed() {
		  showValidationFailure("Deletion failed");
	 }
	 
    $.ajax({
        url: url,
        data: data,
        success: deletionSuccessful,
        error: deletionFailed
    });
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

function navigate(url) {
    window.location = url;
}

function appendText(t, a) {
    if (t !== "") t += "<br />";
    return t + a;
}

function updateNameDescription(updateUri, successUri) {
	 var j = getIdNameDescriptionJson();
    if (!validateSaveNameDescriptionJson(j)) return;
    ajaxSave(updateUri, j, successUri);
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
    if (j.name === "") failureText = "Please enter a name";
    if (j.description === "") failureText = appendText(failureText, "Please enter a description");

    var validationSuccessful = failureText === "";
    if (!validationSuccessful) showValidationFailure(failureText);
    return validationSuccessful;
}

function ajaxSave(url, data, successUri) {
	 function saveSuccess() {
		  showValidationSuccess("Save Successful");
		  setTimeout(function() {
				hideValidationSuccess();
				if (successUri) navigate(successUri);
		  }, 3000);
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
});

function setLoginText() 
{
	 var userid = $.cookie("user_id");
	 $("#logintext").html("Logged in as " + userid + " | <a href='logout'>(Log out)</a>");	 
}

//end generic functions
function deleteUser(id) {
	 j = {"id": id};
	 ajaxDelete(urls.deleteuser, j, urls.users);
}

function updateUser(id) {
	 j  = {
		  "id": id,
		  "userid": $('#userid').val() 
	 };
	 ajaxSave(urls.updateuser, j, urls.users);
}


