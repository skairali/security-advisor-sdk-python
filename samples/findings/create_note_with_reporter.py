from ibm_cloud_security_advisor import FindingsApiV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator(apikey='abc')
findings_service =FindingsApiV1(authenticator=authenticator)
findings_service.set_service_url("https://us-south.secadvisor.cloud.ibm.com/findings")

response = findings_service.create_note(
  account_id="abc123",
  provider_id="sdktest",
  short_description="sdk test findings",
  long_description="sdk test findings",
  kind="FINDING",
  id="sdk_note_id1",
  reported_by={
    'id':'1',
    'title':'test1',
    'url':'www.test.com'
  },
  finding={
      "severity": "LOW",
      "next_steps": [
        {
          "title": "string",
          "url": "string"
        }
      ]
  }
)

print(response)