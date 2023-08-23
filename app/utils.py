import json
from data_dict import data_dict

def prepare_json_for_production(data: dict):
    records: list[dict] = data.get("records")

    if records:
        result = list()

        for call in records: 
            result.append(
                {
                    "ringcentral_link": f"https://app.ringcentral.com/phone/recent/all/{call['id']}",
                    "call_start_time": call["startTime"],
                    "call_duration_time_seconds": call["duration"],
                    "call_type": call["type"],
                    "call_direction": call["direction"],
                    "call_action": call["action"],
                    "call_result": call["result"],
                    "called_to": call["to"].get("extensionId"),
                    "called_from": call["from"]["phoneNumber"],  
                    "recording_link": f"https://app.ringcentral.com/phone/recordings/{call['recording']['id']}",
                    "call_summary": call.get("reasonDescription", "No Description"),
                }
            )

        return result
    else:
        return False

if __name__ == "__main__":
    print(prepare_json_for_production(data_dict))
