from ibm_cloud_security_advisor import NotificationsApiV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    apikey='abc')
notifications_service =NotificationsApiV1(authenticator=authenticator)
notifications_service.set_service_url("https://us-south.secadvisor.cloud.ibm.com/notifications")

response = notifications_service.delete_notification_channels(
    account_id="abc",
    body=["<channel_id1>", "<channel_id2>"]
)

print(response)
