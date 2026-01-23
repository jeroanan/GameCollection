import unittest
from Interactors.Interactor import Interactor


class TestInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = Interactor()

    def test_validate_integer_field_with_none_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", None)

    def test_validate_integer_field_with_string_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", "wrong")

    def test_execute_with_negative_num_copies_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", -1)

    def test_execute_with_floating_point_num_copies_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", 3.141)

    def test_execute_with_none_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_string_field, "field_name", None)

    def test_execute_with_empty_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_string_field, "field_name", "")

    def test_execute_with_whitespace_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.validate_string_field, "field_name", " ")