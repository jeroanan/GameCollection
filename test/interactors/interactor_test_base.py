"""Base class for interactor unit tests."""
import unittest
from mock import Mock
from persistence.abstract_persistence import AbstractPersistence

class InteractorTestBase(unittest.TestCase):
    """Base class for interactor unit tests."""

    def setUp(self):
        self.__validated_integer_field_names = []
        self.__validated_integer_field_values = []
        self.__validated_string_field_names = []
        self.__validated_string_field_values = []
        self.persistence = Mock(AbstractPersistence)

    def validate_integer_field(self, field_name, field_value):
        """Test helper to record integer field validations."""
        self.__validated_integer_field_names.append(field_name)
        self.__validated_integer_field_values.append(field_value)

    def validate_integer_field_was_called_with(self, field_name, field_value):
        """Test helper to check if integer field validation was called with specific parameters."""
        return (field_name in self.__validated_integer_field_names and
                field_value in self.__validated_integer_field_values)

    def validate_string_field(self, field_name, field_value):
        """Test helper to record string field validations."""
        self.__validated_string_field_names.append(field_name)
        self.__validated_string_field_values.append(field_value)

    def validate_string_field_was_called_with(self, field_name, field_value):
        """Test helper to check if string field validation was called with specific parameters."""
        return (field_name in self.__validated_string_field_names and
                field_value in self.__validated_string_field_values)
