from UI.Handlers.Handler import Handler


class AllGamesHandler(Handler):

    def get_page(self, sort_field, sort_direction, platform):

        sort_field = self.set_if_null(sort_field, "title")
        sort_direction = self.set_if_null(sort_direction, "asc")

        games = self.__get_games(sort_direction, sort_field, platform)

        return self.renderer.render("allgames.html", games=list(games), title="All Games", game_sort_field=sort_field,
                                    game_sort_direction=sort_direction, platform=platform)

    def __get_games(self, sort_direction, sort_field, platform):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        games = interactor.execute(sort_field=sort_field, sort_direction=sort_direction, platform=platform)
        return games