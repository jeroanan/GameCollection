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
                    "GetGamesInteractor": game_interactors.GetGamesInteractor,
                    "GetPlatformsInteractor": platform_interactors.GetPlatformsInteractor,
                    "AddPlatformInteractor": platform_interactors.AddPlatformInteractor,
                    "GetGameInteractor": game_interactors.GetGameInteractor,
                    "UpdateGameInteractor": game_interactors.UpdateGameInteractor,
                    "DeleteGameInteractor": game_interactors.DeleteGameInteractor,
                    "GetHardwareListInteractor": hardware_interactors.GetHardwareListInteractor,
                    "SaveHardwareInteractor": hardware_interactors.SaveHardwareInteractor,
                    "GetPlatformInteractor": platform_interactors.GetPlatformInteractor,
                    "UpdatePlatformInteractor": platform_interactors.UpdatePlatformInteractor,
                    "DeletePlatformInteractor": platform_interactors.DeletePlatformInteractor,
                    "GetHardwareDetailsInteractor": hardware_interactors.GetHardwareDetailsInteractor,
                    "UpdateHardwareInteractor": hardware_interactors.UpdateHardwareInteractor,
                    "DeleteHardwareInteractor": hardware_interactors.DeleteHardwareInteractor,
                    "GetHardwareDetailsInteractor": hardware_interactors.GetHardwareDetailsInteractor,
                    "UpdateHardwareInteractor": hardware_interactors.UpdateHardwareInteractor,
                    "DeleteHardwareInteractor": hardware_interactors.DeleteHardwareInteractor,
                    "GetSuggestedPlatformsInteractor": platform_interactors.GetSuggestedPlatformsInteractor,
                    "GetGenresInteractor": genre_interactors.GetGenresInteractor,
                    "AddGenreInteractor": genre_interactors.AddGenreInteractor,
                    "GetGenreInteractor": genre_interactors.GetGenreInteractor,
                    "UpdateGenreInteractor": genre_interactors.UpdateGenreInteractor,
                    "DeleteGenreInteractor": genre_interactors.DeleteGenreInteractor,
                    "CountGamesInteractor": game_interactors.CountGamesInteractor,
                    "SearchInteractor": search_interactor.SearchInteractor,
                    "CountHardwareInteractor": hardware_interactors.CountHardwareInteractor,
                    "LoginInteractor": user_interactors.LoginInteractor,
                    "AddUserInteractor": user_interactors.AddUserInteractor,
                    "GetUserInteractor": user_interactors.GetUserInteractor,
                    "ChangePasswordInteractor": user_interactors.ChangePasswordInteractor,
                    "GetUsersInteractor": user_interactors.GetUsersInteractor,
                    "UpdateUserInteractor": user_interactors.UpdateUserInteractor,
                    "DeleteUserInteractor": user_interactors.DeleteUserInteractor,
                    "GetSuggestedGenresInteractor": genre_interactors.GetSuggestedGenresInteractor
                    }

        assert_mapping = lambda m: self.assertIsInstance(self.__target.create(m), mappings[m], m)
        list(map(assert_mapping, mappings))

