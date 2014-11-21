from Interactors.Interactor import Interactor


class UpdatePlatformInteractor(Interactor):
    def execute(self, platform):
        self.persistence.update_platform(platform)