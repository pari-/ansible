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

from ansible import errors
from ansible.plugins.lookup import LookupBase
from ansible.utils.listify import listify_lookup_plugin_terms

try:
    import toml
except ImportError:
    raise errors.AnsibleFilterError('You need to install "toml" prior to using a "*_toml"-filter')


def to_toml(a):
    ''' Convert the value to TOML '''

    try:
        output = toml.dumps(a)
    except AttributeError as e:
        if str(e).find("object has no attribute 'keys'"):
            raise errors.AnsibleFilterError('Only dicts can be fed to: to_toml')
        else:
            raise e
    return output


def from_toml(a):
    ''' Convert the value from TOML '''

    try:
        output = toml.loads(str(a))
    except AttributeError as e:
        raise e
    return output


class FilterModule(object):
    ''' TOML filters '''

    def filters(self):
        return {
            'to_toml': to_toml,
            'from_toml': from_toml
        }
