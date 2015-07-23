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

		  this.assertOperationCallsAjaxSave = function(operation, assert) {
				this.hardware[operation]();
				assert.ok(this.ajax.ajaxSaveCalled);
		  };

		  this.assertOperationDoesNotCallAjaxSave = function(operation, assert) {
				this.hardware.validateSaveHardware = function(j) { return false };
				this.hardware[operation]();
				assert.notOk(this.ajax.ajaxSaveCalled);
		  };

		  this.assertValidateSaveHardwareReturnsFalseWithMissingField = function(fieldName, assert) {
				var j = {
					 'name': 'myname',
					 'numowned': '1',
					 'numboxed': '1'
				};

				j[fieldName] = '';

				assert.notOk(this.hardware.validateSaveHardware(j));
		  };
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

QUnit.test('Test addHardware calls ajaxSave if all is well', function(assert) {
	 this.assertOperationCallsAjaxSave('addHardware', assert)
});

QUnit.test('Test addHardware does not call ajaxSave if validation fails', function(assert) {
	 this.assertOperationDoesNotCallAjaxSave('addHardware', assert);
});

QUnit.test('Test updateHardware calls ajaxSave if all is well', function(assert) {
	 this.assertOperationCallsAjaxSave('updateHardware', assert)
});

QUnit.test('Test updateHardware does not call ajaxSave if validation fails.', function(assert) {
	 this.assertOperationDoesNotCallAjaxSave('updateHardware', assert);
});

QUnit.test('Test validateSaveHardware returns true if all required fields filled.', function(assert) {
	 var j = {
		  'name': 'myname',
		  'numowned': '1',
		  'numboxed': '1'
	 };

	 assert.ok(this.hardware.validateSaveHardware(j))
});

QUnit.test('Test validateSaveHardware returns false if name is missing.', function(assert) {
	 this.assertValidateSaveHardwareReturnsFalseWithMissingField('name', assert);
});

QUnit.test('Test validateSaveHardware returns false if numowned is missing.', function(assert) {
	 this.assertValidateSaveHardwareReturnsFalseWithMissingField('numowned', assert);
});

QUnit.test('Test validateSaveHardware returns false if numboxed is missing.', function(assert) {
	 this.assertValidateSaveHardwareReturnsFalseWithMissingField('numboxed', assert);
});

QUnit.test('Test sortHardware', function(assert) {
	 this.hardware.sortHardware('title');
	 assert.ok(this.ajax.loadAjaxCalled)
});