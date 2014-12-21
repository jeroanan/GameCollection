from Persistence.Exceptions.UnrecognisedFieldNameException import UnrecognisedFieldNameException


class SortFieldMapper(object):

    def __init__(self):
        self.__mappings = {
            "title": "_Game__title",
            "platform": "_Game__platform",
            "numcopies": "_Game__num_copies"
        }

    def map(self, field_name):
        if field_name in self.__mappings:
            return self.__mappings[field_name]
        raise UnrecognisedFieldNameException("%s is not a recognised field" % field_name)
