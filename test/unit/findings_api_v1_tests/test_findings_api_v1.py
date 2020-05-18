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

from ibm_cloud_security_advisor import FindingsApiV1

from ibm_cloud_sdk_core import BaseService

from unittest.mock import patch
from unittest import mock
m = mock.Mock()


class TestFindingsApi(unittest.TestCase):
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        with mock.patch('ibm_cloud_security_advisor.findings_api_v1.BaseService') as mocked_os:
            TestFindingsApi.app = FindingsApiV1({},)
        # read env vars
        #envvars = read_credentials()

    @classmethod
    def teardown_class(cls):
        print("\nrunning teardown, cleaning up the env...")
        #print("teardown:delete note")

    def test_init(self):
        with mock.patch('ibm_cloud_security_advisor.findings_api_v1.BaseService') as mocked_os:
            app = FindingsApiV1({},)

    @patch.object(BaseService, '__init__')
    def test_new_instance(self, mock1):
        assert BaseService.__init__ is mock1
        with mock.patch('ibm_cloud_security_advisor.findings_api_v1.get_authenticator_from_environment') as mocked_os:
            FindingsApiV1.new_instance()

    """
    post_graph test cases
    """

    def test_post_graph_account_id_is_none(self):
        account_id = None
        query = "query {occurrence(providerId:\"provider_id\",id:\"id\") {name id}}"
        self.assertRaises(
            ValueError, TestFindingsApi.app.post_graph, account_id, body=query)

    def test_post_graph_body_is_none(self):
        account_id = "abc"
        query = None
        self.assertRaises(
            ValueError, TestFindingsApi.app.post_graph, account_id, body=query)

    @patch.object(BaseService, 'prepare_request')
    @patch.object(BaseService, 'send')
    def test_post_graph_success(self, mock1, mock2):
        query = "query {occurrence(providerId:\"provider_id\",id:\"id\") {name id}}"
        TestFindingsApi.app.post_graph("abc", body=query,
                                       content_type="application/graphql")

    @patch.object(BaseService, 'prepare_request')
    @patch.object(BaseService, 'send')
    def test_post_graph_pass_kwargs(self, mock1, mock2):
        query = "query {occurrence(providerId:\"provider_id\",id:\"id\") {name id}}"
        headers = {"headers": {}}
        TestFindingsApi.app.post_graph("abc", body=query,
                                       content_type="application/graphql", **headers)

    @patch.object(BaseService, 'prepare_request')
    @patch.object(BaseService, 'send')
    def test_post_graph_content_type_is_application_json(self, mock1, mock2):
        query = {}
        headers = {"headers": {}}
        TestFindingsApi.app.post_graph("abc", body=query,
                                       content_type="application/json", **headers)

    """
    create_note test cases
    """

    def test_create_note_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id=None, provider_id="provider_id",
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_create_note_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id="account_id", provider_id=None,
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_create_note_short_description_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id="account_id", provider_id="provider_id",
            short_description=None, long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_create_note_long_description_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id="account_id", provider_id="provider_id",
            short_description="short_description", long_description=None,
            kind="kind", id="id", reported_by={}
        )

    def test_create_note_kind_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id="account_id", provider_id="provider_id",
            short_description="short_description", long_description="long_description",
            kind=None, id="id", reported_by={}
        )

    def test_create_note_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id="account_id", provider_id="provider_id",
            short_description="short_description", long_description="long_description",
            kind="kind", id=None, reported_by={}
        )

    def test_create_note_reported_by_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_note, account_id="account_id", provider_id="provider_id",
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_create_note_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.create_note(account_id="account_id", provider_id="provider_id",
                                        short_description="short_description", long_description="long_description",
                                        kind="kind", id="id", reported_by={},
                                        related_url=[], finding={}, kpi={}, card={}, section={}, **headers)

    """
    list_note test cases
    """

    def test_list_notes_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_notes, account_id=None, provider_id="provider_id"
        )

    def test_list_notes_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_notes, account_id="account_id", provider_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_list_notes_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.list_notes(
            account_id="account_id", provider_id="provider_id", **headers)

    """
    get_note test cases
    """

    def test_get_note_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_note, account_id=None, provider_id="provider_id",
            note_id="abc"
        )

    def test_get_note_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_note, account_id="account_id", provider_id=None,
            note_id="abc"
        )

    def test_get_note_note_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_note, account_id="account_id", provider_id="abc",
            note_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_get_note_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.get_note(
            account_id="account_id", provider_id="provider_id", note_id="abc", **headers)

    """
    update_note test cases
    """

    def test_update_note_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id=None, provider_id="provider_id", note_id="abc",
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_update_note_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id=None, note_id="abc",
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_update_note_note_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id="abc", note_id=None,
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_update_note_short_description_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id="provider_id", note_id="abc",
            short_description=None, long_description="long_description",
            kind="kind", id="id", reported_by={}
        )

    def test_update_note_long_description_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id="provider_id", note_id="abc",
            short_description="short_description", long_description=None,
            kind="kind", id="id", reported_by={}
        )

    def test_update_note_kind_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id="provider_id", note_id="abc",
            short_description="short_description", long_description="long_description",
            kind=None, id="id", reported_by={}
        )

    def test_update_note_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id="provider_id", note_id="abc",
            short_description="short_description", long_description="long_description",
            kind="kind", id=None, reported_by={}
        )

    def test_update_note_reported_by_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_note, account_id="account_id", provider_id="provider_id", note_id="abc",
            short_description="short_description", long_description="long_description",
            kind="kind", id="id", reported_by=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_update_note_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.update_note(account_id="account_id", provider_id="provider_id", note_id="abc",
                                        short_description="short_description", long_description="long_description",
                                        kind="kind", id="id", reported_by={},
                                        related_url=[], finding={}, kpi={}, card={}, section={}, **headers)

    """
    delete_note  test cases
    """

    def test_delete_note_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.delete_note, account_id=None, provider_id="provider_id",
            note_id="abc"
        )

    def test_delete_note_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.delete_note, account_id="account_id", provider_id=None,
            note_id="abc"
        )

    def test_delete_note_note_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.delete_note, account_id="account_id", provider_id="abc",
            note_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_delete_note_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.delete_note(
            account_id="account_id", provider_id="provider_id", note_id="abc", **headers)

    """
    get_occurrence_note test cases
    """

    def test_get_occurrence_note_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_occurrence_note, account_id=None, provider_id="provider_id",
            occurrence_id="abc"
        )

    def test_get_occurrence_note_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_occurrence_note, account_id="account_id", provider_id=None,
            occurrence_id="abc"
        )

    def test_get_occurrence_note_occurrence_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_occurrence_note, account_id="account_id", provider_id="abc",
            occurrence_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_get_occurrence_note_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.get_occurrence_note(
            account_id="account_id", provider_id="provider_id", occurrence_id="abc", **headers)

    """
    create_occurrence test cases
    """

    def test_create_occurrence_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_occurrence, account_id=None, provider_id="provider_id",
            note_name="abc",
            kind="kind", id="id", reported_by={}
        )

    def test_create_occurrence_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_occurrence, account_id="account_id", provider_id=None,
            note_name="abc",
            kind="kind", id="id", reported_by={}
        )

    def test_create_occurrence_note_name_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_occurrence, account_id="account_id", provider_id="provider_id",
            note_name=None,
            kind="kind", id="id", reported_by={}
        )

    def test_create_occurrence_kind_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_occurrence, account_id="account_id", provider_id="provider_id",
            note_name="abc",
            kind=None, id="id", reported_by={}
        )

    def test_create_occurrence_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.create_occurrence, account_id="account_id", provider_id="provider_id",
            note_name="abc",
            kind="kind", id=None, reported_by={}
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_create_occurrence_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.create_occurrence(account_id="account_id", provider_id="provider_id",
                                              note_name="abc",
                                              kind="kind", id="id", context={},
                                              finding={}, kpi={}, **headers)

    """
    list_occurrence test cases
    """

    def test_list_occurrences_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_occurrences, account_id=None, provider_id="provider_id"
        )

    def test_list_occurrences_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_occurrences, account_id="account_id", provider_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_list_occurrences_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.list_occurrences(
            account_id="account_id", provider_id="provider_id", **headers)

    """
    list_note_occurrences test cases
    """

    def test_list_note_occurrences_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_note_occurrences, account_id=None, provider_id="provider_id",
            note_id="abc"
        )

    def test_list_note_occurrences_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_note_occurrences, account_id="account_id", provider_id=None,
            note_id="abc"
        )

    def test_list_note_occurrences_note_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_note_occurrences, account_id="account_id", provider_id="abc",
            note_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_list_note_occurrences_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.list_note_occurrences(
            account_id="account_id", provider_id="provider_id", note_id="abc", **headers)

    """
    get_occurrence test cases
    """

    def test_get_occurrence_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_occurrence, account_id=None, provider_id="provider_id",
            occurrence_id="abc"
        )

    def test_get_occurrence_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_occurrence, account_id="account_id", provider_id=None,
            occurrence_id="abc"
        )

    def test_get_occurrence_occurrence_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.get_occurrence, account_id="account_id", provider_id="abc",
            occurrence_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_get_occurrence_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.get_occurrence(
            account_id="account_id", provider_id="provider_id", occurrence_id="abc", **headers)

    """
    update_occurrence test cases
    """

    def test_update_occurrence_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_occurrence, account_id=None, provider_id="provider_id",
            note_name="abc", occurrence_id="abc",
            kind="kind", id="id", reported_by={}
        )

    def test_update_occurrence_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_occurrence, account_id="account_id", provider_id=None,
            note_name="abc", occurrence_id="abc",
            kind="kind", id="id", reported_by={}
        )

    def test_update_occurrence_occurrence_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_occurrence, account_id="account_id", provider_id="abc",
            note_name="abc", occurrence_id=None,
            kind="kind", id="id", reported_by={}
        )

    def test_update_occurrence_note_name_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_occurrence, account_id="account_id", provider_id="provider_id",
            note_name=None, occurrence_id="abc",
            kind="kind", id="id", reported_by={}
        )

    def test_update_occurrence_kind_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_occurrence, account_id="account_id", provider_id="provider_id",
            note_name="abc", occurrence_id="abc",
            kind=None, id="id", reported_by={}
        )

    def test_update_occurrence_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.update_occurrence, account_id="account_id", provider_id="provider_id",
            note_name="abc", occurrence_id="abc",
            kind="kind", id=None, reported_by={}
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_update_occurrence_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.update_occurrence(account_id="account_id", provider_id="provider_id",
                                              note_name="abc", occurrence_id="abc",
                                              kind="kind", id="id", context={},
                                              finding={}, kpi={}, **headers)

    """
    delete_occurrence test cases
    """

    def test_delete_occurrence_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.delete_occurrence, account_id=None, provider_id="provider_id",
            occurrence_id="abc"
        )

    def test_delete_occurrence_provider_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.delete_occurrence, account_id="account_id", provider_id=None,
            occurrence_id="abc"
        )

    def test_delete_occurrence_occurrence_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.delete_occurrence, account_id="account_id", provider_id="abc",
            occurrence_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_delete_occurrence_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.delete_occurrence(
            account_id="account_id", provider_id="provider_id", occurrence_id="abc", **headers)

    """
    list_providers test cases
    """

    def test_list_providers_account_id_is_none(self):
        self.assertRaises(
            ValueError, TestFindingsApi.app.list_providers, account_id=None
        )

    @patch.object(BaseService, '_convert_model')
    @patch.object(BaseService, 'send')
    @patch.object(BaseService, 'prepare_request')
    def test_list_providers_success(self, mock1, mock2, mock3):
        headers = {"headers": {}}
        TestFindingsApi.app.list_providers(
            account_id="account_id", **headers)
