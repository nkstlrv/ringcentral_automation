import os
from dotenv import load_dotenv
import requests
import json
from utils import format_response_json

load_dotenv()


# RingCentral API Credentials
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
EXTENSION_ID = os.getenv("EXTENSION_ID")
TOKEN = os.getenv("TOKEN")


def get_calls_list():
    calls_list_url = (f"https://platform.ringcentral.com/restapi/v1.0/account/"
                      f"{ACCOUNT_ID}/extension/{EXTENSION_ID}/call-log")

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {TOKEN}",
        "content-type": "application/json",
    }

    response: dict = requests.get(url=calls_list_url, headers=headers).json()

    # formatting data to return only necessary information about calls
    data: list[dict] = format_response_json(response_data=response)
    return data


if __name__ == "__main__":
    print(get_calls_list())
