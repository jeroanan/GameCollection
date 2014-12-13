from UI.Handlers.Handler import Handler


class EditGenreHandler(Handler):

    def get_page(self, genre_id):
        interactor = self.interactor_factory.create("GetGenreInteractor")
        genre = interactor.execute(genre_id)
        return self.renderer.render("editgenre.html", title="Edit Genre", genre=genre)
