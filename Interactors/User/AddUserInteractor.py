from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.Interactor import Interactor


class AddUserInteractor(Interactor):

    def __init__(self):
        self.__hash_provider = None

    def execute(self, user):
        self.__validate(user)
        self.__stop_if_user_exists(user)
        user.password = self.__hash_provider.hash_text(user.password)
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

    def set_hash_provider(self, hash_provider):
        self.__hash_provider = hash_provider
    
    def get_hash_provider(self):
        return self.__hash_provider
