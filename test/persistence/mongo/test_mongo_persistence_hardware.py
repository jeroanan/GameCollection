from unittest.mock import MagicMock

from bson import ObjectId

from hardware import Hardware
from interactors.params.get_hardware_list_interactor_params import GetHardwareListInteractorParams
from persistence.exceptions import HardwareNotFoundException
from test.persistence.mongo.mongo_test_base import MongoTestBase

class TestMongoPersistenceHardware(MongoTestBase):

    def setUp(self) -> None:
        super().setUp()

        self.hardware_id = "666f6f2d6261722d71757578"

    def test_count_hardware_makes_call(self) -> None:
        """Tests that count_hardware makes a call to the database."""
        self.mongo_persistence.count_hardware("user_id")
        self.assertTrue(self.mongo_client.GamesCollection.hardware.count_documents.called_once_with(
            {"user_id": "user_id"})
        )

    def test_get_hardware_details_makes_call(self) -> None:
        """Tests that get_hardware_details makes a call to the database."""
        cursor = MagicMock()
        self.mongo_client.GamesCollection.hardware.find_one = MagicMock(return_value=cursor)
        self.mongo_persistence.get_hardware_details(self.hardware_id, "user_id")
        self.mongo_client.GamesCollection.hardware.find_one.assert_called_once_with(
            {"_id": ObjectId(self.hardware_id), "user_id": "user_id"})

    def test_get_hardware_details_no_hardware_returned_raises_exception(self) -> None:
        """Tests that get_hardware_details raises a HardwareNotFoundException if no hardware is returned."""
        self.mongo_client.GamesCollection.hardware.find_one = MagicMock(return_value=None)
        with self.assertRaises(HardwareNotFoundException):
            self.mongo_persistence.get_hardware_details(self.hardware_id, "user_id")

    def test_get_hardware_details_invalid_id_raises_exception(self) -> None:
        """Tests that get_hardware_details raises a HardwareNotFoundException if an invalid ID is provided."""
        cursor = MagicMock()
        self.mongo_client.GamesCollection.hardware.find_one = MagicMock(return_value=cursor)
        with self.assertRaises(HardwareNotFoundException):
            self.mongo_persistence.get_hardware_details("invalid-id", "user_id")

    def test_get_hardware_list_makes_call(self) -> None:
        """Tests that get_hardware_list makes a call to the database."""
        params = GetHardwareListInteractorParams(user_id="user_id", number_of_items=5)
        cursor = MagicMock()
        self.mongo_client.GamesCollection.hardware.find = MagicMock(return_value=cursor)
        cursor.sort.return_value = cursor
        cursor.limit.return_value = []
        self.mongo_persistence.get_hardware_list(params)
        self.mongo_client.GamesCollection.hardware.find.assert_called_once_with(
            {"user_id": params.user_id}, limit=params.number_of_items)

    def test_get_hardware_list_for_platform_makes_call(self) -> None:
        """Tests that get_hardware_list_for_platform makes a call to the database."""
        params = GetHardwareListInteractorParams(user_id="user_id", platform="platform", number_of_items=5)
        cursor = MagicMock()
        self.mongo_client.GamesCollection.hardware.find = MagicMock(return_value=cursor)
        cursor.sort.return_value = cursor
        cursor.limit.return_value = []
        self.mongo_persistence.get_hardware_list_for_platform(params)
        self.mongo_client.GamesCollection.hardware.find.assert_called_once_with(
            {"user_id": params.user_id, "_Hardware__platform": params.platform}, limit=params.number_of_items)

    def test_save_hardware_makes_call(self) -> None:
        """Tests that save_hardware makes a call to the database."""
        hardware = MagicMock()
        self.mongo_client.GamesCollection.hardware.insert_one = MagicMock()
        self.mongo_persistence.save_hardware(hardware, "user_id")
        self.assertTrue(self.mongo_client.GamesCollection.hardware.insert_one.called)

    def test_update_hardware_makes_call(self) -> None:
        """Tests that update_hardware makes a call to the database."""
        hardware = Hardware()
        hardware.id = self.hardware_id

        self.mongo_client.GamesCollection.hardware.update_one = MagicMock()
        self.mongo_persistence.update_hardware(hardware, "user_id")
        self.assertTrue(self.mongo_client.GamesCollection.hardware.update_one.called)

    def test_delete_hardware_makes_call(self) -> None:
        """Tests that delete_hardware makes a call to the database."""
        self.mongo_client.GamesCollection.hardware.delete_one = MagicMock()
        self.mongo_persistence.delete_hardware(self.hardware_id, "user_id")
        self.assertTrue(self.mongo_client.GamesCollection.hardware.delete_one.called)

    def test_hardware_from_mongo_result_performs_mapping(self) -> None:
        """Mapping mongo result to Hardware object properly initialises object."""

        hd = {
            "_id": "id",
            "_Hardware__name": "name",
            "_Hardware__platform": "platform",
            "_Hardware__num_owned": 1,
            "_Hardware__num_boxed": 2,
            "_Hardware__notes": "notes",
            "_Hardware__hardware_type": "ht"
        }

        h = self.mongo_persistence.hardware_from_mongo_result(hd)

        expected_mappings = {
            "_id": h.id,
            "_Hardware__name": h.name,
            "_Hardware__platform": h.platform,
            "_Hardware__num_owned": h.num_owned,
            "_Hardware__num_boxed": h.num_boxed,
            "_Hardware__notes": h.notes,
            "_Hardware__hardware_type": h.hardware_type
        }

        for k, v in expected_mappings.items():
            self.assertEqual(hd[k], v)

