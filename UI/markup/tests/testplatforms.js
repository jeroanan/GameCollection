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
