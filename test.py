#!/usr/bin/env python

from manukaclient import client
from nectar_tools import auth


session = auth.get_session()

c = client.Client('1', session=session)
try:
    print(c.users.list()[0])
except Exception as e:
    print(e)

try:
    print(c.users.get('1'))
except Exception as e:
    print(e)
try:
    print(c.users.get('18'))
except Exception as e:
    print(e)
