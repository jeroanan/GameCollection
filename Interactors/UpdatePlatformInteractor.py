from Interactors.Interactor import Interactor


class UpdatePlatformInteractor(Interactor):

    def execute(self, platform):
        self.__validate(platform)
        self.persistence.update_platform(platform)

    def __validate(self, platform):
        if platform is None:
            raise TypeError("platform")
        self.validate_string_field("Platform", platform.name)