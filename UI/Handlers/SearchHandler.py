from Interactors.Search.Params.SearchInteractorParams import SearchInteractorParams
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class SearchHandler(AuthenticatedHandler):

    """The Search Page.
    param params: A dictionary consisting of the following keys:
                  + gamesort: The field to sort search results on.
                  + gamesortdir: The direction to sort search results in.
                  + searchterm: The term given to search on.
    returns: A rendered search results page.
    """
    def get_page(self, params):
        super().get_page(params)
                
        interactor = self.interactor_factory.create("SearchInteractor")
        p = self.__get_interactor_params(params)
        results = interactor.execute(p)

        return self.renderer.render(template="search.html", title="Search Results", games=list(results),
                                    search_term=p.search_term, game_sort_field=p.sort_field,
                                    game_sort_direction=p.sort_direction, query="searchterm=%s" % p.search_term)        

    def __get_interactor_params(self, params):
        p = SearchInteractorParams()
        p.sort_field = self.set_if_null(params.get("gamesort", "title"), "title")
        p.sort_direction = self.set_if_null(params.get("gamesortdir", "asc"), "asc")
        p.search_term = params.get("searchterm", "")
        p.user_id = self.session.get_value("user_id")
        return p
        
        
