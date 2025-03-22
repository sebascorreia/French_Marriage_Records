from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient
from config import ACCOUNT_NAME
import json
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plt
def get_blob_service_client()->BlobServiceClient:
    credential = DefaultAzureCredential()
    return BlobServiceClient(
        account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net/",
        credential= credential
    )
def get_container_client(container_name:str):
    blob_service = get_blob_service_client()
    return blob_service.get_container_client(container_name)

def get_blob_client(container_name:str,blob_name:str):
    blob_service = get_blob_service_client()
    return blob_service.get_blob_client(container_name,blob_name)
def print_blob(blob_client):
    blob_data= get_blob_data(blob_client)
    if blob_client.blob_name.endswith('.json'):
        print_json_blob(blob_data)
    elif blob_client.blob_name.endswith('.png'):
        plot_img_blob(blob_data)
    elif blob_client.blob_name.endswith('.txt'):
        print_text_blob(blob_data)
    else:
        print("Blob type not supported")

def get_blob_data(blob_client):
    return blob_client.download_blob().readall()
def print_json_blob(blob_data):
    try:
        data = json.loads(blob_data.decode("utf-8"))
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Failed to read {blob_data.name}: {e}")

def print_text_blob(blob_data):
    try:
        print(blob_data.decode("utf-8"))
    except Exception as e:
        print(f"Failed to read {blob_data.name}: {e}")

def plot_img_blob(blob_data):
    try:
        image=Image.open(BytesIO(blob_data))
        plt.imshow(image)
        plt.axis('off')
        plt.title(blob_data.name)
        plt.show()
    except Exception as e:
        print(f"Failed to read {blob_data.name}: {e}")








