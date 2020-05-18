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

from ibm_cloud_security_advisor.findings_api_v1 import ApiNote

from ibm_cloud_security_advisor.findings_api_v1 import ApiNoteKind
from ibm_cloud_security_advisor.findings_api_v1 import ApiNoteRelatedUrl
from ibm_cloud_security_advisor.findings_api_v1 import Reporter
from ibm_cloud_security_advisor.findings_api_v1 import KpiType
from ibm_cloud_security_advisor.findings_api_v1 import Card
from ibm_cloud_security_advisor.findings_api_v1 import Section
from ibm_cloud_security_advisor.findings_api_v1 import FindingType
from ibm_cloud_security_advisor.findings_api_v1 import Severity 

from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiApiNoteClass(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        apiNoteKind = ApiNoteKind()
        apiNoteRelatedUrl = ApiNoteRelatedUrl()
        reporter = Reporter("","")
        kpiType = KpiType("")
        card = Card("","","","","")
        section = Section("","")
        severity = Severity()
        findingType = FindingType(severity=severity)
        TestFindingsApiApiNoteClass.app = ApiNote(
             short_description= "abc", long_description= "abc",
                kind=apiNoteKind,related_url=[apiNoteRelatedUrl],expiration_time="abc",
                create_time= "abc", update_time= "abc", id= "abc",
            shared=True, reported_by=reporter, finding=findingType,
            kpi=kpiType, card=card, section=section,
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
            ValueError, ApiNote._from_dict, {"bad_key": "abc"})

    @patch.object(ApiNoteKind, '_from_dict')
    @patch.object(ApiNoteRelatedUrl, '_from_dict')
    @patch.object(Reporter, '_from_dict')
    @patch.object(FindingType, '_from_dict')
    @patch.object(KpiType, '_from_dict')
    @patch.object(Card, '_from_dict')
    @patch.object(Section, '_from_dict')
    def test_from_dict_success(self,mock1,mock2,mock3,mock4
    ,mock5,mock6,mock7):
        with mock.patch('ibm_cloud_security_advisor.findings_api_v1.string_to_datetime') as mocked_os:
            ApiNote._from_dict({
                "short_description": "abc", "long_description": "abc",
                "kind":"abc","related_url":"abc","expiration_time":"abc",
                "create_time": "abc", "update_time": "abc", "id": "abc",
                "shared": True, "reported_by": "abc", "finding": "abc",
                "kpi": "abc","card": "abc","section": "abc",
            })

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestFindingsApiApiNoteClass.app.to_dict()

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiApiNoteClass.app.__eq__(TestFindingsApiApiNoteClass.app)

    def test__eq__not_isinstance(self):
        TestFindingsApiApiNoteClass.app.__eq__({})

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiApiNoteClass.app.__ne__(TestFindingsApiApiNoteClass.app)
