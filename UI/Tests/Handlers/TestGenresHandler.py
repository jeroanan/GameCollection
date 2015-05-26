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

from Genre import Genre
from Interactors.GenreInteractors import GetGenresInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.GenresHandler import GenresHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestGenresHandler(unittest.TestCase):
    """Unit tests for the GenresHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__genres = [Genre()]
        interactor_factory = Mock(InteractorFactory)        
        interactor = Mock(GetGenresInteractor)
        interactor.execute = Mock(return_value=self.__genres)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = GenresHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
        

    def test_is_type_of_authenticated_handler(self):
        """Test that GenresHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_renders_page(self):
        """Test that calling GenresHandler.get_page causes renderer.render to be called with the correct parameters"""
        self.__target.get_page(None)
        self.__renderer.render.assert_called_with("genres.html", title="Manage Genres", genres=self.__genres)
