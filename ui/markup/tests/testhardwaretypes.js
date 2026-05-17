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

QUnit.module('hardware types tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.hardwareTypes = new HardwareTypes(this.ajax, urls);
	 }
});

QUnit.test('Test deleteHardwareType calls ajaxDelete', function(assert) {
	 this.hardwareTypes.deleteHardwareType();
	 assert.ok(this.ajax.ajaxDeleteCalled);
});

QUnit.test('Test addHardwareType calls addNameDescription', function(assert) {
	 this.hardwareTypes.addHardwareType('name', 'description');
	 assert.ok(this.ajax.addNameDescriptionCalled);
});

QUnit.test('Test addNewHardwareType calls addNewNameDescription', function(assert) {
	 this.hardwareTypes.addNewHardwareType();
	 assert.ok(this.ajax.addNewNameDescriptionCalled);
 });

QUnit.test('Test updateHardwareType calls updateNameDescription', function(assert) {
	 this.hardwareTypes.updateHardwareType();
	 assert.ok(this.ajax.updateNameDescriptionCalled);
});
