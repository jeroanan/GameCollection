"""SortFieldMapper unit tests."""
import unittest

from Persistence.exceptions import UnrecognisedFieldNameException
from Persistence.mappers.SortFieldMapper import SortFieldMapper


class TestSortFieldMapper(unittest.TestCase):
    """SortFieldMapper unit tests."""

    def setUp(self):
        self.__target = SortFieldMapper()

    def test_map_with_unknown_field_name_raises_unknown_field_exception(self):
        """Tests that an unrecognised field name raises an UnrecognisedFieldNameException."""
        self.assertRaises(UnrecognisedFieldNameException, self.__target.map, "bananas")

    def test_map_title_returns_mapped_field_name(self):
        """Tests that the title field is mapped correctly."""
        self.assertEqual("_Game__title", self.__target.map("title"))

    def test_map_platform_returns_mapped_field_name(self):
        """Tests that the platform field is mapped correctly."""
        self.assertEqual("_Game__platform", self.__target.map("platform"))

    def test_map_numcopies_returns_mapped_field_name(self):
        """Tests that the number of copies field is mapped correctly."""
        self.assertEqual("_Game__num_copies", self.__target.map("numcopies"))