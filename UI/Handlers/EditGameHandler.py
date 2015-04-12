from Game import Game
from Persistence.Exceptions.GameNotFoundException import GameNotFoundException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class EditGameHandler(AuthenticatedHandler):

    """The Edit game page
    :param args: A dictionary containing a key "gameid" whose value is the uuid of a game
    :returns: An rendered edit page. If the page isn't found or the current user can't
    access the game then a "Game Not Found" message will display.
    """
    def get_page(self, args):
        super().get_page(args)
        game_found = True
        game = Game()
        try:
            game = self.__get_game(args.get("gameid", ""))
            page_title = self.__get_page_title(game)
        except GameNotFoundException:
            game_found = False
            page_title = "Game Not Found"

        platforms = self.__get_platforms()

        return self.renderer.render("editgame.html",
                                    game=game, title=page_title, platforms=platforms, game_found=game_found)

    def __get_game(self, game_id):
        get_game_interactor = self.interactor_factory.create("GetGameInteractor")
        return get_game_interactor.execute(game_id=game_id, user_id=self.session.get_value("user_id"))

    def __get_platforms(self):
        platform_interactor = self.interactor_factory.create("GetPlatformsInteractor")
        return platform_interactor.execute()

    def __get_page_title(self, game):
        return "{title} ({platform})".format(title=game.title, platform=game.platform)
