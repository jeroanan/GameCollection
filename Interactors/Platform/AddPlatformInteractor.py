from Interactors.Interactor import Interactor


class AddPlatformInteractor(Interactor):

    def execute(self, platform):
        self.__validate(platform)
        self.persistence.add_platform(platform)

    def __validate(self, platform):
        if platform is None:
            raise TypeError("platform")
        if len(platform.id) > 0:
            raise ValueError("Id must be blank when adding a new platform")
        self.validate_string_field("Platform name", platform.name)
