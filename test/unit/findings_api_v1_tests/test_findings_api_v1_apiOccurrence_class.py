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

from ibm_cloud_security_advisor.findings_api_v1 import ApiOccurrence

from ibm_cloud_security_advisor.findings_api_v1 import ApiNoteKind
from ibm_cloud_security_advisor.findings_api_v1 import Finding
from ibm_cloud_security_advisor.findings_api_v1 import Kpi
from ibm_cloud_security_advisor.findings_api_v1 import Context

from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiApiOccurrenceClass(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        apiNoteKind = ApiNoteKind()
        kpi = Kpi("")
        finding = Finding()
        context= Context()
        TestFindingsApiApiOccurrenceClass.app = ApiOccurrence(
            note_name="abc",kind=apiNoteKind,id="abc",
            resource_url="abc",remediation="abc",
            create_time= "abc", update_time= "abc",
            context=context,finding=finding,
            kpi=kpi,
        )
        
        # read env vars
        #envvars = read_credentials()

    @classmethod
    def teardown_class(cls):
        print("\nrunning teardown, cleaning up the env...")
        #print("teardown:delete note")

    """_from_dict test cases """
    def test_from_dict_bad_key_neg(self):
        self.assertRaises(
            ValueError, ApiOccurrence._from_dict, {"bad_key": "abc"})

    @patch.object(ApiNoteKind, '_from_dict')
    @patch.object(Context, '_from_dict')
    @patch.object(Finding,'_from_dict')
    @patch.object(Kpi, '_from_dict')
    def test_from_dict_success(self,mock1,mock2,mock3,mock4):
        with mock.patch('ibm_cloud_security_advisor.findings_api_v1.string_to_datetime') as mocked_os:
            ApiOccurrence._from_dict({
                "note_name": "abc",
                "kind":"abc","resource_url":"abc",
                "create_time": "abc", "update_time": "abc", "id": "abc",
                "finding": "abc",
                "kpi": "abc"
            })

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestFindingsApiApiOccurrenceClass.app.to_dict()

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiApiOccurrenceClass.app.__eq__(TestFindingsApiApiOccurrenceClass.app)

    def test__eq__not_isinstance(self):
        TestFindingsApiApiOccurrenceClass.app.__eq__({})

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiApiOccurrenceClass.app.__ne__(TestFindingsApiApiOccurrenceClass.app)
