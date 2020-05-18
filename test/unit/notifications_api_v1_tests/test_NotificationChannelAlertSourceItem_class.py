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
Test the  ibm_security_advisor_notifications_api_sdk service API operations
"""

import pytest
import unittest
import datetime
# import json
# import os

from ibm_cloud_security_advisor import NotificationsApiV1

from ibm_cloud_security_advisor.notifications_api_v1 import NotificationChannelAlertSourceItem

from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestNotificationChannelAlertSourceItem(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        TestNotificationChannelAlertSourceItem.app = NotificationChannelAlertSourceItem(
             provider_name="abc",finding_types=['abc']
        )
        
        # read env vars
        #envvars = read_credentials()

    """_from_dict test cases """
    def test_from_dict_bad_key_neg(self):
        self.assertRaises(
            ValueError, NotificationChannelAlertSourceItem._from_dict, {"bad_key": "abc"})

    """_from_dict test cases """
    def test_from_dict_provider_name_neg(self):
        self.assertRaises(
            ValueError, NotificationChannelAlertSourceItem._from_dict, {"finding_types": ['abc']})

    def test_from_dict_success(self):
        res = NotificationChannelAlertSourceItem._from_dict({
            "provider_name": "abc", "finding_types": ['abc']
        })
        print(res)

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestNotificationChannelAlertSourceItem.app.to_dict()

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestNotificationChannelAlertSourceItem.app.__eq__(TestNotificationChannelAlertSourceItem.app)

    def test__eq__not_isinstance(self):
        TestNotificationChannelAlertSourceItem.app.__eq__({})

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestNotificationChannelAlertSourceItem.app.__ne__(TestNotificationChannelAlertSourceItem.app)
