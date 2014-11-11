from Game import Game
import uuid


class GamesGateway(object):

    def __init__(self):
        self.__games = []
        self.__games.append(self.__get_mega_man_2())
        self.__games.append(self.__get_burnout_revenge())

    def get_all_games(self):
        return self.__games

    def add_game(self, game):
        game.id = uuid.uuid4()
        self.__games.append(game)

    def __get_mega_man_2(self):
        mega_man_2 = Game()
        mega_man_2.id = uuid.uuid4()
        mega_man_2.title = "Mega Man 2"
        mega_man_2.platform = "Nes"
        mega_man_2.num_copies = 3
        mega_man_2.num_boxed = 1
        mega_man_2.num_manuals = 1
        return mega_man_2

    def __get_burnout_revenge(self):
        burnout_revenge = Game()
        burnout_revenge.id = uuid.uuid4()
        burnout_revenge.title = "Burnout Revenge"
        burnout_revenge.platform = "PS2"
        burnout_revenge.num_copies = 1
        burnout_revenge.num_boxed = 1
        burnout_revenge.num_manuals = 1
        return burnout_revenge
