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
 *  A failing user script for test purposes. The stuff it sends to the 
 *  application will cause some failure, e.g. validation.
 */

'use strict';

var FailLogin = function(ajax, urls) {
	 Login.call(this, ajax, urls);
};

FailLogin.prototype = Object.create(Login.prototype);
FailLogin.prototype.constructor = Login;

FailLogin.prototype.login = function() {
	 $('#userid').val('');
	 return this.loginPageAjax.call(this, '/signin');
};

FailLogin.prototype.loginPageAjax = function(url) {
	 var data = {
        userid: $("#userid").val(),
        password: $("#password").val()
    };
	 return this.ajax.sendAjax(url, data);	
};

$(function() {
	 var login = new FailLogin(new Ajax(), urls);

	 var loginButton = $('#login');

	 loginButton.unbind('click');
	 loginButton.on('click', function(e) {
		  e.preventDefault();
		  login.login().done(function(d) {
				login.loginDone(d);
				if (d == 'True') {
					 document.location = '/';
				}
		  });

		  return false;
	 });

	 $('#newuser').on('click', function(e) {
		  e.preventDefault();
		  
		  login.newUser().done(function(d) {
				newUserDone(d);
				if (d === 'True') {
					 setTimeout(function() {
						  document.location = '/';
					 }, 2000);
				}
		  });
	 });
});


