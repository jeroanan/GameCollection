from Interactors.Interactor import Interactor


class GetPlatformInteractor(Interactor):
    def execute(self, platform_id):
        return self.persistence.get_platform(platform_id)
