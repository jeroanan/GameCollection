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
				this.hardware[operation](this.hardware, this.ajax);
				assert.ok(this.ajax.ajaxSaveCalled);
		  };

		  this.assertOperationDoesNotCallAjaxSave = function(operation, assert) {
				this.hardware.validateSaveHardwareJson = function(j) { return {'result': 'fail'}; };
				this.hardware[operation](this.hardware, this.ajax);
				assert.notOk(this.ajax.ajaxSaveCalled);
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

QUnit.test('Test sortHardware', function(assert) {
	 this.hardware.sortHardware('title');
	 assert.ok(this.ajax.loadAjaxCalled)
});

QUnit.test('Test validateSaveHardwareJson gives failure for missing required fields', function(assert) {
	 
	 var requiredFields = ['name', 'numowned', 'numboxed'];
	 var hardware = this.hardware;

	 requiredFields.forEach(function(f) {
		  var j = {
				'name': 'myname',
				'numowned': '1',
				'numboxed': '2'
		  };

		  var expected = {
				'result': 'fail',
				'fields': [f]
		  };

		  var origVal = j[f];
		  j[f] = ''

		  var result = hardware.validateSaveHardwareJson(j);	 
		  assert.deepEqual(result, expected);
	 });
	 
});

QUnit.test('Test validateSaveHardwareJson returns success if validation succeeds', function(assert) {
	 var j = {
		  'name': 'myname',
		  'numowned': '1',
		  'numboxed': '2'
	 };

	 var expected = {
		  'result': 'success',
		  'fields': []
	 };

	 var result = this.hardware.validateSaveHardwareJson(j);
	 
	 assert.deepEqual(result, expected);
});
