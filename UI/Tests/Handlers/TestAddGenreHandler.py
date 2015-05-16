# Copyright (c) David Wilson 2015
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

from functools import partial
import unittest
from unittest.mock import Mock

from Genre import Genre
from Interactors.Genre.AddGenreInteractor import AddGenreInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.AddGenreHandler import AddGenreHandler
from UI.Handlers.Session.Session import Session
from UI.Tests.Handlers.HandlerTestAssertions import (get_missing_param_assertion, 
                                                     get_empty_param_assertion, 
                                                     assert_operation_on_params_returns_true)


class TestAddGenreHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(AddGenreInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = AddGenreHandler(interactor_factory, None)
        self.__target.session = Mock(Session)
        self.__set_assertions()
        
    def __set_assertions(self):
        missing_param_assertion = get_missing_param_assertion(self.__target)
        self.__missing_param_test = partial(missing_param_assertion, params=self.__get_params())
        empty_param_assertion = get_empty_param_assertion(self.__target)
        self.__empty_param_test = partial(empty_param_assertion, params=self.__get_params())

    def test_is_type_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_misssing_required_params_returns_empty_string(self):
        params = ["name", "description"]
        self.assertTrue(assert_operation_on_params_returns_true(self.__missing_param_test, params))

    def test_empty_required_params_returns_empty_string(self):
        params = ["name", "description"]
        self.assertTrue(assert_operation_on_params_returns_true(self.__empty_param_test, params))    

    def test_executes_interactor(self):
        params = self.__get_params()
        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(Genre.from_dict(self.__get_params()))

    def __get_params(self, name="name", description="description"):
        return {"name": name,
                "description": description}


