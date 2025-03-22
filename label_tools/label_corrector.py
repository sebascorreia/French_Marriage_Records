from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
from azure_utils import connection
from config import CONTAINER_NAME, IMG_PREFIX
import json

container_client = connection.get_container_client(CONTAINER_NAME)

blob_list= container_client.list_blobs(name_starts_with=IMG_PREFIX)

for blob in blob_list:
    if "labels" in blob.name:
        print(f"Reading: {blob.name}")
        blob_client = container_client.get_blob_client(blob=blob.name)
        connection.print_blob(blob_client)




