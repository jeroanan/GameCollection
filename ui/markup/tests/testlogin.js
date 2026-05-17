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

"use strict";

QUnit.module('login tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.login = new Login(this.ajax, urls);
	 }
});

QUnit.test('test loginDone with true data calls showValidationSuccess', function(assert) {
	 var json = JSON.parse('{"result": "ok", "message": "success"}')
	 this.login.loginDone(json);
	 assert.equal(this.ajax.showValidationSuccessMessage, 'Login successful.');
});

QUnit.test('test loginDone with missing username/password calls showValidationFailure', function(assert) {
	 this.login.loginDone(JSON.parse('{"result": "failed", "message": "failed_validation"}'));
	 assert.equal(this.ajax.showValidationFailureMessage, 'Please enter user id and password.');
});

QUnit.test('test loginDone with invalid username/password calls showValidationFailure', function(assert) {
	 this.login.loginDone(JSON.parse('{"result": "failed", "message": "invalid"}'));
	 assert.equal(this.ajax.showValidationFailureMessage, 'Invalid user id or password.');
});

QUnit.test('test loginDone with any other error shows generic login failed message', function(assert) {
	 this.login.loginDone(JSON.parse('{"result": "failed", "message": "bananas"}'));
	 assert.equal(this.ajax.showValidationFailureMessage, 'Error while logging in.');
});
