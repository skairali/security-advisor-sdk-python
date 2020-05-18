# coding: utf-8

# Copyright 2020 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test the  ibm_security_advisor_findings_api_sdk service API operations
"""

import pytest
import unittest
import datetime
# import json
# import os

from ibm_cloud_security_advisor.findings_api_v1 import NetworkConnection
from ibm_cloud_security_advisor.findings_api_v1 import  SocketAddress

from ibm_cloud_sdk_core import BaseService

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiNetworkConnectionClass(unittest.TestCase):
    app = {}
    socketAddress= {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        TestFindingsApiNetworkConnectionClass.socketAddress = SocketAddress(
            address="1.1.1.1", port=1)
        TestFindingsApiNetworkConnectionClass.app = NetworkConnection(direction="abc",
                                                      protocol="http",
                                                        client=TestFindingsApiNetworkConnectionClass.socketAddress,
                                                            server=TestFindingsApiNetworkConnectionClass.socketAddress
                                                  )
        # read env vars
        #envvars = read_credentials()

    @classmethod
    def teardown_class(cls):
        print("\nrunning teardown, cleaning up the env...")
        #print("teardown:delete note")

    """_from_dict test cases """
    @patch.object(SocketAddress, '_from_dict')
    def test_from_dict_success(self, mock1):
       NetworkConnection._from_dict({
           "direction": "abc",
           "protocol": "http",
           "client":TestFindingsApiNetworkConnectionClass.socketAddress,
            "server":TestFindingsApiNetworkConnectionClass.socketAddress
       })


    def test_from_dict_value_error(self):
       self.assertRaises(
            ValueError, NetworkConnection._from_dict, {"total": 1.2})

    """_from_dict test cases """
    def test_from_dict_bad_key_neg(self):
        self.assertRaises(
            ValueError, NetworkConnection._from_dict, {"bad_key": "abc"})

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestFindingsApiNetworkConnectionClass.app.to_dict()
    
    """__str__ test cases """
    def test__str__success(self):
        TestFindingsApiNetworkConnectionClass.app.__str__()

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiNetworkConnectionClass.app.__eq__(TestFindingsApiNetworkConnectionClass.app)

    def test__eq__not_isinstance(self):
        TestFindingsApiNetworkConnectionClass.app.__eq__({})

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiNetworkConnectionClass.app.__ne__(TestFindingsApiNetworkConnectionClass.app)
