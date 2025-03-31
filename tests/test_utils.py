import json
from unittest.mock import patch

from src.utils import read_json


def test_read_json_correct_path():
    file_path = "C:/Users/ggrea/Desktop/ST PY/pj/data/operations.json"
    with open(file_path, "r", encoding="UTF-8") as f:
        test_data = f.read()
        test_result = json.loads(test_data)
    result = read_json()
    assert result == test_result


def test_read_json_wrong_path():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json()
    assert result == []


def test_read_json_wrong_json():
    with patch("builtins.open", return_data=""):
        with patch("json.loads", side_effect=json.JSONDecodeError("msg", "doc", 0)):
            result = read_json()

    assert result == []
