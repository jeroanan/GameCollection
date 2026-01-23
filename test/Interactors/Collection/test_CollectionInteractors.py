# Copyright (c) David Wilson 2015
# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from unittest.mock import Mock

import Game as g
import Hardware as h
import Interactors.GameInteractors as gi
import Interactors.CollectionInteractors as ci
import Interactors.HardwareInteractors as hi
import Interactors.Interactor as interactor
import Interactors.InteractorFactory as interactor_factory

class TestExportCollectionInteractor(unittest.TestCase):
    
    def setUp(self):

        def init_games():
            game_data = [{'title': 'game1',
                          'platform': 'platform1'},
                         {'title': 'game2',
                          'platform': 'platform2'}]
            return [g.Game.from_dict(d) for d in game_data]

        def init_hardware():
            hardware_data = [{'title': 'game1',
                            'platform': 'platform1'},
                            {'title': 'game2',
                             'platform': 'platform2'}]
            return [h.Hardware.from_dict(d) for d in hardware_data]

        self.__games = init_games()
        self.__hardware = init_hardware()

        self.__get_games_interactor = Mock(gi.GetGamesInteractor)
        self.__get_games_interactor.execute = Mock(return_value=self.__games)

        self.__hardware_list_interactor = Mock(hi.GetHardwareListInteractor)
        self.__hardware_list_interactor.execute = Mock(return_value=self.__hardware)

        def interactor_factory_create(interactor_type):
            interactors = {'GetGamesInteractor': self.__get_games_interactor,
                           'GetHardwareListInteractor': self.__hardware_list_interactor}

            return interactors[interactor_type]

        factory = Mock(interactor_factory.InteractorFactory)
        factory.create = Mock(side_effect=interactor_factory_create)
        self.__target = ci.ExportCollectionInteractor(factory) 

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_with_games_returns_games(self):
        expected = {'games': self.__games}
        result = self.__target.execute(['games'], 'user')
        self.assertEqual(expected, result)        

    def test_execute_with_hardware_returns_hardware(self):
        expected = {'hardware': self.__hardware}
        result = self.__target.execute(['hardware'], 'user')
        self.assertEqual(expected, result)

    def test_execute_with_games_and_hardware_returns_games_and_hardware(self):
        expected = {'games': self.__games,
                    'hardware': self.__hardware}
        result = self.__target.execute(['games', 'hardware'], 'user')
        self.assertEqual(expected, result)
