# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

class Interactor(object):
    """A base class for interactor objects."""

    def __init__(self):
        self.__persistence = None
        self.__interactor_factory = None

    @property
    def persistence(self):
        """The object to use for persistence"""
        return self.__persistence

    @persistence.setter
    def persistence(self, value):
        """The object to use for persistence"""
        self.__persistence = value

    @property
    def interactor_factory(self):
        """The object to use to create other interactor objects"""
        return self.__interactor_factory

    @interactor_factory.setter    
    def interactor_factory(self, value):
        """The object to use to create other interactor objects"""
        self.__interactor_factory = value

    
    def validate_string_field(self, field_name, field_value):
        """Throw a ValueError if field_value is None or an empty string.
        :param field_name: The textual name of the field. Used in the event of the field being invalid
        :param field_value: The value to test"""
        if field_value is None or str(field_value).strip() == "":
            raise ValueError("%s must have a value" % field_name)

    def validate_integer_field(self, field_name, field_value):
        """Throw a value error if the given field value is not a numeric digit
        :param field_name: The textual name of the field. Used in the event of the field being invalid
        :param field_value: The value to test"""
        if not str(field_value).isdigit():
            raise ValueError("%s must be a number" % field_name)
