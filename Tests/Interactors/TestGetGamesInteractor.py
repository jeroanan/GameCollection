import unittest

from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.Interactor import Interactor


class TestGetGamesInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = GetGamesInteractor()

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)
