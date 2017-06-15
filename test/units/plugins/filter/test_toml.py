# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.compat.tests import unittest
from ansible.plugins.filter.toml import to_toml, from_toml


class TestTOML(unittest.TestCase):
    def test_toml_key_value(self):
        kv = {'a': 'b'}
        kv_toml = 'a = "b"\n'
        self.assertEqual(to_toml(kv), kv_toml)
        self.assertEqual(from_toml(kv_toml), kv)

    def test_toml_boolean(self):
        boolean = {'a': False}
        boolean_toml = 'a = false\n'
        self.assertEqual(to_toml(boolean), boolean_toml)
        self.assertEqual(from_toml(boolean_toml), boolean)

    def test_toml_integer(self):
        integer = {'a': 42}
        integer_toml = 'a = 42\n'
        self.assertEqual(to_toml(integer), integer_toml)
        self.assertEqual(from_toml(integer_toml), integer)

    def test_toml_float(self):
        float = {'a': 23.5}
        float_toml = 'a = 23.5\n'
        self.assertEqual(to_toml(float), float_toml)
        self.assertEqual(from_toml(float_toml), float)

    def test_toml_array_of_tables(self):
        array_of_tables = {'a': [{'b': 'c', 'd': 'e'}]}
        array_of_tables_toml = '[[a]]\nb = "c"\nd = "e"\n'
        self.assertEqual(to_toml(array_of_tables), array_of_tables_toml)
        self.assertEqual(from_toml(array_of_tables_toml), array_of_tables)

    def test_toml_array(self):
        array = {'a': [1, 2, 3]}
        array_toml = 'a = [ 1, 2, 3,]\n'
        self.assertEqual(to_toml(array), array_toml)
        self.assertEqual(from_toml(array_toml), array)

    def test_toml_table(self):
        table = {'a': {'b': 'c'}}
        table_toml = '[a]\nb = "c"\n'
        self.assertEqual(to_toml(table), table_toml)
        self.assertEqual(from_toml(table_toml), table)
