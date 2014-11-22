from Interactors.Interactor import Interactor


class DeletePlatformInteractor(Interactor):
    def execute(self, platform):
        self.persistence.delete_platform(platform)
