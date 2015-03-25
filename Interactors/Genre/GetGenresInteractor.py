from Interactors.Interactor import Interactor


class GetGenresInteractor(Interactor):

    def execute(self):
        return self.persistence.get_genres()
