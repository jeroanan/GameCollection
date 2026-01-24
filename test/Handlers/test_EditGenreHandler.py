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
from Interactors.GenreInteractors import GetGenreInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.EditGenreHandler import EditGenreHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestEditGenreHandler(unittest.TestCase):
    """Unit tests for the EditGenreHandler class"""
    
    def setUp(self):        
        """setUp function for all unit tests in this class"""
        get_params = lambda genre_id="id": {"genreid": genre_id}
        self.__get_page = lambda: self.__target.get_page(get_params())
        self.__genre = Genre.from_dict(get_params())
        interactor_factory = Mock(InteractorFactory)
        interactor = Mock(GetGenreInteractor)
        interactor.execute = Mock(return_value=self.__genre)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditGenreHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)        

    def test_is_type_of_authenticated_handler(self):
        """Test that EditGenreHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)
        
    def test_get_page_calls_renderer(self):
        """Test that calling EditGenreHandler.get_page causes renderer.render to be called wiht the correct data."""
        self.__get_page()
        self.__renderer.render.assert_called_with("editgenre.html", genre=self.__genre, title="Edit Genre")

