from Interactors.Interactor import Interactor


class GetPlatformsInteractor(Interactor):

    def execute(self):
        platforms = self.persistence.get_platforms()
        if platforms is None:
            platforms = []
        return platforms
