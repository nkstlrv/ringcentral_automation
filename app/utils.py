import json
from data.data_dict import data_dict

def prepare_json_for_production(input_data: dict):
    records: list[dict] = input_data.get("records")

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
                    "called_to": call["to"], # potentially empty
                    "called_from": call["from"],  
                    "recording_link": f"https://app.ringcentral.com/phone/recordings/{call['recording']['id']}",
                    "call_summary": call.get("reasonDescription"), # potentially empty
                }
            )

        return result
    return False

if __name__ == "__main__":

    prepared_data = prepare_json_for_production(data_dict)

    with open("data/production_data.json", "w") as f:
        json.dump(prepared_data, f)
    
