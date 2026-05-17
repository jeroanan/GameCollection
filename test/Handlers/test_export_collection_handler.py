"""Provides unit tests for the ExportCollectionHandler class"""
# Copyright (c) David Wilson 2015, 2026
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

import ui.Handlers.authenticated_handler as ah
import ui.Handlers.ExportCollectionHandler as ech
import ui.Handlers.Session.Session as sess
import ui.template_renderer as tr


class TestExportCollectionHandler(unittest.TestCase):
    """Unit tests for the ExportCollectionHandler class"""

    def setUp(self):
        self.__renderer = Mock(tr.TemplateRenderer)
        self.__target = ech.ExportCollectionHandler(None, self.__renderer)
        self.__target.session = Mock(sess.Session)

    def test_is_instance_of_authenticated_handler(self):
        """Test that ExportCollectionHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that calling ExportCollectionHandler.get_page calls renderer.render correctly"""
        self.__target.get_page(None)
        self.__renderer.render.assert_called_with(
            'exportcollection.html',
            title='Export Collection')
