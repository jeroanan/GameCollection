from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AllGamesHandler(AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        sort_field = self.set_if_null(params.get("gamesort", "title"), "title")
        sort_direction = self.set_if_null(params.get("gamesortdir", "asc"), "asc")
        platform = params.get("platform", "")

        p = GetGamesInteractorParams()
        p.sort_field = sort_field
        p.sort_direction = sort_direction
        p.platform = platform
        p.user_id = self.session.get_value("user_id")

        games = self.__get_games(p)

        return self.renderer.render("allgames.html", games=list(games), title="All Games", game_sort_field=sort_field,
                                    game_sort_dir=sort_direction, platform=platform,
                                    query="platform=%s" % platform)

    def __get_games(self, params):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        return interactor.execute(params)
