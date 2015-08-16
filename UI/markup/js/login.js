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

var Login = function(ajax, urls) {
	 this.ajax = ajax;
	 this.urls = urls;
};


Login.prototype.login = function() {
    this.ajax.hideValidationMessages();
    return this.loginPageAjax("/signin");
};

Login.prototype.loginDone = function(data) {
	 if (data.result === 'ok') {
		  this.ajax.showValidationSuccess('Login successful.');
		  this.ajax.setLoginText();
	 } else if (data.result === 'failed' && data.message === 'failed_validation') {
		  this.ajax.showValidationFailure('Please enter user id and password.');
	 } else if (data.result === 'failed' && data.message === 'invalid') {
		  this.ajax.showValidationFailure('Invalid user id or password.');
	 } else {
		  this.ajax.showValidationFailure('Error while logging in.');
	 }
};

Login.prototype.newUser = function() {
    this.ajax.hideValidationMessages();
    return this.loginPageAjax("/signup");
};

Login.prototype.newUserDone = function(data) {
    if (data === false) return;

    if (data=="True") {
        this.ajax.showValidationSuccess("Signed up successfully");
		  this.ajax.setLoginText();
    } else {
        this.ajax.showValidationFailure("Error encountered while signing up");
    }
};

Login.prototype.loginPageAjax = function(url) {
    if (!this.validateLoginForm()) {
		  var def = new $.Deferxred();
		  def.resolve(JSON.stringify({'result': 'failed', 'message': 'failed_validation'}));
		  return def;
	 }

	 var data = {
        userid: $("#userid").val(),
        password: $("#password").val()
    };

	 return this.ajax.sendAjax(url, data);	 
};

Login.prototype.validateLoginForm = function() {
    var failureText = "";
    if ($("#userid").val() === "") failureText = "Please enter a user id";
    if ($("#password").val() === "") failureText = this.ajax.appendText(failureText, "Please enter a password");
    if (failureText !== "") this.ajax.showValidationFailure(failureText);
    return failureText === "";
};

$(function() {
	 var login = new Login(new Ajax(), urls);
	 $("#login").on("click", function(e) {
		  e.preventDefault();
		  login.login().done(function(d) {
				var data = JSON.parse(d);

				login.loginDone(data);

				if (data.result == 'ok') {
					 document.location = '/';
				}
		  });

		  return false;
	 });

	 $("#newuser").on("click", function(e) {
		  e.preventDefault();
		  
		  login.newUser().done(function(d) {

				newUserDone(d);
				if (d === 'ok') {
					 setTimeout(function() {
						  document.location = '/';
					 }, 2000);
				}
		  });
	 });
	 
	 if (document.location.pathname === '/login') $('#userid').focus();	 
});

