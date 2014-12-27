from Interactors.Interactor import Interactor


class SearchInteractor(Interactor):

    def execute(self, search_term):
        return self.persistence.search(search_term=search_term)
