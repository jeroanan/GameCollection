import cherrypy
from UI.Handlers.Handler import Handler


class DeleteGenreHandler(Handler):
    def get_page(self, genre_id):
        interactor = self.interactor_factory.create("DeleteGenreInteractor")
        interactor.execute(genre_id)
        raise cherrypy.HTTPRedirect("/genres")
