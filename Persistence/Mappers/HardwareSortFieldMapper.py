from Persistence.Exceptions.UnrecognisedFieldNameException import UnrecognisedFieldNameException


class HardwareSortFieldMapper(object):
    def __init__(self):
        self.__fields = {
            "name": "_Hardware__name",
            "platform": "_Hardware__platform",
            "numowned": "_Hardware__numowned"
        }

    def map(self, field_name):
        if field_name in self.__fields:
            return self.__fields[field_name]
        raise UnrecognisedFieldNameException("%s is not a recognised field name" % field_name)
