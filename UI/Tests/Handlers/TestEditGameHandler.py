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

import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.GameInteractors import GetGameInteractor
from Interactors.PlatformInteractors import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.TemplateRenderer import TemplateRenderer


class TestEditGameHandler(unittest.TestCase):
    """Unit tests for the EditGameHandler class"""

    def setUp(self):        
        """setUp function for all unit tests in this class"""
        
        def init_get_game_interactor():
            i = Mock(GetGameInteractor)
            i.execute = Mock(return_value=self.__game)
            return i

        def init_get_platforms_interactor():
            i = Mock(GetPlatformsInteractor)
            i.execute = Mock(return_value=self.__platforms)
            return i

        def init_interactor_factory():
            get_interactor = lambda: [get_game_interactor, get_platforms_interactor]
            factory = Mock(InteractorFactory)
            factory.create = Mock(side_effect=get_interactor())
            return factory

        def get_target():
            target = EditGameHandler(interactor_factory, self.__renderer)
            target.session = Mock(Session)
            target.session.get_value = Mock(return_value="1234")
            return target
            
        self.__game = Game.from_dict({"title": "Game", "platform": "Platform"})
        self.__platforms = [Platform]
        self.__renderer = Mock(TemplateRenderer)
        get_game_interactor = init_get_game_interactor()
        get_platforms_interactor = init_get_platforms_interactor()
        interactor_factory = init_interactor_factory()
        self.__target = get_target()
        self.__get_page = lambda: self.__target.get_page({"gameid": "game_id"})


    def test_is_instance_of_authenticated_handler(self):
        """Test that EditGameHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_renderer(self):
        """Test that calling EditGameHandler.get_page causes renderer.render to be called correctly"""

        def make_page_title():
            g = self.__game
            return "{title} ({platform})".format(title=g.title, platform=g.platform)        

        self.__get_page()
        self.__renderer.render.assert_called_with("editgame.html", game=self.__game, title=make_page_title(), 
                                                  platforms=self.__platforms, game_found=True)    


