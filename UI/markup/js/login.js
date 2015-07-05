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

$(function() {
	 $("#login").on("click", function() {login().done(loginDone);return false;});
	 $("#newuser").on("click", function() {newUser().done(newUserDone);});
});

function login() {
    hideValidationMessages();
    return loginPageAjax("/signin");
}

function loginDone(data) {
	 if (data === false) return;

	 if (data === "True") {
		  showValidationSuccess("Login successful.");
		  setTimeout(function() { navigate("/"); }, 2000);
		  setLoginText();
	 } else {
		  showValidationFailure("Login failed.");
	 }	 
}

function newUser() {
    hideValidationMessages();
    return loginPageAjax("/signup");
}

function newUserDone(data) {
    if (data === false) return;

    if (data=="True") {
        showValidationSuccess("Signed up successfully");
		  setLoginText();
    } else {
        showValidationFailure("Error encountered while signing up");
    }
}

function loginPageAjax(url) {
    if (!validateLoginForm()) {
		  var def = new $.Deferred();
		  def.resolve(false);
		  return def;
	 }
    return $.ajax({
        url: url,
        type: "POST",
        data: {
            userid: $("#userid").val(),
            password: $("#password").val()
        }
    });
}
