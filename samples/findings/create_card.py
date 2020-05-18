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
  kind="CARD",
  id="sdk_note_id1",
  reported_by={'id':'1','title':'test1','url':'www.test.com'},
  card={
  "elements": [
    {
      "default_time_range": "1d",
      "kind": "NUMERIC",
      "text": "Count of findings reported by my security tool",
      "value_type": {
        "finding_note_names": [
          "providers/sdktest/notes/sdk_note_name1"
        ],
        "kind": "FINDING_COUNT"
      }
    }
  ],
  "finding_note_names": [
    "providers/sdktest/notes/sdk_note_name1"
  ],
  "section": "My Security Tools",
  "order": 1,
  "title": "My Security Tool Findings",
  "subtitle": "My Security Tool",
  }
)

print(response)