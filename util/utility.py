import json
import re


def remove_code_fences(text):
    code = re.sub(r"```json", "", text)
    code = re.sub(r"```", "", code)
    return code

def ai_response_to_json(response_string=""):
    try:
        cleaned = remove_code_fences(response_string)
        parsed_json = json.loads(cleaned)
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None