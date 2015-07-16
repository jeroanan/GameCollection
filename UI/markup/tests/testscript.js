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

QUnit.start();

QUnit.test('toggleSortdirection asc -> desc', function (assert) {
	 assert.equal(toggleSortDirection('asc'), 'desc');
});

QUnit.test('toggleSortDirection desc -> asc', function(assert) {
	 assert.equal(toggleSortDirection('desc'), 'asc');
});

QUnit.test('toggleSortDirection notDesc -> asc', function(assert) {
	 assert.equal(toggleSortDirection('notDesc'), 'asc');
});

QUnit.test('getIdJson -> id', function(assert) {
	 var id = 'my id';
	 $('#id').val(id);
	 assert.equal(getIdJson().id, id);
});

QUnit.test('addNewNameDescription', function(assert) {

	 var nameElementValue = 'myname';
	 var descriptionElementValue = 'mydescription';

	 $('#name').val(nameElementValue);
	 $('#description').val(descriptionElementValue);
	 
	 var name = '';
	 var description = '';
	 
	 var f = function(n, d) {
		  name = n;
		  description = d;
	 }

	 addNewNameDescription(f);
	 assert.equal(name, nameElementValue);
	 assert.equal(description, descriptionElementValue);
});

QUnit.test('appendText first line just includes that text.', function(assert) {
	 var t = '';
	 var a = 'some text';
	 
	 assert.equal(appendText(t, a), a);
});

QUnit.test('appendText inserts html breaks if adding subsequent lines.', function(assert) {
	 var t = 'some text';
	 var a = 'some more text';
	 var expected = t + '<br />' + a;
	 
	 assert.equal(appendText(t, a), expected);
});

