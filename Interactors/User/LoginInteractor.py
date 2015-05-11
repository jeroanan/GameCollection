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

from Cryptography.HashProvider import HashProvider
from Interactors.LoggingInteractor import LoggingInteractor


class LoginInteractor(LoggingInteractor):
    # Logic for verifying and performing a log-in

    def __init__(self):
        super().__init__()
        self.__hash_provider = HashProvider()

    def execute(self, user):
        """Executes the login logic.
        :param user: An object of type User
        :returns: True if login is successful, otherwise False
        """
        self.__validate(user)
        hashed_pw = self.__hash_provider.hash_text(user.password)
        db_user = self.persistence.get_user(user)
        if db_user.user_id == "":
            self.logger.info("Failed login attempt: unknown user id {user_id}".format(user_id=user.user_id))
            return False
        correct_pw = self.__hash_provider.verify_password(user.password, db_user.password)

        if correct_pw:
            self.logger.info("Successful login: {user_id}".format(user_id=user.user_id))
        else:
            self.logger.info("Failed login attempt: invalid password for {user_id}".format(user_id=user.user_id))
        return correct_pw

    def __validate(self, user):
        if user is None:
            raise TypeError
        self.validate_string_field("user_id", user.user_id)
        self.validate_string_field("password", user.password)

    def set_hash_provider(self, param):
        if not isinstance(param, HashProvider):
            raise ValueError
        self.__hash_provider = param
