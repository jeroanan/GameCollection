from unittest.mock import Mock
from AbstractPersistence import AbstractPersistence
from Interactors.Exceptions.PersistenceException import PersistenceException
from Interactors.Interactor import Interactor
from Interactors.Game.UpdateGameInteractor import UpdateGameInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestUpdateGameInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = UpdateGameInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field
        self.__target.validate_integer_field = self.validate_integer_field
        self.__game = self.get_game(title="title", platform="platform", num_copies=1, num_boxed=2, num_manuals=3,
                                    notes="")

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_calls_persistence_method(self):
        self.__target.execute(self.__game)
        self.assertTrue(self.persistence.update_game.called)

    def test_with_null_game_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_validates_title_field(self):
        self.__assert_string_validation("Game title", self.__game.title)

    def test_validates_platform_field(self):
        self.__assert_string_validation("Game platform", self.__game.platform)

    def __assert_string_validation(self, field_name, field_value):
        self.__target.execute(self.__game)
        self.validate_string_field_was_called_with(field_name, field_value)

    def test_validates_num_copies_field(self):
        self.__assert_integer_validation("Number of copies", self.__game.num_copies)

    def test_validates_num_boxed_field(self):
        self.__assert_integer_validation("Number of boxed copies", self.__game.num_boxed)

    def test_validates_num_manuals_field(self):
        self.__assert_integer_validation("Number of manuals", self.__game.num_manuals)

    def __assert_integer_validation(self, field_name, field_value):
        self.__target.execute(self.__game)
        self.validate_integer_field_was_called_with(field_name, field_value)

    def test_raises_persistence_exception_when_database_throws(self):
        def update_game(g):
            raise Exception

        self.__target.persistence = None
        p = Mock(AbstractPersistence)
        p.update_game = Mock(side_effect=update_game)
        self.__target.persistence = p
        self.assertRaises(PersistenceException, self.__target.execute, self.__game)

    
