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
	 this.login.loginDone('True');
	 assert.ok(this.ajax.showValidationSuccessCalled);
});

QUnit.test('test loginDone with none-true data calls showValidationFailure', function(assert) {
	 this.login.loginDone('False');
	 assert.ok(this.ajax.showValidationFailureCalled);	 
});

QUnit.test('test loginDone with boolean false data doesnt show any validaton message', function(assert) {

	 this.login.loginDone(false);
	 assert.notOk(this.ajax.showValidationSuccessCalled);
	 assert.notOk(this.ajax.showValidationFailureCalled);
});
