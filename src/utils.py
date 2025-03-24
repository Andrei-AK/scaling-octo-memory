import json

file_path = "C:/Users/ggrea/Desktop/ST PY/pj/data/operations.json"


def read_json():
    """Чтение файла формата json"""
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            file_data = f.read()
            if file_data:
                json_data = json.loads(file_data)
                return json_data
            else:
                print("Файл не содержит список.")
                return []
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Невозможно декодировать (преобразовать) JSON-данные.")
        return []
