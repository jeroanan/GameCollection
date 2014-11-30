from Interactors.Interactor import Interactor


class UpdatePlatformInteractor(Interactor):
    def execute(self, platform):

        if platform is None:
            raise TypeError("platform")

        if platform.name is None or platform.name.strip() == "":
            raise ValueError("Platform name must be set")

        self.persistence.update_platform(platform)