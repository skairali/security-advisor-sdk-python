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

from ibm_cloud_security_advisor.findings_api_v1 import Card

from ibm_cloud_sdk_core import BaseService

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiCardClass(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        TestFindingsApiCardClass.app = Card(
            section="", title= "abc", subtitle= "abc", finding_note_names=[], elements=[], order=1, requires_configuration=True, badge_text= "", badge_image=""
        )
        # read env vars
        #envvars = read_credentials()

    @classmethod
    def teardown_class(cls):
        print("\nrunning teardown, cleaning up the env...")
        #print("teardown:delete note")

    def test_init(self):
        print("test init")

    """_from_dict test cases """
    def test_from_dict_bad_key_neg(self):
        self.assertRaises(
            ValueError, Card._from_dict, {"bad_key": "abc"})

    def test_from_dict_missing_section_neg(self):
        self.assertRaises(
            ValueError, Card._from_dict, {})

    def test_from_dict_missing_title_neg(self):
        self.assertRaises(
            ValueError, Card._from_dict, {"section":"abc"})

    def test_from_dict_missing_subtitle_neg(self):
        self.assertRaises(
            ValueError, Card._from_dict, {"section":"abc","title":"abc"})

    def test_from_dict_missing_finding_note_names_neg(self):
        self.assertRaises(
            ValueError, Card._from_dict, {"section": "abc", "title": "abc", "subtitle": "abc", "order": 1})

    def test_from_dict_missing_elements_neg(self):
        self.assertRaises(
            ValueError, Card._from_dict, {"section": "abc", "title": "abc","subtitle":"abc","order":1,
                                         "finding_note_names": "",
                "requires_configuration":True,"badge_text":"abc","badge_image":"abc"
            })

    def test_from_dict_elements_success(self):
        Card._from_dict({"section": "abc", "title": "abc", "subtitle": "abc", "order": 1,
                         "finding_note_names":"",
                        "requires_configuration": True, "badge_text": "abc", "badge_image": "abc",
                        "elements":[]
                        })

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestFindingsApiCardClass.app._to_dict()
    
    """__str__ test cases """
    def test__str__success(self):
        TestFindingsApiCardClass.app.__str__()
    
    """__eq__ test cases """

    def test__eq__not_isinstance(self):
        TestFindingsApiCardClass.app.__eq__({})

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiCardClass.app.__eq__(TestFindingsApiCardClass.app)

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiCardClass.app.__ne__(TestFindingsApiCardClass.app)
