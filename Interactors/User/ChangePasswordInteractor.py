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

from Interactors.Exceptions.InteractorFactoryNotSetException import InteractorFactoryNotSetException
from Interactors.LoggingInteractor import LoggingInteractor

class ChangePasswordInteractor(LoggingInteractor):
    """Logic to change a user's password"""

    def __init__(self):
        super().__init__()
        self.__hash_provider = HashProvider()
    
    def execute(self, user):
        """Use persistence to change a user's password.
        :param user: An object of type User. The user_id and password fields are mandatory.
                     The new password should be set in the password field.
        """
        self.__validate(user)
        get_user_interactor = self.interactor_factory.create("GetUserInteractor")
        db_user = get_user_interactor.execute(user)

        db_user.password=self.__hash_provider.hash_text(user.password)
        self.persistence.change_password(db_user)

    def __validate(self, user):
        if user is None:
            raise TypeError
        if self.interactor_factory is None:
            raise InteractorFactoryNotSetException
        self.validate_string_field("user_id", user.user_id)
        self.validate_string_field("password", user.password)

    def set_hash_provider(self, param):
        """Set the hash provider for this object to use for encrypting passwords.
        :param param: The instance of the HashProvider object to use"""
        if not isinstance(param, HashProvider):
            raise ValueError
        self.__hash_provider = param
