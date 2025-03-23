import json
import os


def read_json():
    """Чтение файла формата json"""
    file_path = "../data/operations.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="UTF-8") as f:
            file_data = f.read()
            if file_data:
                json_data = json.loads(file_data)
                if type(json_data) is list:
                    return json_data
    return []
