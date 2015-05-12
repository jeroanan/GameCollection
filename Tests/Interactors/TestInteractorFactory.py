# Copyright (c) 2015 David Wilson
# This file is part of Icarus.

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

from logging import Logger
import unittest
from unittest.mock import Mock

from Interactors.Genre.AddGenreInteractor import AddGenreInteractor
from Interactors.Game.CountGamesInteractor import CountGamesInteractor
from Interactors.Hardware.CountHardwareInteractor import CountHardwareInteractor
from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.Platform.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Genre.GetGenreInteractor import GetGenreInteractor
from Interactors.Genre.GetGenresInteractor import GetGenresInteractor
from Interactors.Hardware.GetHardwareDetailsInteractor import GetHardwareDetailsInteractor
from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Game.AddGameInteractor import AddGameInteractor
from Interactors.Game.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.Game.GetGameInteractor import GetGameInteractor
from Interactors.Game.GetGamesInteractor import GetGamesInteractor
from Interactors.Platform.GetPlatformInteractor import GetPlatformInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.Search.SearchInteractor import SearchInteractor
from Interactors.Game.UpdateGameInteractor import UpdateGameInteractor
from Interactors.Hardware.UpdateHardwareInteractor import UpdateHardwareInteractor
from Interactors.User.AddUserInteractor import AddUserInteractor
from Interactors.User.ChangePasswordInteractor import ChangePasswordInteractor
from Interactors.User.GetUserInteractor import GetUserInteractor
from Persistence.MongoPersistence import MongoPersistence
from Interactors.User.LoginInteractor import LoginInteractor
from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Tests.Interactors.Genre.TestDeleteGenreInteractor import DeleteGenreInteractor
from Tests.Interactors.Platform.TestGetPlatformsInteractor import GetPlatformsInteractor
from Tests.Interactors.Platform.TestUpdatePlatformInteractor import UpdatePlatformInteractor
from Interactors.Genre.UpdateGenreInteractor import UpdateGenreInteractor


class TestInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__target = InteractorFactory(Mock(MongoPersistence), Mock(Logger))

    def test_create_unrecognised_type_string_throws_exception(self):
        self.assertRaises(UnrecognisedInteractorTypeException, self.__target.create, "InteractorType")

    def test_create(self):
        mappings = {"AddGameInteractor": AddGameInteractor,
                    "GetGamesInteractor": GetGamesInteractor,
                    "GetPlatformsInteractor": GetPlatformsInteractor,
                    "AddPlatformInteractor": AddPlatformInteractor,
                    "GetGameInteractor": GetGameInteractor,
                    "UpdateGameInteractor": UpdateGameInteractor,
                    "DeleteGameInteractor": DeleteGameInteractor,
                    "GetHardwareListInteractor": GetHardwareListInteractor,
                    "SaveHardwareInteractor": SaveHardwareInteractor,
                    "GetPlatformInteractor": GetPlatformInteractor,
                    "UpdatePlatformInteractor": UpdatePlatformInteractor,
                    "DeletePlatformInteractor": DeletePlatformInteractor,
                    "GetHardwareDetailsInteractor": GetHardwareDetailsInteractor,
                    "UpdateHardwareInteractor": UpdateHardwareInteractor,
                    "DeleteHardwareInteractor": DeleteHardwareInteractor,
                    "GetHardwareDetailsInteractor": GetHardwareDetailsInteractor,
                    "UpdateHardwareInteractor": UpdateHardwareInteractor,
                    "DeleteHardwareInteractor": DeleteHardwareInteractor,
                    "GetSuggestedPlatformsInteractor": GetSuggestedPlatformsInteractor,
                    "GetGenresInteractor": GetGenresInteractor,
                    "AddGenreInteractor": AddGenreInteractor,
                    "GetGenreInteractor": GetGenreInteractor,
                    "UpdateGenreInteractor": UpdateGenreInteractor,
                    "DeleteGenreInteractor": DeleteGenreInteractor,
                    "CountGamesInteractor": CountGamesInteractor,
                    "SearchInteractor": SearchInteractor,
                    "CountHardwareInteractor": CountHardwareInteractor,
                    "LoginInteractor": LoginInteractor,
                    "AddUserInteractor": AddUserInteractor,
                    "GetUserInteractor": GetUserInteractor,
                    "ChangePasswordInteractor": ChangePasswordInteractor
                    }

        for m in mappings:
            result = self.__target.create(m)
            self.assertIsInstance(result, mappings[m], m)

