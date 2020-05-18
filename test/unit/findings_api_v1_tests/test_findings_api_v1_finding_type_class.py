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

from ibm_cloud_security_advisor.findings_api_v1 import FindingType
from ibm_cloud_security_advisor.findings_api_v1 import Severity
from ibm_cloud_security_advisor.findings_api_v1 import RemediationStep

from ibm_cloud_sdk_core import BaseService

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiFindingTypeClass(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        severity = Severity()
        remediationStep = RemediationStep()

        TestFindingsApiFindingTypeClass.app = FindingType(severity=severity,
                                                      next_steps=[
                                                          remediationStep],
                                                  )
        # read env vars
        #envvars = read_credentials()

    @classmethod
    def teardown_class(cls):
        print("\nrunning teardown, cleaning up the env...")
        #print("teardown:delete note")

    """_from_dict test cases """
    def test_from_dict_success(self):
       FindingType._from_dict({
           "severity": {},
           "next_steps": [],
       })

    """_from_dict test cases """
    def test_from_dict_bad_key_neg(self):
        self.assertRaises(
            ValueError, FindingType._from_dict, {"bad_key": "abc"})

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestFindingsApiFindingTypeClass.app.to_dict()
    
    """__str__ test cases """
    def test__str__success(self):
        TestFindingsApiFindingTypeClass.app.__str__()

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiFindingTypeClass.app.__eq__(TestFindingsApiFindingTypeClass.app)

    def test__eq__not_isinstance(self):
        TestFindingsApiFindingTypeClass.app.__eq__({})

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiFindingTypeClass.app.__ne__(TestFindingsApiFindingTypeClass.app)
