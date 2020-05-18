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

from ibm_cloud_security_advisor.findings_api_v1 import ApiListNoteOccurrencesResponse

from ibm_cloud_security_advisor.findings_api_v1 import ApiOccurrence

from ibm_cloud_sdk_core import BaseService

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApiApiListNoteOccurrencesResponseClass(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        apiOccurrence = ApiOccurrence("abc","abc","abc")
        TestFindingsApiApiListNoteOccurrencesResponseClass.app = ApiListNoteOccurrencesResponse(
            occurrences=[apiOccurrence],next_page_token="abc"
            )
        # read env vars
        #envvars = read_credentials()

    @classmethod
    def teardown_class(cls):
        print("\nrunning teardown, cleaning up the env...")
        #print("teardown:delete note")

    """_from_dict test cases """
    @patch.object(ApiOccurrence, '_from_dict')
    def test_from_dict_success(self,mock1):
       ApiListNoteOccurrencesResponse._from_dict({
             "occurrences":[{}],"next_page_token":"abc"
       })

    """_to_dict test cases """
    @patch.object(ApiOccurrence, 'to_dict')
    def test_to_dict_success(self,mock1):
        TestFindingsApiApiListNoteOccurrencesResponseClass.app.to_dict()
    
    # """__str__ test cases """
    # @patch.object(ApiOccurrence, 'to_dict')
    # def test__str__success(self,mock1):
    #     TestFindingsApiApiListNoteOccurrencesResponseClass.app.__str__()

    """__eq__ test cases """

    def test__eq__isinstance(self):
        TestFindingsApiApiListNoteOccurrencesResponseClass.app.__eq__(TestFindingsApiApiListNoteOccurrencesResponseClass.app)

    def test__eq__not_isinstance(self):
        TestFindingsApiApiListNoteOccurrencesResponseClass.app.__eq__({})

    """__ne__ test cases """

    def test__ne__isinstance(self):
        TestFindingsApiApiListNoteOccurrencesResponseClass.app.__ne__(TestFindingsApiApiListNoteOccurrencesResponseClass.app)
