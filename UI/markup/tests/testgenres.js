var ajaxFunctions = function() {
	 this.addNameDescriptionCalled = false;
	 this.addNewNameDescriptionCalled = false;
	 this.ajaxDeleteCalled = false;
	 this.updateNameDescriptionCalled = false;
};

ajaxFunctions.prototype.addNameDescription = function(url, name, descritption) {
	 this.addNameDescriptionCalled = true;	 
}

ajaxFunctions.prototype.ajaxDelete = function(url1, id, url2) {
	 this.ajaxDeleteCalled = true;
}

ajaxFunctions.prototype.addNewNameDescription = function(f) {
	 this.addNewNameDescriptionCalled = true;
}

ajaxFunctions.prototype.updateNameDescription = function(uri1, uri2) {
	 this.updateNameDescriptionCalled = true;
}

ajaxFunctions.prototype.getIdJson = function () {
	 return "id";
}

QUnit.module('genres tests', {
	 beforeEach: function() {
		  this.ajax = new ajaxFunctions();
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
