"""Logging Interactor -- holds the logger object"""
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

from Interactors.interactor import Interactor

class LoggingInteractor(Interactor):
    """Logging Interactor -- holds the logger object"""

    def __init__(self):
        super().__init__()
        self.__logger = None

    @property
    def logger(self):
        """The logger object to use for logging"""
        return self.__logger

    @logger.setter
    def logger(self, value):
        self.__logger = value

