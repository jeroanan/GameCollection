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

QUnit.module('genres tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.genres = new Genres(this.ajax, urls);
	 }
});

QUnit.test('Test addGenre calls addNameDescription', function (assert) {
	 this.genres.addGenre('name', 'descritption');	 
	 assert.equal(this.ajax.addNameDescriptionCalled, true);
});

QUnit.test('Test addNewGenre calls addNewNameDescription', function(assert) {
	 this.genres.addNewGenre();
	 assert.equal(this.ajax.addNewNameDescriptionCalled, true);
});

QUnit.test('Test deleteGenre calls ajaxDelete', function(assert) {
	 this.genres.deleteGenre();
	 assert.equal(this.ajax.ajaxDeleteCalled, true);
});

QUnit.test('Test updateGenre calls updateNameDescription', function(assert) {
	 this.genres.updateGenre();
	 assert.equal(this.ajax.updateNameDescriptionCalled, true);
});
