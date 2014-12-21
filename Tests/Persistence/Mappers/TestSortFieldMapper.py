import unittest

from Persistence.Exceptions.UnrecognisedFieldNameException import UnrecognisedFieldNameException
from Persistence.Mappers.SortFieldMapper import SortFieldMapper


class TestSortFieldMapper(unittest.TestCase):

    def test_map_with_unknown_field_name_raises_unknown_field_exception(self):
        target = SortFieldMapper()
        self.assertRaises(UnrecognisedFieldNameException, target.map, "bananas")

    def test_map_title_returns_mapped_field_name(self):
        target = SortFieldMapper()
        self.assertEqual("_Game__title", target.map("title"))

    def test_map_platform_returns_mapped_field_name(self):
        target = SortFieldMapper()
        self.assertEqual("_Game__platform", target.map("platform"))

    def test_map_numcopies_returns_mapped_field_name(self):
        target = SortFieldMapper()
        self.assertEqual("_Game__num_copies", target.map("numcopies"))