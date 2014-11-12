import unittest
from unittest.mock import Mock
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestGetPlatformsInteractor(unittest.TestCase):

    def test_execute_calls_persistence(self):
        persistence = Mock(MongoPersistence)
        target = GetPlatformsInteractor()
        target.persistence = persistence
        target.execute()
        self.assertTrue(persistence.get_platforms.called)

    def test_is_interactor(self):
        target = GetPlatformsInteractor()
        self.assertIsInstance(target, Interactor)