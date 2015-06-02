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

from Data.Config import Config
from Game import Game
from Hardware import Hardware
from Interactors.GameInteractors import CountGamesInteractor, GetGamesInteractor
from Interactors.HardwareInteractors import CountHardwareInteractor, GetHardwareListInteractor
from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestIndexHandler(unittest.TestCase):
    """Unit tests for the IndexHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        
        def get_interactor(interactor_type):
            interactors = {GetGamesInteractor: self.__games,
                           CountGamesInteractor: 0,
                           GetHardwareListInteractor: self.__hardware,
                           CountHardwareInteractor: 2
            }
            
            if interactor_type in interactors:
                interactor = Mock(interactor_type)
                interactor.execute = Mock(return_value=interactors[interactor_type])
                return interactor
            return None

        self.__games = [Game()]
        self.__hardware = [Hardware()]
        self.__renderer = Mock(TemplateRenderer)
        get_interactors = lambda: [get_interactor(GetGamesInteractor), get_interactor(GetHardwareListInteractor), 
                                   get_interactor(CountGamesInteractor), get_interactor(CountHardwareInteractor)]
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=get_interactors())
        self.__config = Mock(Config)
        self.__config.get = Mock(return_value=0)
        self.__target = IndexHandler(interactor_factory, self.__renderer, self.__config)
        self.__target.session = Mock(Session)
        self.__get_page = lambda args: self.__target.get_page(args)

    def test_gets_config_settings(self):
        """Test that IndexHandler.get_page reads configuration settings"""
        self.__get_page(self.__get_args())
        settings = ["front-page-games",
                    "front-page-hardware"]
        
        for s in settings:
            self.__config.get.assert_any_call(s)

    def test_uses_default_sort_options_for_games(self):        
        """Test that when sort options are not given, the correct default sort options are used."""
        args = self.__get_args(game_sort=None, game_sort_direction=None, hardware_sort=None, 
                               hardware_sort_direction=None)
        self.__get_page(args)
        self.__renderer.render.assert_called_with("index.html", games=self.__games, hardware=self.__hardware,
                                                  title="Games Collection", game_sort_field="title", 
                                                  game_sort_dir="asc", hw_sort_field="name", 
                                                  number_of_games=0, hw_sort_dir="asc", number_of_hardware=2)

    def __get_args(self, game_sort="title", game_sort_direction="asc", hardware_sort="name",
                   hardware_sort_direction="asc"):
        return {
            "gamesort":  game_sort,
            "gamesortdir": game_sort_direction,
            "hardwaresort": hardware_sort,
            "hardwaresortdir": hardware_sort_direction
        }

    def test_is_type_of_authenticated_handler(self):
        """Test that IndexHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)
