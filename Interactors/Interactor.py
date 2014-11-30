class Interactor(object):

    def __init__(self):
        self.__persistence = None

    @property
    def persistence(self):
        return self.__persistence

    @persistence.setter
    def persistence(self, value):
        self.__persistence = value

    def validate_string_field(self, field_name, field_value):
        if field_value is None or field_value.strip() == "":
            raise ValueError("%s must have a value" % field_name)

    def validate_integer_field(self, field_name, field_value):
        if not str(field_value).isdigit():
            raise ValueError("%s must be a number" % field_name)