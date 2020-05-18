from ibm_cloud_security_advisor import FindingsApiV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator(apikey='abc')
findings_service =FindingsApiV1(authenticator=authenticator)
findings_service.set_service_url("https://us-south.secadvisor.cloud.ibm.com/findings")

response = findings_service.create_occurrence(
  account_id="abc123",
  provider_id="sdktest",
  note_name="abc123/providers/sdktest/notes/sdk_note_id1",
  kind="FINDING",
  id="sdk_occ_id1",
  context = {
  "region": "us-south",
  "resource_type": "Cluster",
  "service_name": "Kubernetes Cluster",
  "account_id": "abc123"
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