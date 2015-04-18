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

from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.LoggingInteractor import LoggingInteractor


class AddUserInteractor(LoggingInteractor):

    def __init__(self):
        self.__hash_provider = None

    def execute(self, user):
        self.__validate(user)
        self.__stop_if_user_exists(user)
        user.password = self.__hash_provider.hash_text(user.password)
        self.persistence.add_user(user)
        self.logger.info("New user: {user_id}".format(user_id=user.user_id))
        
    def __validate(self, user):
        if user is None:
            raise TypeError
        self.validate_string_field("user_id", user.user_id)
        self.validate_string_field("password", user.password)

    def __stop_if_user_exists(self, user):
        if self.__user_exists(self.persistence.get_user(user)):
            raise UserExistsException

    def __user_exists(self, user):
        return user.user_id != ""

    def set_hash_provider(self, hash_provider):
        self.__hash_provider = hash_provider
    
    def get_hash_provider(self):
        return self.__hash_provider
