from UI.Handlers.Handler import Handler


class SearchHandler(Handler):

    def get_page(self, params):
        sort_field = self.set_if_null(params.get("gamesort", "title"), "title")
        sort_dir = self.set_if_null(params.get("gamesortdir", "asc"), "asc")
        search_term = params.get("searchterm", "")

        interactor = self.interactor_factory.create("SearchInteractor")
        results = interactor.execute(search_term=search_term, sort_field=sort_field,
                                     sort_dir=sort_dir)

        return self.renderer.render(template="search.html", title="Search Results", games=list(results),
                                    search_term=search_term, game_sort_field=sort_field,
                                    game_sort_direction=sort_dir, query="searchterm=%s" % search_term)
