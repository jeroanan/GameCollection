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

from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.GameInteractors import AddGameInteractor
from Interactors.Game.CountGamesInteractor import CountGamesInteractor
from Interactors.Game.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Game.GetGameInteractor import GetGameInteractor
from Interactors.Game.GetGamesInteractor import GetGamesInteractor
from Interactors.Game.UpdateGameInteractor import UpdateGameInteractor
from Interactors.GenreInteractors import (AddGenreInteractor, DeleteGenreInteractor, GetGenresInteractor, 
                                          GetGenreInteractor, UpdateGenreInteractor)
from Interactors.Hardware.CountHardwareInteractor import CountHardwareInteractor
from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.Hardware.GetHardwareDetailsInteractor import GetHardwareDetailsInteractor
from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.Hardware.UpdateHardwareInteractor import UpdateHardwareInteractor
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Interactors.Platform.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Platform.GetPlatformInteractor import GetPlatformInteractor
from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.Platform.UpdatePlatformInteractor import UpdatePlatformInteractor
from Interactors.Search.SearchInteractor import SearchInteractor
from Interactors.User.AddUserInteractor import AddUserInteractor
from Interactors.User.ChangePasswordInteractor import ChangePasswordInteractor
from Interactors.User.DeleteUserInteractor import DeleteUserInteractor
from Interactors.User.GetUserInteractor import GetUserInteractor
from Interactors.User.GetUsersInteractor import GetUsersInteractor
from Interactors.User.LoginInteractor import LoginInteractor
from Interactors.User.UpdateUserInteractor import UpdateUserInteractor
from Persistence.MongoPersistence import MongoPersistence


class TestInteractorFactory(unittest.TestCase):
    """Unit tests for the InteractorFactory class"""

    def setUp(self):
        """setUp function for all unit tests in this class."""
        self.__target = InteractorFactory(Mock(MongoPersistence), Mock(Logger))

    def test_create_unrecognised_type_string_throws_exception(self):
        """Test that calling InteractorFactory.create with an unknown Interactor type raises an 
         UnrecognisedInteractorTypeException""" 
        self.assertRaises(UnrecognisedInteractorTypeException, self.__target.create, "InteractorType")

    def test_create(self):
        """Test that all known types of Interactor can be created with InteractorFactory"""
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
                    "ChangePasswordInteractor": ChangePasswordInteractor,
                    "GetUsersInteractor": GetUsersInteractor,
                    "UpdateUserInteractor": UpdateUserInteractor,
                    "DeleteUserInteractor": DeleteUserInteractor
                    }

        assert_mapping = lambda m: self.assertIsInstance(self.__target.create(m), mappings[m], m)
        list(map(assert_mapping, mappings))

