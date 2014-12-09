from unittest.mock import Mock
from Data.SuggestedPlatforms import SuggestedPlatforms
from Interactors.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetSuggestedPlatformsInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__suggested_platforms = Mock(SuggestedPlatforms)
        self.__suggested_platforms.get = self.__get_suggested_platforms
        self.__target = GetSuggestedPlatformsInteractor(suggested_platforms=self.__suggested_platforms)
        self.persistence.get_platforms = Mock(return_value=[])
        self.__target.persistence = self.persistence
        self.__get_called = False

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_get_platforms(self):
        self.__target.execute()
        self.assertTrue(self.persistence.get_platforms.called)

    def test_executeS_returns_empty_list_if_there_are_none(self):
        suggested_platforms = Mock(SuggestedPlatforms)
        suggested_platforms.get = Mock(return_value=[])
        target = GetSuggestedPlatformsInteractor(suggested_platforms)
        target.persistence = self.persistence
        result = target.execute()
        self.assertEqual(0, len(result))

    def test_execute_suggested_platforms_returns_platforms(self):
        result = self.__target.execute()
        self.assertEqual(2, len(result))

    def test_execute_returns_suggested_platforms_not_already_stored(self):
        persistence = Mock(MongoPersistence)
        persistence.get_platforms = self.__get_stored_platforms
        target = GetSuggestedPlatformsInteractor(self.__suggested_platforms)
        target.persistence = persistence
        result = target.execute()
        self.assertEqual(1, len(result))

    def __get_suggested_platforms(self):
        self.__get_called = True
        platforms = []
        p1 = Platform()
        p1.name = "1"
        p2 = Platform
        p2.name = "2"
        platforms.append(p1)
        platforms.append(p2)
        return platforms

    def __get_stored_platforms(self):
        platforms = []
        p1 = Platform()
        p1.name = "1"
        platforms.append(p1)
        return platforms