from ibm_cloud_security_advisor import NotificationsApiV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator(
    apikey='apikey', url="https://iam.test.cloud.ibm.com/identity/token"
    )
notifications_service =NotificationsApiV1(authenticator=authenticator)
notifications_service.set_service_url("https://us-south.secadvisor.cloud.ibm.com/notifications")


with open("notification.json") as f:
    data = json.load(f)

response = notifications_service.create_notification_channel(
    account_id="accountid",
    **data
)

print(response)
