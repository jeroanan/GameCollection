import unittest

from mock import Mock

from Game import Game
from Interactors.Interactor import Interactor
from Interactors.AddGameInteractor import AddGameInteractor


class TestAddGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = AddGameInteractor()

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)
