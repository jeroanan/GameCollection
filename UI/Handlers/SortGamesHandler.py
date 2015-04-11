from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class SortGamesHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        interactor = self.interactor_factory.create("GetGamesInteractor")
        sort_field = args.get("field", "title")
        sort_direction = args.get("sortdir", "")
        games = interactor.execute(sort_field, sort_direction, int(args.get("numrows", 0)))
        return self.renderer.render("games.html", games=games, game_sort_field=sort_field, game_sort_dir=sort_direction)
