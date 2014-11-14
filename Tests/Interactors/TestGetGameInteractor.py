import unittest
from unittest.mock import Mock
from Interactors.GetGameInteractor import GetGameInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestGetGameInteractor(unittest.TestCase):

    def test_is_instance_of_interactor(self):
        target = GetGameInteractor()
        self.assertIsInstance(target, Interactor)

    def test_execute_calls_persistence(self):
        target = GetGameInteractor()
        persistence = Mock(MongoPersistence)
        target.persistence = persistence
        target.execute(game_id="gameid")
        self.assertTrue(persistence.get_game.called)