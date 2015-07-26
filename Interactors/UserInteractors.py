"""Interactors for User functionality"""

# Copyright (c) 2015 David Wilson
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
from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.Interactor import Interactor
from Interactors.LoggingInteractor import LoggingInteractor


class AddUserInteractor(LoggingInteractor):
    """Add a user"""

    def __init__(self):
        """Initialise AddUserInteractor"""
        self.__hash_provider = None
        self.__user_exists = lambda user: user.user_id != ""

    def execute(self, user):
        """Add a user.
        :param user: An object of type User. The user to be added"""
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

    def set_hash_provider(self, hash_provider):
        self.__hash_provider = hash_provider

    def get_hash_provider(self):
        return self.__hash_provider


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
        db_user.password = self.__hash_provider.hash_text(user.password)

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


class DeleteUserInteractor(Interactor):
    """Use persistence to delete a user"""

    def execute(self, user):
        """Delete a user.
        :param user: The user to delete. The id property contains the id of the user to delete."""
        self.persistence.delete_user(user)


class GetUserInteractor(Interactor):
    """Get a user"""

    def execute(self, user):
        """Get a user from persistence
        :param user: An object of type user containing the id or user_id of the user to get.
                     The id will take precdence.
        :returns: An object of type User. The retrieved user record.
        """
        def validate(user):
            if user is None:
                raise TypeError

        validate(user)
        return self.persistence.get_user(user)


class GetUsersInteractor(Interactor):
    """Get all users"""

    def execute(self):
        """Get all users
        :returns: A list of User objects. All users."""
        return self.persistence.get_all_users()


class LoginInteractor(LoggingInteractor):
    """Logic for verifying and performing a log-in"""

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
            self.logger.info("Failed login attempt: unknown user id {user_id}"
                             .format(user_id=user.user_id))
            return False
        correct_pw = self.__hash_provider.verify_password(user.password, db_user.password)

        if correct_pw:
            self.logger.info("Successful login: {user_id}".format(user_id=user.user_id))
        else:
            self.logger.info("Failed login attempt: invalid password for {user_id}"
                             .format(user_id=user.user_id))
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


class UpdateUserInteractor(Interactor):
    """Use persistence to update the details of a user"""

    def execute(self, user):
        """Use persistence to update the details of a user
        :param user: The user to be updated by id with the user's details."""
        self.persistence.update_user(user)
