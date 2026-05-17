"""
This module contains the SortFieldMapper class, which is responsible for mapping user-friendly 
field names to their corresponding internal representations in the Game class.
"""
from Persistence.exceptions import UnrecognisedFieldNameException


class SortFieldMapper(object):
    """The SortFieldMapper class provides a mapping from user-friendly field names to the internal 
    field names used in the Game class."""

    def __init__(self):
        self.__mappings = {
            "title": "_Game__title",
            "platform": "_Game__platform",
            "numcopies": "_Game__num_copies"
        }

    def map(self, field_name):
        """Maps a user-friendly field name to the internal field name used in the Game class."""
        if field_name in self.__mappings:
            return self.__mappings[field_name]
        raise UnrecognisedFieldNameException(f"{field_name} is not a recognised field")