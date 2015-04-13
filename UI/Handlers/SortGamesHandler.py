from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class SortGamesHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        interactor = self.interactor_factory.create("GetGamesInteractor")
        sort_field = args.get("field", "title")
        sort_direction = args.get("sortdir", "")
        number_of_games = int(args.get("numrows", 0))

        p = GetGamesInteractorParams()
        p.sort_field = sort_field
        p.sort_direction = sort_direction
        p.number_of_games = number_of_games
        p.user_id = self.session.get_value("user_id")

        games = interactor.execute(p)
        return self.renderer.render("games.html", games=games, game_sort_field=sort_field, game_sort_dir=sort_direction)
