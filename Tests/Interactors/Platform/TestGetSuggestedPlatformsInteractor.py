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

from unittest.mock import Mock

from AbstractPersistence import AbstractPersistence
from Data.LoadSuggestedPlatforms import LoadSuggestedPlatforms
from Interactors.PlatformInteractors import GetSuggestedPlatformsInteractor
from Interactors.Interactor import Interactor
from Platform import Platform
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetSuggestedPlatformsInteractor(InteractorTestBase):
    """Unit tests for the platformshandler class""" 
    def setUp(self):
        super().setUp()
        self.__suggested_platforms = Mock(LoadSuggestedPlatforms)
        self.__suggested_platforms.get = self.__get_suggested_platforms
        self.__target = GetSuggestedPlatformsInteractor(suggested_platforms=self.__suggested_platforms)
        self.persistence.get_platforms = Mock(return_value=[])
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        """Test that GetSuggestedPlatformsInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_get_platforms(self):
        """Test that calling GetSuggestedPlatformsInteractor.execute causes persistence.get_platforms to be called"""
        self.__target.execute()
        self.assertTrue(self.persistence.get_platforms.called)

    def test_execute_returns_suggested_platforms_not_already_stored(self):
        """Test that calling GetSuggestedPlatformsInteractor.execute only returns platforms not already stored in persistence"""
        persistence = Mock(AbstractPersistence)
        persistence.get_platforms = self.__get_stored_platforms
        target = GetSuggestedPlatformsInteractor(self.__suggested_platforms)
        target.persistence = persistence
        result = target.execute()
        self.assertEqual(1, len(result))

    def test_execute_sorts_platforms_by_name(self):
        """Test that GetSuggestedPlatformsInteractor.execute sorts the results by platform.name"""
        result = self.__target.execute()
        self.assertEqual("1", result[0].name)
        self.assertEqual("2", result[1].name)

    def __get_suggested_platforms(self):
        return [Platform.from_dict({"name": "1"}), Platform.from_dict({"name": "2"})]

    def __get_stored_platforms(self):
        return [Platform.from_dict({"name": "1"})]

