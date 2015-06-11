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

import Genre as g
import Interactors.GenreInteractors as gi
import Interactors.InteractorFactory as ifactory
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.GenresHandler as gh
import UI.Handlers.Session.Session as session
import UI.TemplateRenderer as tr


class TestGenresHandler(unittest.TestCase):
    """Unit tests for the GenresHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""

        def interactor_factory_create(interactor_type):

            def create_get_genres_interactor():
                get_genres_interactor = Mock(gi.GetGenresInteractor)
                get_genres_interactor.execute = Mock(return_value=self.__genres)
                return get_genres_interactor

            def create_get_suggested_genres_interactor():
                get_genres_interactor = Mock(gi.GetSuggestedGenresInteractor)
                get_genres_interactor.execute = Mock(return_value=self.__suggested_genres)
                return get_genres_interactor

            if interactor_type == "GetGenresInteractor":
                return create_get_genres_interactor()
            elif interactor_type == "GetSuggestedGenresInteractor":
                return create_get_suggested_genres_interactor()

        self.__genres = [g.Genre.from_dict({"name": "stored genre"})]
        self.__suggested_genres = [g.Genre.from_dict({"name": "suggested genre"})]
        interactor_factory = Mock(ifactory.InteractorFactory)        
        interactor_factory.create = Mock(side_effect=interactor_factory_create)
        self.__renderer = Mock(tr.TemplateRenderer)
        self.__target = gh.GenresHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(session.Session)

    def test_is_type_of_authenticated_handler(self):
        """Test that GenresHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_renders_page(self):
        """Test that calling GenresHandler.get_page causes renderer.render to be called with the correct parameters"""
        self.__target.get_page(None)
        self.__renderer.render.assert_called_with("genres.html", title="Manage Genres", genres=self.__genres,
                                                  suggested_genres=self.__suggested_genres)
