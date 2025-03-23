import json
from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_json_correct_path():
    file_path = "C:/Users/ggrea/Desktop/ST PY/pj/data/operations.json"
    with open(file_path, "r", encoding="UTF-8") as f:
        test_data = f.read()
        test_result = json.loads(test_data)
    result = read_json()
    assert result == test_result


@patch("src.utils.open", side_effect=FileNotFoundError)
def test_read_json_wrong_path(mock_file):
    result = read_json()
    assert result == []


@patch("src.utils.open", new_callable=mock_open, read_data="wrong json")
def test_read_json_wrong_json(mock_file):
    result = read_json()
    assert result == []
