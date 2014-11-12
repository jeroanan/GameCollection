from Interactors.Interactor import Interactor


class AddPlatformInteractor(Interactor):
    def execute(self, platform):
        self.persistence.add_platform(platform)
