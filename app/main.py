import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


# RingCentral API Credentials
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
EXTENSION_ID = os.getenv("EXTENSION_ID")
TOKEN = os.getenv("TOKEN")


def get_calls_list():
    calls_list_url = f"https://platform.ringcentral.com/restapi/v1.0/account/{ACCOUNT_ID}/extension/{EXTENSION_ID}/call-log"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {TOKEN}",
        "content-type": "application/json",
    }

    response = requests.get(url=calls_list_url, headers=headers)

    data = response.json()

    print(data)


if __name__ == "__main__":
    get_calls_list()
