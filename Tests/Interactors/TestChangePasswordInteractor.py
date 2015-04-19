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

import unittest
from unittest.mock import Mock

from Interactors.Exceptions.InteractorFactoryNotSetException import InteractorFactoryNotSetException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.LoggingInteractor import LoggingInteractor
from User import User


class ChangePasswordInteractor(LoggingInteractor):
    
    def execute(self, user):
        if self.interactor_factory is None:
            raise InteractorFactoryNotSetException


class TestChangePasswordInteractor(unittest.TestCase):
    
    def test_is_logging_interactor(self):
        target = ChangePasswordInteractor()
        self.assertIsInstance(target, LoggingInteractor)

    def test_execute_interactor_factory_not_set_raises_interactor_factory_not_set_exception(self):
        target = ChangePasswordInteractor()
        self.assertRaises(InteractorFactoryNotSetException, target.execute, User())
        
