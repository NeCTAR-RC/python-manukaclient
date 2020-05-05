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

import json

from manukaclient.v1 import users

from manukaclient.tests.unit import utils
from manukaclient.tests.unit.v1 import fakes


class UsersTest(utils.TestCase):

    def setUp(self):
        super(UsersTest, self).setUp()
        self.cs = fakes.FakeClient()

    def test_user_list(self):
        ul = self.cs.users.list()
        self.cs.assert_called('GET', '/v1/users/')
        for u in ul:
            self.assertIsInstance(u, users.User)
        self.assertEqual(3, len(ul))

    def test_user_get(self):
        u = self.cs.users.get(123)
        self.cs.assert_called('GET', '/v1/users/123/')
        self.assertIsInstance(u, users.User)
        self.assertEqual(123, u.id)

    def test_update(self):
        new_orcid = 'new-orcid'
        u = self.cs.users.update(123, orcid=new_orcid)
        self.cs.assert_called('PATCH', '/v1/users/123/',
                              json.dumps({'orcid': new_orcid}))
        self.assertIsInstance(u, users.User)
        self.assertEqual(new_orcid, u.orcid)

    def test_search(self):
        query = 'needle'
        ul = self.cs.users.search(query)
        self.cs.assert_called('POST', '/v1/users/search/', {'search': query})
        for u in ul:
            self.assertIsInstance(u, users.User)