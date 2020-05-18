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

from ibm_cloud_security_advisor.findings_api_v1 import CardElement

from ibm_cloud_sdk_core import BaseService

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiCardElementClass(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        TestFindingsApiCardElementClass.app = CardElement(
            ""
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
            ValueError, CardElement._from_dict, {"bad_key": "abc"})

    def test_from_dict_missing_kind_neg(self):
        self.assertRaises(
            ValueError, CardElement._from_dict, {})

    def test_from_dict_default_time_range(self):
        CardElement._from_dict({"kind":"abc","default_time_range":"abc"})

    """_to_dict test cases """
    def test_to_dict_success(self):
        TestFindingsApiCardElementClass.app._to_dict()
    
    """__str__ test cases """
    def test__str__success(self):
        TestFindingsApiCardElementClass.app.__str__()
    
    """__eq__ test cases """

    def test__eq__not_isinstance(self):
        TestFindingsApiCardElementClass.app.__eq__({})

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiCardElementClass.app.__eq__(TestFindingsApiCardElementClass.app)

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiCardElementClass.app.__ne__(TestFindingsApiCardElementClass.app)

    def test__get_class_by_discriminator(self):
        CardElement._from_dict({"kind":"abc","default_time_range":"abc"})

    # def test__get_class_by_discriminator_kind_missing(self):
    #     CardElement._from_dict({"default_time_range": "abc"})
