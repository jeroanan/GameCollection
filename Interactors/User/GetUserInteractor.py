# Copyright (c) David Wilson 2015
# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

from Interactors.Interactor import Interactor


class GetUserInteractor(Interactor):
    # Logic to get a user from persistence

    def execute(self, user):
        """Get a user from persistence
        :param user: An object of type user containing the id or user_id of the user to get. The id will take precdence.
        :returns: An object of type User. The retrieved user record.
        """
        def validate(user):
            if user is None:
                raise TypeError

        validate(user)
        return self.persistence.get_user(user)

    

