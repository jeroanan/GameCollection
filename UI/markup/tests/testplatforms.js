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

QUnit.module('platforms tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.platforms = new Platforms(this.ajax, urls);
	 }
});

QUnit.test('Test addNewPlatform', function(assert) {
	 this.platforms.addNewPlatform();
	 assert.ok(this.ajax.addNewNameDescriptionCalled);
});

QUnit.test('Test addPlatform calls addNameDescription', function(assert) {
	 this.platforms.addPlatform('name', 'description');
	 assert.ok(this.ajax.addNameDescriptionCalled);
});

QUnit.test('Test deletePlatform calls ajaxDelete', function(assert) {
	 this.platforms.deletePlatform();
	 assert.ok(this.ajax.ajaxDeleteCalled);
});

QUnit.test('Test updatePlatform', function(assert) {
	 this.platforms.updatePlatform();
	 assert.ok(this.ajax.updateNameDescriptionCalled);
});
