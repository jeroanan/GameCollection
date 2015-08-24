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
import Interactors.CollectionInteractors as ci
import Interactors.InteractorFactory as factory
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.GetExportHandler as geh
import UI.Handlers.Session.Session as sess


class TestGetExportHandler(unittest.TestCase):
    
    def setUp(self):
        def get_games_data():
            games_data = [{'title': 'title1',
                          'platform': 'platform1'},
                          {'title': 'title2',
                           'platform': 'platform2'}]
            return [g.Game.from_dict(d) for d in games_data]

        def get_hardware_data():
            hardware_data = [{'name': 'hardware1',
                              'platform': 'platform1'},
                             {'name': 'hardware2',
                              'platform': 'platform2'}]
            return [h.Hardware.from_dict(d) for d in hardware_data]

        self.__interactor = Mock(ci.ExportCollectionInteractor)
        self.__interactor.execute = Mock(return_value={'games': get_games_data(),
                                                       'hardware': get_hardware_data()})

        self.__games_data = get_games_data()
        self.__hardware_data = get_hardware_data()
        
        self.__user_id = "user"

        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)

        self.__target = geh.GetExportHandler(interactor_factory, None)

        self.__session = Mock(sess.Session)
        self.__session.get_value = Mock(return_value=self.__user_id)

        self.__target.session = self.__session

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page(self):
        self.__target.get_page({ 'data[]': ['spam', 'eggs']})

    def test_get_page_executes_collection_interactor(self):
        collection_data = ['spam', 'eggs']
        self.__target.get_page({ 'data[]': collection_data})
        self.__interactor.execute.assert_called_with(collection_data, self.__user_id)

