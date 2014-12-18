from Interactors.Interactor import Interactor


class DeleteGenreInteractor(Interactor):

    def execute(self, genre_id):
        self.persistence.delete_genre(genre_id)
