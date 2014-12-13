from Interactors.Interactor import Interactor


class GetGenreInteractor(Interactor):

    def execute(self, game_id):
        return self.persistence.get_genre_details(game_id)
