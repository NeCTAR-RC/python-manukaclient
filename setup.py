#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

requirements = parse_requirements("requirements.txt", session=False)

entry_points = {
    'openstack.cli.extension':
    ['account = manukaclient.osc.plugin'],
    'openstack.account.v1':
    [
        'account user list = manukaclient.osc.v1.users:ListUsers',
        'account user show = manukaclient.osc.v1.users:ShowUser',
        'account osuser show = manukaclient.osc.v1.users:ShowUserOS',
        'account user set = manukaclient.osc.v1.users:UpdateUser',
    ]
}


setup(
    name='manukaclient',
    version='0.1.0',
    description=('Client for the Nectar Account system'),
    author='Sam Morrison',
    author_email='sorrison@gmail.com',
    url='https://github.com/NeCTAR-RC/python-manukaclient',
    packages=[
        'manukaclient',
    ],
    include_package_data=True,
    install_requires=[str(r.req) for r in requirements],
    license="Apache",
    zip_safe=False,
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ),
    entry_points=entry_points,
)
