from UI.Handlers.Handler import Handler


class AllGamesHandler(Handler):

    def get_page(self, params):

        sort_field = self.set_if_null(params.get("gamesort", "title"), "title")
        sort_direction = self.set_if_null(params.get("gamesortdir", "asc"), "asc")
        platform = params.get("platform", "")

        games = self.__get_games(sort_direction, sort_field, platform)

        return self.renderer.render("allgames.html", games=list(games), title="All Games", game_sort_field=sort_field,
                                    game_sort_dir=sort_direction, platform=platform,
                                    query="platform=%s" % platform)

    def __get_games(self, sort_direction, sort_field, platform):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        return interactor.execute(sort_field=sort_field, sort_direction=sort_direction, platform=platform)