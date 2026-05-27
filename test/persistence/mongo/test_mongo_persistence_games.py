from logging import Logger
import unittest
from unittest.mock import MagicMock, Mock

from pymongo import MongoClient

from data.config import Config
from interactors.params.get_games_interactor_params import GetGamesInteractorParams
from persistence.exceptions import GameNotFoundException
from persistence.mongo_persistence import MongoPersistence

from test.persistence.mongo.mongo_test_base import MongoTestBase

class TestMongoPersistenceGames(MongoTestBase):

    def setUp(self) -> None:
        super().setUp()

    def test_game_from_mongo_result_performs_mapping(self) -> None:
        """Test that mapping a Game object from a MonoDB result is correct"""

        gd = {
            "_id": "id",
            "_Game__genre": "genre",
            "_Game__title": "title",
            "_Game__platform": "platform",
            "_Game__num_copies": 1,
            "_Game__num_boxed": 2,
            "_Game__num_manuals": 3,
            "_Game__notes": "notes",
            "_Game__date_purchased": "2015-05-23",
            "_Game__approximate_date_purchased": True
        }

        g = self.mongo_persistence.game_from_mongo_result(gd)

        expected_mappings = {
            "_id": g.id,
            "_Game__title": g.title,
            "_Game__genre": g.genre,
            "_Game__platform": g.platform,
            "_Game__num_copies": g.num_copies,
            "_Game__num_boxed": g.num_boxed,
            "_Game__num_manuals": g.num_manuals,
            "_Game__notes": g.notes,
            "_Game__date_purchased": g.date_purchased,
            "_Game__approximate_date_purchased": g.approximate_date_purchased
        }

        for k,v in expected_mappings.items():
            self.assertEqual(gd[k], v)

    def test_add_game_makes_call(self) -> None:
        """Tests that add_game makes a call to the database."""
        game = MagicMock()
        self.mongo_persistence.add_game(game, "user_id")
        self.assertTrue(self.mongo_client.GamesCollection.games.insert_one.called)

    def test_get_all_games_makes_call(self) -> None:
        """Tests that get_all_games makes a call to the database."""
        interactor_params = GetGamesInteractorParams(user_id="test-user")
        game_json = [
            { "_id": "a", "_Game__title": "title" },
            { "_id": "b", "_Game__title": "title 2" }
        ]
        cursor = MagicMock()

        self.mongo_client.GamesCollection.games.find = MagicMock(return_value=cursor)
        cursor.sort.return_value = cursor
        cursor.limit.return_value = game_json
        self.mongo_persistence.get_all_games(interactor_params)
        self.assertTrue(self.mongo_client.GamesCollection.games.find.called_once_with(
            {"user_id": interactor_params.user_id})
        )
    
    def test_get_all_games_for_platform_makes_call(self) -> None:
        """Tests that get_all_games_for_platform makes a call to the database."""
        interactor_params = GetGamesInteractorParams(user_id="test-user", platform="test-platform")
        game_json = [
            { "_id": "a", "_Game__title": "title" },
            { "_id": "b", "_Game__title": "title 2" }
        ]
        cursor = MagicMock()

        self.mongo_client.GamesCollection.games.find = MagicMock(return_value=cursor)
        cursor.sort.return_value = cursor
        cursor.limit.return_value = game_json
        self.mongo_persistence.get_all_games_for_platform(interactor_params)
        self.assertTrue(self.mongo_client.GamesCollection.games.find.called_once_with(
            {"user_id": interactor_params.user_id, "platform": interactor_params.platform})
        )

    def test_count_games_makes_call(self) -> None:
        """Tests that count_games makes a call to the database."""
        interactor_params = GetGamesInteractorParams(user_id="test-user")
        self.mongo_persistence.count_games(user_id=interactor_params.user_id)
        self.assertTrue(self.mongo_client.GamesCollection.games.count_documents.called_once_with(
            {"user_id": interactor_params.user_id})
        )

    def test_get_game_makes_call(self) -> None:
        """Tests that get_game makes a call to the database."""
        cursor = MagicMock()
        self.mongo_client.GamesCollection.games.find_one = MagicMock(return_value=cursor)
        self.mongo_persistence.get_game("666f6f2d6261722d71757578", "user-id")
        self.assertTrue(self.mongo_client.GamesCollection.games.find_one.called_once_with(
            {"_id": "666f6f2d6261722d71757578", "user_id": "user-id"})
        )

    def test_get_game_no_games_returned_raises_game_not_found_exception(self) -> None:
        """Tests that get_game raises a GameNotFoundException if no games are returned."""
        self.mongo_client.GamesCollection.games.find_one = MagicMock(return_value=None)
        with self.assertRaises(GameNotFoundException):
            self.mongo_persistence.get_game("666f6f2d6261722d71757578", "user-id")

    def test_get_game_invalid_id_raises_game_not_found_exception(self) -> None:
        """Tests that get_game raises a GameNotFoundException if an invalid ID is provided."""
        cursor = MagicMock()
        self.mongo_client.GamesCollection.games.find_one = MagicMock(return_value=cursor)
        with self.assertRaises(GameNotFoundException):
            self.mongo_persistence.get_game("invalid-id", "user-id")

    def test_update_game_makes_call(self) -> None:
        """Tests that update_game makes a call to the database."""
        game = Mock()
        game.id = "666f6f2d6261722d71757578"
        self.mongo_client.GamesCollection.games.update_one = MagicMock()
        self.mongo_persistence.update_game(game, "user_id")
        self.assertTrue(self.mongo_client.GamesCollection.games.update_one.called)

    def test_delete_game_makes_call(self) -> None:
        """Tests that delete_game makes a call to the database."""
        game = MagicMock()
        game.id = "666f6f2d6261722d71757578"
        self.mongo_client.GamesCollection.games.delete_one = MagicMock()
        self.mongo_persistence.delete_game(game, "user_id")
        self.assertTrue(self.mongo_client.GamesCollection.games.delete_one.called)
