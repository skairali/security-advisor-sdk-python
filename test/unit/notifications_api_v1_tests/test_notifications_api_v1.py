# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import unittest
import responses
from ibm_cloud_security_advisor.notifications_api_v1 import *
from ibm_cloud_security_advisor import NotificationsApiV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core import BaseService
base_url = 'https://us-south.secadvisor.cloud.ibm.com/notifications'

from unittest import mock
from unittest.mock import patch
m = mock.Mock()

base_url = 'https://gateway.watsonplatform.net/notifications'

##############################################################################
# Start of Service: NotificationChannel
##############################################################################
# region


class TestNotificationsApiV1():
    app = {}
    @classmethod
    def setup_class(cls):
        print("\nrunning setup preparation...")
        with mock.patch('ibm_cloud_security_advisor.notifications_api_v1.BaseService') as mocked_os:
            TestNotificationsApiV1.app = NotificationsApiV1({
            },)

    def test_init(self):
        with mock.patch('ibm_cloud_security_advisor.notifications_api_v1.BaseService') as mocked_os:
            app = NotificationsApiV1({},)

    @patch.object(BaseService, '__init__')
    def test_new_instance(self, mock1):
        assert BaseService.__init__ is mock1
        with mock.patch('ibm_cloud_security_advisor.notifications_api_v1.get_authenticator_from_environment') as mocked_os:
            NotificationsApiV1.new_instance()

