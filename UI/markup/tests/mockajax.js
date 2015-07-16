var Ajax = function() {
	 this.addNameDescriptionCalled = false;
	 this.addNewNameDescriptionCalled = false;
	 this.ajaxDeleteCalled = false;
	 this.updateNameDescriptionCalled = false;
	 this.ajaxSaveCalled = false;
};

Ajax.prototype.addNameDescription = function(url, name, descritption) {
	 this.addNameDescriptionCalled = true;	 
};

Ajax.prototype.ajaxDelete = function(url1, id, url2) {
	 this.ajaxDeleteCalled = true;
};

Ajax.prototype.addNewNameDescription = function(f) {
	 this.addNewNameDescriptionCalled = true;
};

Ajax.prototype.updateNameDescription = function(uri1, uri2) {
	 this.updateNameDescriptionCalled = true;
};

Ajax.prototype.ajaxSave = function(url, data, successUri) {
	 this.ajaxSaveCalled = true;
};

Ajax.prototype.getIdJson = function () {
	 return "id";
}
