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

import Game as g
import Genre as ge
import Interactors.GameInteractors as gi
import Interactors.GenreInteractors as gei
import Interactors.PlatformInteractors as pi
import Interactors.InteractorFactory as factory
import Platform as p
import UI.Handlers.Session.Session as sess
import UI.Handlers.EditGameHandler as egh
import UI.Handlers.AuthenticatedHandler as ah
import UI.TemplateRenderer as tr


class TestEditGameHandler(unittest.TestCase):
    """Unit tests for the EditGameHandler class"""

    def setUp(self):        
        """setUp function for all unit tests in this class"""
        def init_interactor_factory():

            def get_interactor(interactor_type):                
                interactors = {"GetGameInteractor": (gi.GetGameInteractor, self.__game),
                               "GetPlatformsInteractor": (pi.GetPlatformsInteractor, self.__platforms),
                               "GetGenresInteractor": (gei.GetGenreInteractor, self.__genres)}

                if interactor_type not in interactors: 
                    return None

                t, data = interactors[interactor_type]
                i = Mock(t)
                i.execute = Mock(return_value=data)
                return i

            f = Mock(factory.InteractorFactory)
            f.create = Mock(side_effect=get_interactor)
            return f

        def get_target():
            target = egh.EditGameHandler(interactor_factory, self.__renderer)
            target.session = Mock(sess.Session)
            target.session.get_value = Mock(return_value="1234")
            return target
            
        self.__game = g.Game.from_dict({"title": "Game", "platform": "Platform"})
        self.__platforms = [p.Platform()]
        self.__genres = [ge.Genre()]
        self.__renderer = Mock(tr.TemplateRenderer)
        interactor_factory = init_interactor_factory()
        self.__target = get_target()
        self.__get_page = lambda: self.__target.get_page({"gameid": "game_id"})


    def test_is_instance_of_authenticated_handler(self):
        """Test that EditGameHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_calls_renderer(self):
        """Test that calling EditGameHandler.get_page causes renderer.render to be called correctly"""

        def make_page_title():
            g = self.__game
            return "{title} ({platform})".format(title=g.title, platform=g.platform)        

        self.__get_page()
        self.__renderer.render.assert_called_with("editgame.html", game=self.__game, title=make_page_title(), 
                                                  platforms=self.__platforms, game_found=True, genres=self.__genres)    


