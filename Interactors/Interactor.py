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

    def __init__(self):
        self.__persistence = None

    @property
    def persistence(self):
        return self.__persistence

    @persistence.setter
    def persistence(self, value):
        self.__persistence = value

    """Throw a ValueError if field_value is None or an empty string. 
    field_name is included in the exception."""
    def validate_string_field(self, field_name, field_value):
        if field_value is None or str(field_value).strip() == "":
            raise ValueError("%s must have a value" % field_name)

    def validate_integer_field(self, field_name, field_value):
        if not str(field_value).isdigit():
            raise ValueError("%s must be a number" % field_name)
