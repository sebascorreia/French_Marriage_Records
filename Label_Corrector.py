from azure.storage.blob import BlobServiceClient, BlobClient
from azure.identity import DefaultAzureCredential
import json
ACCOUNT_NAME = "frenchmarriagerecords"
container_name="frenchmarriagerecordsblob"
prefix = "frenchmarriagerecordsblob/m-popp_datasets/handwritten/"

token_credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net/", credential=token_credential)
container_client = blob_service_client.get_container_client(container=container_name)


blob_list= container_client.list_blobs(name_starts_with=prefix)
for blob in blob_list:
    if blob.name.endswith(".labels.json"):
        print(f"Reading: {blob.name}")
        blob_client = container_client.get_blob_client(blob=blob.name)
        blob_data = blob_client.download_blob().readall()

        try:
            data = json.loads(blob_data.decode("utf-8"))
            print(json.dumps(data, indent=2))
        except Exception as e:
            print(f"Failed to read {blob.name}: {e}")

