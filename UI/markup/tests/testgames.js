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

QUnit.module('games tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.games = new Games(this.ajax, urls);

	 }
});

QUnit.test('test deleteGame calls ajaxDelete', function(assert) {
	 this.games.deleteGame();
	 assert.ok(this.ajax.ajaxDeleteCalled);
});

QUnit.test('test validateSaveGame calls hideValidationFailure', function(assert) {
	 this.games.validateSaveGame({});
	 assert.ok(this.ajax.hideValidationFailureCalled);
});

QUnit.test('test validateSaveGame returns false with missing required fields', function(assert) {
	 function setUp() {
		  return {
				'title': 't',
				'numcopies': 1,
				'numboxed': 2,
				'nummanuals': 3
		  };
	 }

	 var j = setUp();

	 for (var key in j) {
		  j[key] = '';
		  var result = this.games.validateSaveGame(j);
		  assert.notOk(result);
		  j = setUp();
	 }
	 
});

QUnit.test('test validateSaveGame returns true when all is well', function(assert) {

	 var j = {
		  'title': 't',
		  'numcopies': 1,
		  'numboxed': 2,
		  'nummanuals': 3
	 };

	 var result = this.games.validateSaveGame(j);
	 assert.ok(result);
});

QUnit.test('test getGameNoId', function(assert) {
	 
	 var j = {
		  'title': $('#title').val(),
		  'genre': $('#genre').val(),
		  'platform': $('#platform').val(),
		  'numcopies': $('#numcopies').val(),
		  'numboxed': $('#numboxed').val(),
		  'nummanuals': $('#nummanuals').val(),
		  'datepurchased': $('#datepurchased').val(),
		  'approximatepurchaseddate': $('#approximatepurchaseddate').is(':checked'),
		  'notes': $('#notes').val()
	 };

	 var result = this.games.getGameNoId();
	 assert.deepEqual(result, j);
});

QUnit.test('test updateGame calls ajaxSave if all is well', function(assert) {
	 this.games.updateGame(this.games, this.ajax);
	 assert.ok(this.ajax.ajaxSaveCalled);
});

QUnit.test('test updateGame does not call ajaxSave if validation fails', function(assert) {
	 this.games.validateSaveGameJson = function() { 
		  return {
				'result': 'fail',
				'fields': []
		  };
	 }
	 this.games.updateGame(this.games, this.ajax);
	 assert.notOk(this.ajax.ajaxSaveCalled);
});

QUnit.test('test saveGame calls ajaxSave if all is well', function(assert) {
	 this.games.saveGame(this.games, this.ajax);
	 assert.ok(this.ajax.ajaxSaveCalled);
});

QUnit.test('test saveGame does not call ajaxSave if validation fails', function(assert) {
	 this.games.validateSaveGameJson = function() { 
		  return  {
				'result': 'fail',
				'fields': []
		  };
	 };

	 this.games.saveGame(this.games, this.ajax);
	 assert.notOk(this.ajax.ajaxSaveCalled);
});

QUnit.test('test sortGames', function(assert) {
	 this.games.sortGames('title');
	 assert.ok(this.ajax.loadAjaxCalled);
});

QUnit.test('test validateSaveGameJson returns fail when required fields are missing', function(assert) {
	 
	 var fields = ['title', 'platform', 'numcopies', 'numboxed', 'nummanuals'];

	 var j = {
				'title': 'mytitle',
				'platform': 'myplatform',
				'numcopies': '0',
				'numboxed': '1',
				'nummanuals': '2'
	 };

	 fields.map(function(f) {
		  var origVal = j[f];

		  var expected = {
	 			'result': 'fail',
	 			'fields': [f]
	 	  };

		  j[f] = '';

		  var games = new Games(new Ajax(), urls);
	 	  var result = games.validateSaveGameJson(j);

	 	  assert.deepEqual(result, expected);

	 	  j[f] = origVal;
		  
	 });	 
});

QUnit.test('test validateSaveGameJson returns success when all is well', function(assert) {
	 var j = {
				'title': 'mytitle',
				'platform': 'myplatform',
				'numcopies': '0',
				'numboxed': '1',
				'nummanuals': '2'
	 };

	 var expected = {
		  'result': 'success',
		  'fields': []
	 };

	 var result = this.games.validateSaveGameJson(j);
	 
	 assert.deepEqual(result, expected); 
});
