from Interactors.Interactor import Interactor


class UpdateGenreInteractor(Interactor):

    def execute(self, genre):
        self.persistence.update_genre(genre)
