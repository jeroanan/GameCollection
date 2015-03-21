from Interactors.Interactor import Interactor


class DeletePlatformInteractor(Interactor):

    def execute(self, platform):
        self.__validate(platform)
        self.persistence.delete_platform(platform)

    def __validate(self, platform_id):
        if platform_id is None:
            raise TypeError("platform")
