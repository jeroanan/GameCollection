from Interactors.Interactor import Interactor


class DeletePlatformInteractor(Interactor):

    def execute(self, platform):
        self.__validate(platform)
        self.persistence.delete_platform(platform)

    def __validate(self, platform):
        if platform is None:
            raise TypeError("platform")
        if platform.id is None or platform.id.strip() == "":
            raise ValueError("Platform id must be supplied")
