from Cryptography.HashProvider import HashProvider
from Interactors.Interactor import Interactor


class LoginInteractor(Interactor):

    def __init__(self):
        super().__init__()
        self.__hash_provider = HashProvider()

    def execute(self, user):
        self.__validate(user)
        hashed_pw = self.__hash_provider.hash_text(user.password)
        db_user = self.persistence.get_user(user)
        if db_user.user_id == "":
            return False
        correct_pw = self.__hash_provider.verify_password(user.password, db_user.password)
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
