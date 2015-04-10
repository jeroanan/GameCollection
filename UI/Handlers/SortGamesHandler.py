from UI.Handlers.Handler import Handler


class SortGamesHandler(Handler):

    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        interactor = self.interactor_factory.create("GetGamesInteractor")
        sort_field = args.get("field", "title")
        sort_direction = args.get("sortdir", "")
        games = interactor.execute(sort_field, sort_direction, int(args.get("numrows", 0)))
        return self.renderer.render("games.html", games=games, game_sort_field=sort_field, game_sort_dir=sort_direction)
