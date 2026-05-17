"""Maps user-friendly field names to the corresponding private 
attribute names in the Hardware class."""
from Persistence.exceptions import UnrecognisedFieldNameException

class HardwareSortFieldMapper(object):
    """Maps user-friendly field names to the corresponding private 
    attribute names in the Hardware class."""
    def __init__(self):
        self.__fields = {
            "name": "_Hardware__name",
            "platform": "_Hardware__platform",
            "numowned": "_Hardware__num_owned"
        }

    def map(self, field_name):
        """Maps a user-friendly field name to the corresponding private attribute name."""
        if field_name in self.__fields:
            return self.__fields[field_name]
        raise UnrecognisedFieldNameException(f"{field_name} is not a recognised field name")