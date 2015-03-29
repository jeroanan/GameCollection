from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.Interactor import Interactor


class AddUserInteractor(Interactor):

    def execute(self, user):
        self.__validate(user)
        self.__stop_if_user_exists(user)
        self.persistence.add_user(user)

    def __validate(self, user):
        if user is None:
            raise TypeError
        self.validate_string_field("user_id", user.user_id)
        self.validate_string_field("password", user.password)

    def __stop_if_user_exists(self, user):
        if self.__user_exists(self.persistence.get_user(user)):
            raise UserExistsException

    def __user_exists(self, user):
        return user is not None
