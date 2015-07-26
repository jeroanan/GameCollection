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

var Ajax = function() {
	 this.addNameDescriptionCalled = false;
	 this.addNewNameDescriptionCalled = false;
	 this.ajaxDeleteCalled = false;
	 this.ajaxSaveCalled = false;
	 this.hideValidationFailureCalled = false;
	 this.loadAjaxCalled = false;
	 this.updateNameDescriptionCalled = false;
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

Ajax.prototype.hideValidationFailure = function() {
	 this.hideValidationFailureCalled = true;
};

Ajax.prototype.showValidationFailure = function(failureText) {};

Ajax.prototype.appendText = function(t, a) {};

Ajax.prototype.loadAjax = function(i, u, d) {
	 this.loadAjaxCalled = true;
};
