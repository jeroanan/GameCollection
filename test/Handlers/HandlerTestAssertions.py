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

from unittest.mock import Mock

import json

def get_empty_param_assertion(handler):
    
    def assert_empty_param_returns_empty_string(param, params):
        params[param] = ""
        result = handler.get_page(params)
        return result == ""
    
    return assert_empty_param_returns_empty_string

def get_missing_param_assertion(handler):
    
    def assert_missing_param_returns_empty_string(param, params):
        del(params[param])
        result = handler.get_page(params)
        return result == ""

    return assert_missing_param_returns_empty_string

def get_params_returns_json_result_value_assertion(test_class, handler):
    """
    Get an assertion function that tests that calling a handler's get_page method causes the given result value of a
    json object to be returned.

    Args:
        test_class: An instance of UnitTest.TestCase
        handler: An instance of Handler that is executed when the returned closure is called
    
    Returns:
        A function that will execute handler.get_page with the given parameters and assert that the expected value is 
        returned in the resulting json object's result field.
    """

    def do_params_give_json_result_value(params, result_value):
        """
        Assert that when handler.get_page is called with params, the expected result_value is returned in the returned
        json object's result field.

        Args:
            params: The params to pass to handler.get_page
            result_value: The expected value of the returned json object's result field
        """
        json_result = json.loads(handler.get_page(params))
        test_class.assertEqual(result_value, json_result['result'])

    return do_params_give_json_result_value

def get_exceptions_returns_json_result_value_assertion(test_class, handler, interactor):
    """
    Get an assertion that tests that when and exception is encountered by handler.get_page, the expected result_value
    is returned for that exception.

    Args:
        test_class: An instance of UnitTest.TestCase
        handler: An instance of Handler that is executed when the returned closure is called
        interactor: The instance of Interactor that generates the exception
    
    Returns:
        A function that will execute handler.get_page with the given parameters for each pair of exception and result 
        value and assert that the expected value is returned in the resulting json object's result field when the given
        exception is encountered.
    """
    def do_exceptions_give_json_result_value(params, exceptions_and_results):
        """
        Assert that when handler is called with each of the given exceptions, the matching result value is returned.

        Args:
            params: The params to call handler.get_page with
            exceptions_and_results: A list of tuples. Each tuple is (exception_type, result_value).
        """
        assertion = get_exception_returns_json_result_value_assertion(test_class, handler, interactor)

        for ec in exceptions_and_results:
            expected_exception, result_value = ec
            assertion(params, expected_exception, result_value)

    return do_exceptions_give_json_result_value

def get_exception_returns_json_result_value_assertion(test_class, handler, interactor):
    """
    Get an assertion function that tests that when an exception is encountered by handler.get_page, the expected 
    result_value is returned in the returned json object's result field.

    Args:
        test_class: An instance of UnitTest.TestCase
        handler: An instance of Handler that is executed when the returned closure is called
        interactor: The instance of Interactor that generates the exception

    Returns:
        A function that will execute handler.get_page with the given parameters and assert that the expected value is 
        returned in the resulting json object's result field when the given exception is encountered.
    """

    def does_exception_give_json_result_value(params, exception_type, result_value):
        """
        Assert that when handler.get_page encounters an exception of type exception_type, the returned json object's
        result value is result_value
        
        Args:
            params: Parameters to pass to handler.get_page
            exception_type: The type of exception that is expected to be encountered
            result_value: The expected value of result.result
        """
        
        def interactor_execute(x):
            raise exception_type

        interactor.execute = Mock(side_effect=interactor_execute)
        assertion = get_params_returns_json_result_value_assertion(test_class, handler)
        assertion(params, result_value)

    return does_exception_give_json_result_value

def get_bad_value_returns_json_validation_failed_assertion(test_class, handler, required_params):
    """
    Get an assertion function that tests that when required values are set to None/empty, 'validation_failed' is given
    in the returned json object's result field.

    Args:
        test_class: An instance of UnitTest.TestCase
        handler: An instance of Handler that is executed when the returned closure is called
        required_params: A list of parameter names that should be given None/empty values

    Returns: A function that will execute handler.get_page with its required parameters set to None/empty in turn. The 
    returned json message's result field will be asserted to be 'validation_failed'
    """
    
    def do_bad_values_give_json_validation_failed_message(params):
        """
        Assert that calling handler.get_page with required parameters set to None/empty in turn causes the returned json
        object's result field to be 'validation_failed'

        Args:
            params: The parameters to send to handler.get_page        
        """
        
        def delete_param(x, p):
            del x[p]
            return x

        def empty_param(x, p):
            x[p] = ''
            return x

        def null_param(x, p):
            x[p] = None
            return x

        funcs = [delete_param, empty_param, null_param]

        assertion = get_params_returns_json_result_value_assertion(test_class, handler)

        for rp in required_params:
            for f in funcs:
                ps = f(dict(params), rp)
                assertion(ps, 'validation_failed')
                

    return do_bad_values_give_json_validation_failed_message


def assert_operation_on_params_returns_true(func, params):
        for p in params:
            return func(p)
