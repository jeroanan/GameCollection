"""Interactor for searching the games collection"""
from interactors.interactor import Interactor

class SearchInteractor(Interactor):
    """Interactor for searching the games collection"""

    def execute(self, params):
        """Search the games collection
        param params: An instance of SearchInteractorParams
        returns: the search results
        """
        return self.persistence.search(search_term=params.search_term, sort_field=params.sort_field,
                                       sort_dir=params.sort_direction, user_id=params.user_id)
