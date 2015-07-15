QUnit.module('hardware types tests', {
	 beforeEach: function() {
		  this.ajax = new Ajax();
		  this.hardwareTypes = new HardwareTypes(this.ajax, urls);
	 }
});

QUnit.test('Test deleteHardwareType calls ajaxDelete', function(assert) {
	 this.hardwareTypes.deleteHardwareType();
	 assert.ok(this.ajax.ajaxDeleteCalled);
});

QUnit.test('Test addHardwareType calls addNameDescription', function(assert) {
	 this.hardwareTypes.addHardwareType('name', 'description');
	 assert.ok(this.ajax.addNameDescriptionCalled);
});

QUnit.test('Test addNewHardwareType calls addNewNameDescription', function(assert) {
	 this.hardwareTypes.addNewHardwareType();
	 assert.ok(this.ajax.addNewNameDescriptionCalled);
 });

QUnit.test('Test updateHardwareType calls updateNameDescription', function(assert) {
	 this.hardwareTypes.updateHardwareType();
	 assert.ok(this.ajax.updateNameDescriptionCalled);
});
