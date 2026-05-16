"""HardwareSortFieldMapper unit tests."""

import unittest
from Persistence.Exceptions.exceptions import UnrecognisedFieldNameException
from Persistence.Mappers.HardwareSortFieldMapper import HardwareSortFieldMapper


class TestHardwareSortFieldMapper(unittest.TestCase):
    """HardwareSortFieldMapper unit tests."""

    def setUp(self):
        self.__target = HardwareSortFieldMapper()

    def test_map_unknown_field_raises_unrecognised_fieldname_exception(self):
        """Tests that an unrecognised field name raises an UnrecognisedFieldNameException."""
        self.assertRaises(UnrecognisedFieldNameException, self.__target.map, "bananas")

    def test_map_hardware_name_is_correct(self):
        """Tests that the hardware name field is mapped correctly."""
        self.assertEqual("_Hardware__name", self.__target.map("name"))

    def test_map_hardware_platform_is_correct(self):
        """Tests that the hardware platform field is mapped correctly."""
        self.assertEqual("_Hardware__platform", self.__target.map("platform"))

    def test_map_numowned_is_correct(self):
        """Tests that the number of owned field is mapped correctly."""
        self.assertEqual("_Hardware__num_owned", self.__target.map("numowned"))