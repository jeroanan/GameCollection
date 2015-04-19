from Interactors.Interactor import Interactor


class SearchInteractor(Interactor):

    """Search the games collection
    param params: An instance of SearchInteractorParams
    returns: the search results
    """
    def execute(self, params):
        return self.persistence.search(search_term=params.search_term, sort_field=params.sort_field, 
                                       sort_dir=params.sort_direction, user_id=params.user_id)
