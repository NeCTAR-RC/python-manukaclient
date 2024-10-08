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

import datetime
import json

from nectarclient_lib.tests.unit import utils

from manukaclient.tests.unit.v1 import fakes
from manukaclient.v1 import external_ids


class ExternalIdsTest(utils.TestCase):
    def setUp(self):
        super().setUp()
        self.cs = fakes.FakeClient()

    def test_update(self):
        new_user_id = '234'
        e = self.cs.external_ids.update(123, user_id=new_user_id)
        self.cs.assert_called(
            'PATCH',
            '/v1/external-ids/123/',
            json.dumps({'user_id': new_user_id}),
        )
        self.assertIsInstance(e, external_ids.ExternalId)
        self.assertIsInstance(e.last_login, datetime.datetime)

    def test_delete(self):
        self.cs.external_ids.delete(123)
        self.cs.assert_called('DELETE', '/v1/external-ids/123/')
