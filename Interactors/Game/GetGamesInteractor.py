from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    def execute(self, params):
        if params.platform == "" or params.platform is None:
            return self.persistence.get_all_games(number_of_games=params.number_of_games, sort_field=params.sort_field,
                                                  sort_order=params.sort_direction)

        return self.persistence.get_all_games_for_platform(platform=params.platform, 
                                                           number_of_games=params.number_of_games, 
                                                           sort_field=params.sort_field, 
                                                           sort_order=params.sort_direction)

