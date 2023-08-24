import os
from dotenv import load_dotenv
import requests
import logging
from utils import format_response_json

load_dotenv()

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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

    response = requests.get(url=calls_list_url, headers=headers)

    try:
        response.raise_for_status()  # checking whether request was successful
    except requests.exceptions.HTTPError as ex:
        logging.error(ex)
        return False

    # formatting data to return only necessary information about calls
    data: list[dict] = format_response_json(response_data=response.json())
    return data


def get_recording(recording_id: str):
    base_url = f"https://platform.devtest.ringcentral.com/restapi/v1.0/account/{ACCOUNT_ID}/recording/{recording_id}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {TOKEN}",
        "content-type": "application/json",
    }

    response = requests.get(url=base_url, headers=headers)

    try:
        response.raise_for_status()  # checking whether request was successful
    except requests.exceptions.HTTPError as ex:
        logging.error(ex)
        return False

    data: dict = response.json()
    return data


if __name__ == "__main__":
    print(get_calls_list())
    print(get_recording("2167092738043"))
