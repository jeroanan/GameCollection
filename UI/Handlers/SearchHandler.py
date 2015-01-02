from UI.Handlers.Handler import Handler


class SearchHandler(Handler):

    def get_page(self, search_term, sort_field, sort_dir):
        sort_field = self.set_if_null(sort_field, "title")
        sort_dir = self.set_if_null(sort_dir, "asc")

        interactor = self.interactor_factory.create("SearchInteractor")
        results = interactor.execute(search_term=search_term, sort_field=sort_field, sort_dir=sort_dir)
        return self.renderer.render(template="search.html", title="Search Results", games=list(results),
                                    search_term=search_term, game_sort_field=sort_field, game_sort_direction=sort_dir,
                                    query="searchterm=%s" % search_term)
