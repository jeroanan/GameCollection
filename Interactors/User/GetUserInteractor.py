from Interactors.Interactor import Interactor

class GetUserInteractor(Interactor):

    def execute(self, user):
        self.__validate(user)
        return self.persistence.get_user(user)

    def __validate(self, user):
        if user is None:
            raise TypeError
        self.validate_string_field("user_id", user.user_id)
