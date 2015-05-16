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

def get_missing_param_assertion(handler):
    
    def assert_missing_param_returns_empty_string(param, params):
        del(params[param])
        result = handler.get_page(params)
        return result == ""

    return assert_missing_param_returns_empty_string


def get_empty_param_assertion(handler):
    
    def assert_empty_param_returns_empty_string(param, params):
        params[param] = ""
        result = handler.get_page(params)
        return result == ""
    
    return assert_empty_param_returns_empty_string

def assert_operation_on_params_returns_true(func, params):
        for p in params:
            return func(p)
