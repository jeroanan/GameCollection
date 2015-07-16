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

QUnit.module('hardware tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.hardware = new Hardware(this.ajax, urls);
	 }
});


QUnit.test('Test getHardwareNoId', function(assert) {

	 var expected = {
		  'name': 'myname',
		  'platform': 'myplatform',
		  'numcopies': '1',
		  'numboxed': '2',
		  'notes': 'mynotes',
		  'hardwaretype': 'mytype'
	 };
	 
	 var result = this.hardware.getHardwareNoId();

	 assert.deepEqual(result, expected);
});

QUnit.test('Test deleteHardware', function(assert) {
	 this.hardware.deleteHardware()
	 assert.ok(this.ajax.ajaxDeleteCalled);
});
