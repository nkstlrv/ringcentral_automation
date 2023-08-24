import json
from data.dev_calls_data_dict import data_dict


def format_response_json(response_data: dict):
    """

    returns only necessary information,
    extracted from raw JSON that is being returned by RingCentral

    """
    records: list[dict] = response_data.get("records")

    if records:
        result = list()

        for call in records:
            result.append(
                {
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


if __name__ == "__main__":
    prepared_data = format_response_json(data_dict)

    with open("data/production_calls_list.json", "w") as f:
        json.dump(prepared_data, f)
