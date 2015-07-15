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
