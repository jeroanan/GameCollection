from Interactors.Interactor import Interactor


class UpdateGameInteractor(Interactor):

    def execute(self, game):
        if game is None:
            raise TypeError("game")

        if game.title is None or game.title.strip() == "":
            raise ValueError("Game title must be set.")
        if game.platform is None or game.platform.strip() == "":
            raise ValueError("Game platform must be set.")
        if not str(game.num_copies).isdigit():
            raise ValueError("Number of copies must be set.")
        if not str(game.num_boxed).isdigit():
            raise ValueError("Number boxed must be set.")
        if not str(game.num_manuals).isdigit():
            raise ValueError("Number of manuals must be set.")

        self.persistence.update_game(game)