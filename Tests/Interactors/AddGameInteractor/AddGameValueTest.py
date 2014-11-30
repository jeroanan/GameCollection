import unittest
from unittest.mock import Mock
from Game import Game
from Interactors.AddGameInteractor import AddGameInteractor
from Persistence.MongoPersistence import MongoPersistence


class AddGameValueTest(unittest.TestCase):

    def setUp(self):
        self.__validated_integer_field_names = []
        self.__validated_integer_field_values = []

        self.persistence = Mock(MongoPersistence)
        self.target = AddGameInteractor()
        self.target.persistence = self.persistence
        self.target.validate_integer_field = self.validate_integer_field

    def validate_integer_field(self, field_name, field_value):
        self.__validated_integer_field_names.append(field_name)
        self.__validated_integer_field_values.append(field_value)

    def validate_integer_field_was_called_with(self, field_name, field_value):
        return (field_name in self.__validated_integer_field_names and
                field_value in self.__validated_integer_field_values)

    def get_game(self, game_id="", title="title", platform="platform", num_copies=0, num_boxed=0, num_manuals=0):
        game = Game()
        game.id = game_id
        game.title = title
        game.platform = platform
        game.num_copies = num_copies
        game.num_boxed = num_boxed
        game.num_manuals = num_manuals
        return game