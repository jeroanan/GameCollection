from Interactors.Interactor import Interactor


class SearchInteractor(Interactor):

    def execute(self, search_term, sort_field, sort_dir):
        return self.persistence.search(search_term=search_term, sort_field=sort_field, sort_dir=sort_dir)
