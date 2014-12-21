from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    def execute(self, sort_field, sort_direction, number_of_games=999999):
        return self.persistence.get_all_games(number_of_games=number_of_games, sort_field=sort_field,
                                              sort_order=sort_direction)
