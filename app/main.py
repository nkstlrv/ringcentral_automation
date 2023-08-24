import os
from dotenv import load_dotenv
import requests
import logging
from utils import format_calls_list_response_json, format_sms_list_response_json

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# RingCentral API Credentials
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
EXTENSION_ID = os.getenv("EXTENSION_ID")
TOKEN = os.getenv("TOKEN")

AUTH_HEADERS = {
    "accept": "application/json",
    "authorization": f"Bearer {TOKEN}",
    "content-type": "application/json",
}


def get_calls_list() -> list[dict] | bool:
    calls_list_url = (
        f"https://platform.ringcentral.com/restapi/v1.0/account/"
        f"{ACCOUNT_ID}/extension/{EXTENSION_ID}/call-log"
    )

    response = requests.get(url=calls_list_url, headers=AUTH_HEADERS)

    try:
        response.raise_for_status()  # checking whether request was successful
    except requests.exceptions.HTTPError as ex:
        logging.error(ex)
        return False

    # formatting data to return only necessary information about calls
    data: list[dict] = format_calls_list_response_json(
        response_calls_data=response.json()
    )
    return data


def get_recording(recording_id: str) -> list | bool:
    recording_base_url = f"https://platform.ringcentral.com/restapi/v1.0/account/{ACCOUNT_ID}/recording/{recording_id}"

    response = requests.get(url=recording_base_url, headers=AUTH_HEADERS)

    try:
        response.raise_for_status()  # checking whether request was successful
    except requests.exceptions.HTTPError as ex:
        logging.error(ex)
        return False

    data: dict = response.json()
    return data


def get_sms_list() -> list[dict] | bool:
    sms_base_url = (
        f"https://platform.ringcentral.com/restapi/v1.0/"
        f"account/{ACCOUNT_ID}/extension/{EXTENSION_ID}/message-store"
    )

    response = requests.get(url=sms_base_url, headers=AUTH_HEADERS)

    try:
        response.raise_for_status()  # checking whether request was successful
    except requests.exceptions.HTTPError as ex:
        logging.error(ex)
        return False

    data: list[dict] = format_sms_list_response_json(response_sms_data=response.json())
    return data


if __name__ == "__main__":
    print(get_calls_list())
    print(get_sms_list())
    print(get_recording("2167092738043"))
