from UI.Handlers.Handler import Handler


class GetGenresHandler(Handler):

    def get_page(self):
        interactor = self.interactor_factory.create("GetGenresInteractor")
        genres = interactor.execute()
        return self.renderer.render("genres.html", title="Manage Genres", genres=genres)
