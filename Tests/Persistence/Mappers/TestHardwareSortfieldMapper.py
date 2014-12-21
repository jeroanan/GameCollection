import unittest
from Persistence.Exceptions.UnrecognisedFieldNameException import UnrecognisedFieldNameException
from Persistence.Mappers.HardwareSortFieldMapper import HardwareSortFieldMapper


class TestHardwareSortFieldMapper(unittest.TestCase):

    def setUp(self):
        self.__target = HardwareSortFieldMapper()

    def test_map_unknown_field_raises_unrecognised_fieldname_exception(self):
        self.assertRaises(UnrecognisedFieldNameException, self.__target.map, "bananas")

    def test_map_hardware_name_is_correct(self):
        self.assertEqual("_Hardware__name", self.__target.map("name"))

    def test_map_hardware_platform_is_correct(self):
        self.assertEqual("_Hardware__platform", self.__target.map("platform"))

    def test_map_numowned_is_correct(self):
        self.assertEqual("_Hardware__numowned", self.__target.map("numowned"))