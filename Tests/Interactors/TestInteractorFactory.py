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
import Interactors.GameInteractors as game_interactors
import Interactors.GenreInteractors as genre_interactors
import Interactors.HardwareInteractors as hardware_interactors
import Interactors.InteractorFactory as interactor_factory
import Interactors.PlatformInteractors as platform_interactors
import Interactors.Search.SearchInteractor as search_interactor
import Interactors.UserInteractors as user_interactors
import AbstractPersistence as abstract_persistence


class TestInteractorFactory(unittest.TestCase):
    """Unit tests for the InteractorFactory class"""

    def setUp(self):
        """setUp function for all unit tests in this class."""
        persistence = Mock(abstract_persistence.AbstractPersistence)
        logger = Mock(Logger)
        self.__target = interactor_factory.InteractorFactory(persistence, logger)

    def test_create_unrecognised_type_string_throws_exception(self):
        """Test that calling InteractorFactory.create with an unknown Interactor type raises an 
         UnrecognisedInteractorTypeException""" 
        self.assertRaises(UnrecognisedInteractorTypeException, self.__target.create, "InteractorType")

    def test_create(self):
        """Test that all known types of Interactor can be created with InteractorFactory"""
        mappings = {"AddGameInteractor": game_interactors.AddGameInteractor,
                    "AddGenreInteractor": genre_interactors.AddGenreInteractor,
                    "AddHardwareTypeInteractor": hardware_interactors.AddHardwareTypeInteractor,
                    "AddPlatformInteractor": platform_interactors.AddPlatformInteractor,
                    "AddUserInteractor": user_interactors.AddUserInteractor,
                    "CountGamesInteractor": game_interactors.CountGamesInteractor,
                    "CountHardwareInteractor": hardware_interactors.CountHardwareInteractor,
                    "ChangePasswordInteractor": user_interactors.ChangePasswordInteractor,
                    "DeleteGameInteractor": game_interactors.DeleteGameInteractor,
                    "DeleteGenreInteractor": genre_interactors.DeleteGenreInteractor,
                    "DeleteHardwareInteractor": hardware_interactors.DeleteHardwareInteractor,
                    "DeletePlatformInteractor": platform_interactors.DeletePlatformInteractor,
                    "DeleteUserInteractor": user_interactors.DeleteUserInteractor,
                    "GetGameInteractor": game_interactors.GetGameInteractor,
                    "GetGamesInteractor": game_interactors.GetGamesInteractor,
                    "GetGenreInteractor": genre_interactors.GetGenreInteractor,
                    "GetGenresInteractor": genre_interactors.GetGenresInteractor,
                    "GetHardwareDetailsInteractor": hardware_interactors.GetHardwareDetailsInteractor,
                    "GetHardwareListInteractor": hardware_interactors.GetHardwareListInteractor,
                    "GetHardwareTypeInteractor": hardware_interactors.GetHardwareTypeInteractor,
                    "GetHardwareTypeListInteractor": hardware_interactors.GetHardwareTypeListInteractor,
                    "GetPlatformInteractor": platform_interactors.GetPlatformInteractor,
                    "GetPlatformsInteractor": platform_interactors.GetPlatformsInteractor,
                    "GetSuggestedGenresInteractor": genre_interactors.GetSuggestedGenresInteractor,
                    "GetSuggestedHardwareTypesInteractor": hardware_interactors.GetSuggestedHardwareTypesInteractor,
                    "GetSuggestedPlatformsInteractor": platform_interactors.GetSuggestedPlatformsInteractor,
                    "GetUserInteractor": user_interactors.GetUserInteractor,
                    "GetUsersInteractor": user_interactors.GetUsersInteractor,
                    "LoginInteractor": user_interactors.LoginInteractor,
                    "SaveHardwareInteractor": hardware_interactors.SaveHardwareInteractor,
                    "SearchInteractor": search_interactor.SearchInteractor,
                    "UpdateGameInteractor": game_interactors.UpdateGameInteractor,
                    "UpdateGenreInteractor": genre_interactors.UpdateGenreInteractor,
                    "UpdateHardwareInteractor": hardware_interactors.UpdateHardwareInteractor,
                    "UpdateHardwareTypeInteractor": hardware_interactors.UpdateHardwareTypeInteractor,
                    "UpdatePlatformInteractor": platform_interactors.UpdatePlatformInteractor,
                    "UpdateUserInteractor": user_interactors.UpdateUserInteractor
                    }

        assert_mapping = lambda m: self.assertIsInstance(self.__target.create(m), mappings[m], m)
        list(map(assert_mapping, mappings))


