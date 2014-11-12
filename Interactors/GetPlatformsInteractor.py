from Interactors.Interactor import Interactor


class GetPlatformsInteractor(Interactor):

    def execute(self):
        return self.persistence.get_platforms()
