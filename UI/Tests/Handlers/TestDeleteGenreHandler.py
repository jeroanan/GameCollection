# Copyright (c) 20115 David Wilson
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

from Genre import Genre
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Genre.DeleteGenreInteractor import DeleteGenreInteractor
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.DeleteGenreHandler import DeleteGenreHandler
from UI.Handlers.Session.Session import Session


class TestDeleteGenreHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(DeleteGenreInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteGenreHandler(interactor_factory, None)
        self.__target.session = Mock(Session)
        self.__get_params = lambda genre_id=id: {"id": genre_id}
        self.__genre = Genre.from_dict(self.__get_params())
        self.__get_page = lambda: self.__target.get_page(self.__get_params()) 

    def test_is_type_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_interactor(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(self.__genre)
