from UI.Handlers.Handler import Handler


class AllGamesHandler(Handler):

    def get_page(self, sort_field, sort_direction, platform):

        if sort_field is None:
            sort_field = "title"
        if sort_direction is None:
            sort_direction = "asc"

        games = self.__get_games(sort_direction, sort_field, platform)
        number_of_games = self.__count_games()

        return self.renderer.render("allgames.html", games=list(games), title="All Games", game_sort_field=sort_field,
                                    game_sort_direction=sort_direction, number_of_games=number_of_games,
                                    platform=platform)

    def __get_games(self, sort_direction, sort_field, platform):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        games = interactor.execute(sort_field=sort_field, sort_direction=sort_direction, platform=platform)
        return games

    def __count_games(self):
        interactor = self.interactor_factory.create("CountGamesInteractor")
        number_of_games = interactor.execute()
        return number_of_games
