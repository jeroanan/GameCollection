from Interactors.Game.AddGameInteractor import AddGameInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestAddGameInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = AddGameInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(self.get_game())
        self.assertTrue(self.persistence.add_game.called)

    def test_execute_with_null_game_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_num_boxed_field(self):
        self.__target.execute(self.get_game(num_boxed=1))
        self.validate_integer_field_was_called_with("Number of boxed items", 1)

    def test_execute_validates_num_copies_field(self):
        self.__target.execute(self.get_game(num_copies=1))
        self.validate_integer_field_was_called_with("Number of copies", 1)

    def test_execute_validates_num_manuals_field(self):
        self.__target.execute(self.get_game(num_manuals=1))
        self.validate_integer_field_was_called_with("Number of manuals", 1)

    def test_execute_with_game_id_raises_value_error(self):
        game = self.get_game(game_id="id")
        self.assertRaises(ValueError, self.__target.execute, game)

    def test_execute_validates_platform_field(self):
        self.__target.execute(self.get_game(platform="platform"))
        self.assertTrue(self.validate_string_field_was_called_with("Platform", "platform"))

    def test_execute_validates_game_title_field(self):
        self.__target.execute(self.get_game(title="title"))
        self.assertTrue(self.validate_string_field_was_called_with("Game title", "title"))
