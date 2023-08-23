import os
from dotenv import load_dotenv
import requests

load_dotenv()


# RingCentral API Credentials

ACCOUNT_ID = os.getenv("ACCOUNT_ID")
EXTENSION_ID = os.getenv("EXTENSION_ID")
# CLIENT_ID = os.getenv("CLIENT_ID")
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN = os.getenv("TOKEN")
# EXTENSION = os.getenv("EXTENSION")

BASE_URl = f"https://platform.ringcentral.com/restapi/v1.0/account/{ACCOUNT_ID}/extension/{EXTENSION_ID}/call-log"

headers = {
    "accept": "application/json",
    "authorization": f"Bearer {TOKEN}",
    "content-type": "application/json",
}

response = requests.get(url=BASE_URl, headers=headers)


data = response
print(data.text)
