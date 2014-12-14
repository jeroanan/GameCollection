import cherrypy
from Genre import Genre
from UI.Handlers.Handler import Handler


class UpdateGenreHandler(Handler):

    def get_page(self, id, name, description):
        interactor = self.interactor_factory.create("UpdateGenreInteractor")
        genre = self.__get_genre(id, description, name)
        interactor.execute(genre)
        raise cherrypy.HTTPRedirect("/genres")

    def __get_genre(self, id, description, name):
        genre = Genre()
        genre.id = id
        genre.name = name
        genre.description = description
        return genre
