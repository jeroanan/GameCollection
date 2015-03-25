from Cryptography.HashProvider import HashProvider
from Interactors.Interactor import Interactor


class LoginInteractor(Interactor):

    def __init__(self):
        super().__init__()
        self.hash_provider = HashProvider()

    def execute(self, user):
        self.__validate(user)
        hashed_pw = self.hash_provider.hash_text(user.password)
        db_user = self.persistence.get_user(user)
        correct_pw = self.hash_provider.verify_password(hashed_pw, db_user.password)
        return correct_pw

    def __validate(self, user):
        if user is None:
            raise TypeError
        self.validate_string_field("user_ud", user.user_id)
        self.validate_string_field("password", user.password)

    def set_hash_provider(self, param):
        if not isinstance(param, HashProvider):
            raise ValueError
        self.hash_provider = param
