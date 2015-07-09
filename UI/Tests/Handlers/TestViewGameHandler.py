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
import Interactors.InteractorFactory as factory
import Interactors.GameInteractors as gi
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.ViewGameHandler as vgh
import UI.Handlers.Session.Session as sess
import UI.TemplateRenderer as tr


class TestViewGameHandler(unittest.TestCase):
    """Unit tests for the ViewGameHandler class"""

    def setUp(self):
        """setUp for all unit tests in this class"""
        self.__game = g.Game.from_dict({"id": "myid", "title": "my title"})
        get_game_interactor = Mock(gi.GetGameInteractor)
        get_game_interactor.execute = Mock(return_value=self.__game)
        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(return_value=get_game_interactor)
        self.__renderer = Mock(tr.TemplateRenderer)
        self.__target = vgh.ViewGameHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(sess.Session)
        self.__target.session.get_value = Mock(return_value="1234")

    def test_is_instance_of_authenticated_handler(self):
        """Test that ViewGameHandler is and instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_causes_renderer_to_be_called_correctly(self):
        """Test that calling ViewGameHandler.get_page causes TemplateRenderer.render to be called"""
        params = {"id": "myid", "title": "my title"}
        self.__target.get_page(params)
        self.__renderer.render.assert_called_with("viewgame.html", title=self.__game.title, game=self.__game)
