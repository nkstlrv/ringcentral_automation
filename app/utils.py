import json
from data.dev_calls_data_dict import calls_dict
from data.dev_sms_data_dict import sms_dict


def format_calls_list_response_json(response_calls_data: dict):
    """

    returns only necessary CALL information,
    extracted from raw JSON that is being returned by RingCentral

    """
    records: list[dict] = response_calls_data.get("records")

    if records:
        result = list()

        for call in records:
            result.append(
                {
                    "call_id": call.get("id"),
                    "ringcentral_link": f"https://app.ringcentral.com/phone/recent/all/{call.get('id')}",
                    "start_time": call.get("startTime"),
                    "duration_time_seconds": call.get("duration"),
                    "type": call.get("type"),
                    "direction": call.get("direction"),
                    "action": call.get("action"),
                    "result": call.get("result"),
                    "to": call.get("to"),
                    "from": call.get("from"),
                    # potential exception may occur
                    "recording_link": f"https://app.ringcentral.com/phone/recordings/{call['recording']['id']}",
                    "summary": call.get("reasonDescription"),
                }
            )

        return result
    return False


def format_sms_list_response_json(response_sms_data: dict):
    """

        returns only necessary SMS information,
        extracted from raw JSON that is being returned by RingCentral

    """
    records: list[dict] = response_sms_data.get("records")

    if records:
        result = list()

        for sms in records:
            result.append(
                {
                    "sms_id": sms.get("id"),
                    "to": sms.get("to"),
                    "from": sms.get("from"),
                    "type": sms.get("type"),
                    "send_time": sms.get("creationTime"),
                    "last_modified_time": sms.get("lastModifiedTime"),
                    "read_status": sms.get("readStatus"),
                    "priority": sms.get("priority"),
                    "direction": sms.get("direction"),
                    "subject": sms.get("subject"),
                    "status": sms.get("messageStatus"),
                    "availability": sms.get("availability"),
                    "attachments": sms.get("attachments")


                }
            )

        return result
    return False


if __name__ == "__main__":
    call_data = format_calls_list_response_json(calls_dict)
    with open("data/production_calls_list.json", "w") as f:
        json.dump(call_data, f)

    sms_data = format_sms_list_response_json(sms_dict)
    with open("data/production_sms_list.json", "w") as f:
        json.dump(sms_data, f)
