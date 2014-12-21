from UI.Handlers.Handler import Handler


class AllGamesHandler(Handler):

    def get_page(self, sort_field, sort_direction):

        if sort_field is None:
            sort_field = "title"
        if sort_direction is None:
            sort_direction = "asc"

        interactor = self.interactor_factory.create("GetGamesInteractor")
        games = interactor.execute(sort_field=sort_field, sort_direction=sort_direction)

        return self.renderer.render("allgames.html", games=games, title="All Games", game_sort_field=sort_field,
                                    game_sort_direction=sort_direction)
