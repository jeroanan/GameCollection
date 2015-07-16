QUnit.module('users tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.users = new Users(this.ajax, urls);
	 }
});

QUnit.test('Test deleteUser calls ajaxDelete', function(assert) {
	 this.users.deleteUser();
	 assert.ok(this.ajax.ajaxDeleteCalled);
});

QUnit.test('Test updateUser calls ajaxSave', function(assert) {
	 this.users.updateUser();
	 assert.ok(this.ajax.ajaxSaveCalled);
});
