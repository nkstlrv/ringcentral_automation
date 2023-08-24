"""













DOES        NOT             WORK




























"""


import os
from dotenv import load_dotenv
from ringcentral import SDK

load_dotenv()


# RingCentral API Credentials
SERVER_URL = "https://platform.ringcentral.com"

ACCOUNT_ID = os.getenv("ACCOUNT_ID")
EXTENSION_ID = os.getenv("EXTENSION_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN = os.getenv("TOKEN")
EXTENSION = os.getenv("EXTENSION")


queryParams = {
    #'page': 000,
    #'perPage': 000
}

# setting up RingCentral SDK
rcsdk = SDK(CLIENT_ID, CLIENT_SECRET, SERVER_URL)
platform = rcsdk.platform()

platform.login(USERNAME, EXTENSION, PASSWORD)
platform.auth()


# Get List of Calls
r = platform.get(f"/restapi/v1.0/account/{ACCOUNT_ID}/call-log", queryParams)


print(r)
