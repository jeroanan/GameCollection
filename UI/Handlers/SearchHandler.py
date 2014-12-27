from UI.Handlers.Handler import Handler


class SearchHandler(Handler):

    def get_page(self, search_term):
        interactor = self.interactor_factory.create("SearchInteractor")
        results = interactor.execute(search_term)
        return self.renderer.render("search.html", title="Search Results", games=list(results),
                                    search_term=search_term, query="searchterm=%s" % search_term)
