"""Unit tests for Interactor class."""
import unittest
from interactors.interactor import Interactor


class TestInteractor(unittest.TestCase):
    """Unit tests for Interactor class."""

    def setUp(self):
        self.__target = Interactor()

    def test_validate_integer_field_with_none_raises_value_error(self):
        """Tests that validate_integer_field raises a ValueError when the field value is None."""
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", None)

    def test_validate_integer_field_with_string_raises_value_error(self):
        """Tests that validate_integer_field raises a ValueError when the field value is a 
        string."""
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", "wrong")

    def test_validate_integer_field_with_negative_value_raises_value_error(self):
        """Tests that validate_integer_field raises a ValueError when the field value is 
        negative."""
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", -1)

    def test_validate_integer_field_with_floating_point_value_raises_value_error(self):
        """Tests that validate_integer_field raises a ValueError when the field value is a 
        floating-point number."""
        self.assertRaises(ValueError, self.__target.validate_integer_field, "field_name", 3.141)

    def test_validate_string_field_with_none_raises_value_error(self):
        """Tests that validate_string_field raises a ValueError when the field value is None."""
        self.assertRaises(ValueError, self.__target.validate_string_field, "field_name", None)

    def test_validate_string_field_with_empty_value_raises_value_error(self):
        """Tests that validate_string_field raises a ValueError when the field value is an empty 
        string."""
        self.assertRaises(ValueError, self.__target.validate_string_field, "field_name", "")

    def test_execute_with_whitespace_platform_raises_value_error(self):
        """Tests that validate_string_field raises a ValueError when the field value is a string
        containing only whitespace."""
        self.assertRaises(ValueError, self.__target.validate_string_field, "field_name", " ")
