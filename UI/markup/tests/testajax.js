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

QUnit.module('ajax tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
	 }
});

QUnit.test('Test addNewNameDescription', function(assert) {

	 var f = function(n, d) {
		  var def = $.Deferred();

		  if (n === expectedName && d == expectedDescription) functionCalled = true; 

		  def.resolve();
		  return def;
	 };
	 
	 var functionCalled = false;
	 var expectedName = $('#name').val();
	 var expectedDescription = $('#description').val();

	 this.ajax.addNewNameDescription(f);
	 
	 assert.ok(functionCalled);
});

QUnit.test('Test addNameDescription makes ajax request', function(assert) {

	 this.ajax.sendAjax = function(u, d) {
		  var def = $.Deferred();

		  if (u === expectedUri && JSON.stringify(d) == JSON.stringify(expectedData)) sendAjaxCalled = true;
		  
		  def.resolve();
		  return def;
	 };

	 var sendAjaxCalled = false;

	 var expectedData = {
		  'name': 'myname',
		  'description': 'mydescription'
	 };
	 var expectedUri = '/something'

	 this.ajax.addNameDescription(expectedUri, expectedData.name, expectedData.description);

	 assert.ok(sendAjaxCalled);
});

QUnit.test('Test ajaxDelete', function(assert) {
	 
	 this.ajax.sendAjax = function(u, d) {
		  var def = $.Deferred();
		  if (u === expectedUri && JSON.stringify(d) == JSON.stringify(expectedData)) sendAjaxCalled = true;

		  def.resolve();
		  return def;
	 };

	 var expectedUri = '/deletesomething';
	 var expectedData = {
		  'id': 'myid'
	 };
	 var sendAjaxCalled = false;

	 this.ajax.ajaxDelete(expectedUri, expectedData);
	 assert.ok(sendAjaxCalled);
});

QUnit.test('Test deletionSuccessful', function(assert) {

	 this.ajax.showValidationSuccess = function(m) {
		  showValidationSuccessCalled = true;
	 };

	 var showValidationSuccessCalled = false;

	 this.ajax.deletionSuccessful('/someuri');

	 assert.ok(showValidationSuccessCalled);
});


QUnit.test('Test deletionFailed', function(assert) {
	 
	 this.ajax.showValidationFailure = function() {
		  showValidationFailureCalled = true;
	 };

	 var showValidationFailureCalled = false;
	 this.ajax.deletionFailed();
	 
	 assert.ok(showValidationFailureCalled);
});

QUnit.test('Test getIdNameDescriptionJson', function(assert) {
	 
	 var expected = {
		  'id': $('#id').val(),
		  'name': $('#name').val(),
		  'description': $('#description').val()
	 };

	 var result = this.ajax.getIdNameDescriptionJson();

	 assert.deepEqual(result, expected);
});

QUnit.test('Test validateSaveNameDescriptionJson calls hideValidationFailure', function(assert) {

	 this.ajax.hideValidationFailure = function() {
		  hideValidationFailureCalled = true;
	 };
	 var hideValidationFailureCalled = false;

	 this.ajax.validateSaveNameDescriptionJson({}); 
	 
	 assert.ok(hideValidationFailureCalled);
});

QUnit.test('Test validateSaveNameDescriptionJson with empty name returns false', function(assert) {
	 var data = {
		  'name': '',
		  'description': $('#description').val()
	 };

	 assertValidateSaveNameDescritpoinJsonReturnsFalse(assert, this.ajax, data);
});

QUnit.test('Test validateSaveNameDescriptionJson with empty description returns false', function(assert) {
	 var data = {
		  'name': $('#name').val(),
		  'description': ''
	 };
	 assertValidateSaveNameDescritpoinJsonReturnsFalse(assert, this.ajax, data);
});

function assertValidateSaveNameDescritpoinJsonReturnsFalse(assert, ajax, data) {
	 ajax.showValidationFailure = function(t) {
		  showValidationFailureCalled = true;
	 };
	 var showValidationFailureCalled = false;

	 var result = ajax.validateSaveNameDescriptionJson(data);

	 assert.notOk(result);
	 assert.ok(showValidationFailureCalled);
}

QUnit.test('Test appendText returns one line of text for first line', function(assert) {
	 var expected = 'test'
	 var result = this.ajax.appendText('', expected);
	 assert.equal(result, expected);
});

QUnit.test('Test appendText returns two lines for second line', function(assert) {
	 var expected = 'test<br />text';
	 var result = this.ajax.appendText('test', 'text');
	 assert.equal(result, expected);
});

QUnit.test('Test updateNameDescription calls ajaxSave if everything is well', function(assert) {
	 this.ajax.ajaxSave = function(uri, j, successUri) {
		  var d = $.Deferred();
		  ajaxSaveCalled = true;
		  d.resolve();
		  return d;
	 };

	 var ajaxSaveCalled = false;
	 this.ajax.updateNameDescription('/someuri', 'someotheruri');
	 
	 assert.ok(ajaxSaveCalled);
});

QUnit.test('Test updateNameDescription does not call ajaxSave if validation fails', function(assert) {
	 this.ajax.ajaxSave = function(uri, j, successUri) {
		  ajaxSaveCalled = true;
	 };

	 this.ajax.validateSaveNameDescriptionJson = function(j) {
		  return false;
	 };

	 var ajaxSaveCalled = false;
	 this.ajax.updateNameDescription('/someuri', 'someotheruri');
	 
	 assert.notOk(ajaxSaveCalled);
});

QUnit.test('Test getIdJson', function(assert) {	 
	 var expected = 'myid';

	 var result = this.ajax.getIdJson();
	 assert.equal(result.id, expected);
});
