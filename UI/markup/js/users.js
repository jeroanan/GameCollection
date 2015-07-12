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

/**
 * Delete a user
 *
 * @param {string} id The uuid of the user to be deleted
 */
function deleteUser() {
	 j = {"id": getIdJson().id};
	 ajaxDelete(urls.deleteuser, j, urls.users);
}

/**
 * Update a user
 * 
 * @param id The uuid of the user to be updated
 */
function updateUser() {
	 j  = {
		  "id": getIdJson().id,
		  "userid": $('#userid').val() 
	 };
	 ajaxSave(urls.updateuser, j, urls.users);
}
