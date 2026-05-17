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

function validateLoginForm() {
    var failureText = "";
    if ($("#userid").val() === "") failureText = "Please enter a user id";
    if ($("#password").val() === "") failureText = appendText(failureText, "Please enter a password");
    if (failureText !== "") showValidationFailure(failureText);
    return failureText === "";
}

function showValidationSuccess(successText) {
	 hideValidationFailure();
    showValidationMessage($("#success"), $("#successText"), successText);
}

function hideValidationMessages() {
	 hideValidationSuccess();
	 hideValidationFailure();
}

function hideValidationSuccess() {
    hideValidationBox($("#success"), $("#successText"));
}

function hideValidationFailure() {
    hideValidationBox($("#failure"), $("#failureText"));
}

function hideValidationBox(box, boxText) {
    box.fadeOut();
}

function showValidationFailure(failureText) {
    showValidationMessage($("#failure"), $("#failureText"), failureText);
}

function showValidationMessage(box, boxTextCtrl, boxTextContent) {    
    boxTextCtrl.html(boxTextContent);
	 box.fadeIn();
}
