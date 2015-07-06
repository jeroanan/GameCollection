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

QUnit.test('getId -> id', function(assert) {
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