#-----------------------------------------------------------------------------
# Test Class for list_all_channels
#-----------------------------------------------------------------------------
class TestListAllChannels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_channels_response(self):
        body = self.construct_full_body()
        response = fake_response_ListChannelsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_channels_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListChannelsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_channels_empty(self):
        check_empty_required_params(self, fake_response_ListChannelsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels'.format(body['account_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_all_channels(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['limit'] = 12345
        body['skip'] = 12345
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_notification_channel
#-----------------------------------------------------------------------------
class TestCreateNotificationChannel(unittest.TestCase):

    def test_create_notification_channel_account_id_is_none(self):
        account_id = None
        data = {
            "name": "sdk_test_notification1",
            "description": "test1 description",
            "type": "Webhook",
            "endpoint": "http://test.com",
            "enabled": True,
            "severity": [
                "high",
                "medium",
                "low"
            ],
            "alertSource": [
                {
                    "provider_name": "VA",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "CERT",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "config-advisor",
                    "finding_types": [
                        "appprotection-dns_not_proxied",
                        "appprotection-dnssec_off"
                    ]
                }
            ]
        }
        self.assertRaises(
            ValueError, TestNotificationsApiV1.app.create_notification_channel, account_id,**data)

    def test_create_notification_channel_name_is_none(self):
            account_id = "abc"
            data = {
                "name": None,
                "description": "test1 description",
                "type": "Webhook",
                "endpoint": "http://test.com",
                "enabled": True,
                "severity": [
                    "high",
                    "medium",
                    "low"
                ],
                "alertSource": [
                    {
                        "provider_name": "VA",
                        "finding_types": [
                            "ALL"
                        ]
                    },
                    {
                        "provider_name": "CERT",
                        "finding_types": [
                            "ALL"
                        ]
                    },
                    {
                        "provider_name": "config-advisor",
                        "finding_types": [
                            "appprotection-dns_not_proxied",
                            "appprotection-dnssec_off"
                        ]
                    }
                ]
            }
            self.assertRaises(
                ValueError, TestNotificationsApiV1.app.create_notification_channel, account_id,**data)

    def test_create_notification_channel_type_is_none(self):
            account_id = "abc"
            data = {
                "name": "sdk_test_notification1",
                "description": "test1 description",
                "type": None,
                "endpoint": "http://test.com",
                "enabled": True,
                "severity": [
                    "high",
                    "medium",
                    "low"
                ],
                "alertSource": [
                    {
                        "provider_name": "VA",
                        "finding_types": [
                            "ALL"
                        ]
                    },
                    {
                        "provider_name": "CERT",
                        "finding_types": [
                            "ALL"
                        ]
                    },
                    {
                        "provider_name": "config-advisor",
                        "finding_types": [
                            "appprotection-dns_not_proxied",
                            "appprotection-dnssec_off"
                        ]
                    }
                ]
            }
            self.assertRaises(
                ValueError, TestNotificationsApiV1.app.create_notification_channel, account_id,**data)

    def test_create_notification_channel_endpoint_is_none(self):
        account_id = "abc"
        data = {
            "name": "sdk_test_notification1",
            "description": "test1 description",
            "type": "Webhook",
            "endpoint": None,
            "enabled": True,
            "severity": [
                    "high",
                    "medium",
                    "low"
            ],
            "alertSource": [
                {
                    "provider_name": "VA",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "CERT",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "config-advisor",
                    "finding_types": [
                        "appprotection-dns_not_proxied",
                        "appprotection-dnssec_off"
                    ]
                }
            ]
        }
        self.assertRaises(
            ValueError, TestNotificationsApiV1.app.create_notification_channel, account_id, **data)


    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_notification_channel_response(self):
        body = self.construct_full_body()
        response = fake_response_CreateChannelsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_notification_channel_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CreateChannelsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_notification_channel_empty(self):
        check_empty_required_params(self, fake_response_CreateChannelsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels'.format(body['account_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.create_notification_channel(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body.update({"name": "string1", "type": "string1", "endpoint": "string1", "description": "string1", "severity": [], "enabled": True, "alert_source": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        body.update({"name": "string1", "type": "string1", "endpoint": "string1", "description": "string1", "severity": [], "enabled": True, "alert_source": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_notification_channels
#-----------------------------------------------------------------------------
class TestDeleteNotificationChannels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_notification_channels_response(self):
        body = self.construct_full_body()
        response = fake_response_BulkDeleteChannelsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_notification_channels_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BulkDeleteChannelsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_notification_channels_empty(self):
        check_empty_required_params(self, fake_response_BulkDeleteChannelsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels'.format(body['account_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_notification_channels(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['body'] = []
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['body'] = []
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_notification_channel
#-----------------------------------------------------------------------------
class TestDeleteNotificationChannel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_notification_channel_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_notification_channel_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_notification_channel_empty(self):
        check_empty_required_params(self, fake_response_DeleteChannelResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels/{1}'.format(body['account_id'], body['channel_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_notification_channel(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_notification_channel
#-----------------------------------------------------------------------------
class TestGetNotificationChannel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_notification_channel_response(self):
        body = self.construct_full_body()
        response = fake_response_GetChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_notification_channel_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_GetChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_notification_channel_empty(self):
        check_empty_required_params(self, fake_response_GetChannelResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels/{1}'.format(body['account_id'], body['channel_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_notification_channel(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_notification_channel
#-----------------------------------------------------------------------------
class TestUpdateNotificationChannel(unittest.TestCase):

    def test_update_notification_channel_name_is_none(self):
        account_id = "abc"
        data = {
            "channel_id": "abc",
            "name": None,
            "description": "test1 description",
            "type": "Webhook",
            "endpoint": "http://test.com",
            "enabled": True,
            "severity": [
                "high",
                "medium",
                "low"
            ],
            "alertSource": [
                {
                    "provider_name": "VA",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "CERT",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "config-advisor",
                    "finding_types": [
                        "appprotection-dns_not_proxied",
                        "appprotection-dnssec_off"
                    ]
                }
            ]
        }
        self.assertRaises(
            ValueError, TestNotificationsApiV1.app.update_notification_channel, account_id, **data)

    def test_update_notification_channel_channel_id_is_none(self):
        account_id = "abc"
        data = {
            "channel_id": None,
            "name": "abc",
            "description": "test1 description",
            "type": "Webhook",
            "endpoint": "http://test.com",
            "enabled": True,
            "severity": [
                    "high",
                    "medium",
                    "low"
            ],
            "alertSource": [
                {
                    "provider_name": "VA",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "CERT",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "config-advisor",
                    "finding_types": [
                        "appprotection-dns_not_proxied",
                        "appprotection-dnssec_off"
                    ]
                }
            ]
        }
        self.assertRaises(
            ValueError, TestNotificationsApiV1.app.update_notification_channel, account_id, **data)

    def test_update_notification_channel_type_is_none(self):
        account_id = "abc"
        data = {
            "channel_id": "abc",
            "name": "sdk_test_notification1",
            "description": "test1 description",
            "type": None,
            "endpoint": "http://test.com",
            "enabled": True,
            "severity": [
                    "high",
                    "medium",
                    "low"
            ],
            "alertSource": [
                {
                    "provider_name": "VA",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "CERT",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "config-advisor",
                    "finding_types": [
                        "appprotection-dns_not_proxied",
                        "appprotection-dnssec_off"
                    ]
                }
            ]
        }
        self.assertRaises(
            ValueError, TestNotificationsApiV1.app.update_notification_channel, account_id, **data)

    def test_update_notification_channel_endpoint_is_none(self):
        account_id = "abc"
        data = {
            "channel_id": "abc",
            "name": "sdk_test_notification1",
            "description": "test1 description",
            "type": "Webhook",
            "endpoint": None,
            "enabled": True,
            "severity": [
                    "high",
                    "medium",
                    "low"
            ],
            "alertSource": [
                {
                    "provider_name": "VA",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "CERT",
                    "finding_types": [
                        "ALL"
                    ]
                },
                {
                    "provider_name": "config-advisor",
                    "finding_types": [
                        "appprotection-dns_not_proxied",
                        "appprotection-dnssec_off"
                    ]
                }
            ]
        }
        self.assertRaises(
            ValueError, TestNotificationsApiV1.app.update_notification_channel, account_id, **data)



    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_notification_channel_response(self):
        body = self.construct_full_body()
        response = fake_response_UpdateChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_notification_channel_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_UpdateChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_notification_channel_empty(self):
        check_empty_required_params(self, fake_response_UpdateChannelResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels/{1}'.format(body['account_id'], body['channel_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.update_notification_channel(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        body.update({"name": "string1", "type": "string1", "endpoint": "string1", "description": "string1", "severity": [], "enabled": True, "alert_source": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        body.update({"name": "string1", "type": "string1", "endpoint": "string1", "description": "string1", "severity": [], "enabled": True, "alert_source": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for test_notification_channel
#-----------------------------------------------------------------------------
class TestTestNotificationChannel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_test_notification_channel_response(self):
        body = self.construct_full_body()
        response = fake_response_TestChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_test_notification_channel_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TestChannelResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_test_notification_channel_empty(self):
        check_empty_required_params(self, fake_response_TestChannelResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/channels/{1}/test'.format(body['account_id'], body['channel_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.test_notification_channel(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        body['channel_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_public_key
#-----------------------------------------------------------------------------
class TestGetPublicKey():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_public_key_response(self):
        body = self.construct_full_body()
        response = fake_response_PublicKeyResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_public_key_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_PublicKeyResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_public_key_empty(self):
        check_empty_required_params(self, fake_response_PublicKeyResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/{0}/notifications/public_key'.format(body['account_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NotificationsApiV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_public_key(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['account_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['account_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: NotificationChannel
##############################################################################


def check_empty_required_params(obj, response):
    """Test function to assert that the operation will throw an error when given empty required data

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    body = {k: None for k in body.keys()}
    error = False
    try:
        send_request(obj, body, response)
    except ValueError as e:
        error = True
    assert error

def check_missing_required_params(obj):
    """Test function to assert that the operation will throw an error when missing required data

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    url = obj.make_url(body)
    error = False
    try:
        send_request(obj, {}, {}, url=url)
    except TypeError as e:
        error = True
    assert error

def check_empty_response(obj):
    """Test function to assert that the operation will return an empty response when given an empty request

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    url = obj.make_url(body)
    send_request(obj, {}, {}, url=url)

def send_request(obj, body, response, url=None):
    """Test function to create a request, send it, and assert its accuracy to the mock response

    Args:
        obj: The generated test function
        body: Dict filled with fake data for calling the service
        response_str: Mock response string

    """
    if not url:
        url = obj.make_url(body)
    obj.add_mock_response(url, response)
    output = obj.call_service(body)
    assert responses.calls[0].request.url.startswith(url)
    assert output.get_result() == response

####################
## Mock Responses ##
####################

fake_response__json = None
fake_response_ListChannelsResponse_json = """{"channels": []}"""
fake_response_CreateChannelsResponse_json = """{"channel_id": "fake_channel_id", "statusCode": 11}"""
fake_response_BulkDeleteChannelsResponse_json = """{"message": "fake_message"}"""
fake_response_DeleteChannelResponse_json = """{"channel_id": "fake_channel_id", "message": "fake_message"}"""
fake_response_GetChannelResponse_json = """{"channel": {"channel_id": "fake_channel_id", "name": "fake_name", "description": "fake_description", "type": "fake_type", "severity": {"high": true, "medium": true, "low": false}, "endpoint": "fake_endpoint", "enabled": false, "alertSource": [], "frequency": "fake_frequency"}}"""
fake_response_UpdateChannelResponse_json = """{"channel_id": "fake_channel_id", "statusCode": 11}"""
fake_response_TestChannelResponse_json = """{"test": "fake_test"}"""
fake_response_PublicKeyResponse_json = """{"publicKey": "fake_public_key"}"""
