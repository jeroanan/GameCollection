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

var Users = function(ajax, urls) {
	 this.ajax = ajax;
	 this.urls = urls;
};

/**
 * Delete a user
 */
Users.prototype.deleteUser = function() {
	 var def = $.Deferred();

	 var j = {"id": this.ajax.getIdJson().id};
	 this.ajax.ajaxDelete(urls.deleteuser, j, urls.users)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });

	 return def;
};

/**
 * Update a user
 */
Users.prototype.updateUser = function () {

	 var def = $.Deferred();

	 j  = {
		  "id": this.ajax.getIdJson().id,
		  "userid": $('#userid').val() 
	 };
	 this.ajax.ajaxSave(urls.updateuser, j)
		  .done(function(r) { def.resolve(r); })
		  .fail(function(r) { def.reject(r); });
	 
	 return def;
};

$(function() {

	 var users = new Users(new Ajax(), urls);

	 $('input.saveButton').on('click', function(e) {
		  e.preventDefault();
		  users.updateUser()
				.done(function() { document.location = '/users'; });
		  return false;
	 });

	 $('a.yesDelete').on('click', function(e) {
		  e.preventDefault();
		  users.deleteUser()
			.done(function() { document.location = '/users'; });
		  return false;
	 });
});
