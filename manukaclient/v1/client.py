#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from nectarclient_lib import exceptions

from manukaclient import client
from manukaclient.v1 import external_ids
from manukaclient.v1 import keystone_ext
from manukaclient.v1 import users


class Client:
    """Client for the Nectar Allocations v1 API
    :param string session: session
    :type session: :py:class:`keystoneauth.adapter.Adapter`
    """

    def __init__(self, session=None, service_type='account', **kwargs):
        """Initialize a new client for the Manuka v1 API."""
        if session is None:
            raise exceptions.ClientException(
                message='Session is required argument'
            )
        self.http_client = client.SessionClient(
            session, service_type=service_type, **kwargs
        )
        self.external_ids = external_ids.ExternalIdManager(self.http_client)
        self.keystone_ext = keystone_ext.KeystoneExtManager(self.http_client)
        self.pending_users = users.PendingUserManager(self.http_client)
        self.users = users.UserManager(self.http_client)
