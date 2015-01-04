import unittest
from mock import Mock
from AbstractPersistence import AbstractPersistence
from Game import Game
from Hardware import Hardware
from Platform import Platform


class InteractorTestBase(unittest.TestCase):

    def setUp(self):
        self.__validated_integer_field_names = []
        self.__validated_integer_field_values = []
        self.__validated_string_field_names = []
        self.__validated_string_field_values = []
        self.persistence = Mock(AbstractPersistence)

    def validate_integer_field(self, field_name, field_value):
        self.__validated_integer_field_names.append(field_name)
        self.__validated_integer_field_values.append(field_value)

    def validate_integer_field_was_called_with(self, field_name, field_value):
        return (field_name in self.__validated_integer_field_names and
                field_value in self.__validated_integer_field_values)

    def validate_string_field(self, field_name, field_value):
        self.__validated_string_field_names.append(field_name)
        self.__validated_string_field_values.append(field_value)

    def validate_string_field_was_called_with(self, field_name, field_value):
        return (field_name in self.__validated_string_field_names and
                field_value in self.__validated_string_field_values)

    def get_game(self, game_id="", title="title", platform="platform", num_copies=0, num_boxed=0, num_manuals=0,
                 notes=""):
        game = Game()
        game.id = game_id
        game.title = title
        game.platform = platform
        game.num_copies = num_copies
        game.num_boxed = num_boxed
        game.num_manuals = num_manuals
        game.notes = notes
        return game

    def get_platform(self, platform_id="", name=""):
        platform = Platform()
        platform.id = platform_id
        platform.name = name
        return platform

    def get_hardware(self, hardware_id="", name="name", platform="platform", num_owned=0, num_boxed=0):
        hardware = Hardware()
        hardware.id = hardware_id
        hardware.name = name
        hardware.platform = platform
        hardware.num_owned = num_owned
        hardware.num_boxed = num_boxed
        return hardware