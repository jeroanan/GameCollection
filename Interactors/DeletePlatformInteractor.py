from Interactors.Interactor import Interactor


class DeletePlatformInteractor(Interactor):

    def execute(self, platform):
        self.__validate(platform)
        self.persistence.delete_platform(platform)

    def __validate(self, platform):
        if platform is None:
            raise TypeError("platform")
        self.validate_string_field("Platform id", platform.id)
