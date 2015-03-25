from Interactors.Interactor import Interactor


class AddGenreInteractor(Interactor):

    def execute(self, genre):
        if genre is None:
            raise TypeError("genre")
        self.validate_string_field("Name", genre.name)

        return self.persistence.add_genre(genre)
