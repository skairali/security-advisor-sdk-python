from ibm_cloud_security_advisor import FindingsApiV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator(apikey='<<Apikey here>>')
findings_service =FindingsApiV1(authenticator=authenticator)
findings_service.set_service_url("https://us-south.secadvisor.cloud.ibm.com/findings")


with open('findings.json') as f:
  data = json.load(f)

response = findings_service.create_note(
  account_id="<<Account ID here>>",
  **data
)

print(response)
