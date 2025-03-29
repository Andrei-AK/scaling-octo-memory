from unittest.mock import patch

import pandas as pd

from src.read_data import read_csv_file, read_file_by_pandas


def test_read_csv_file_ok():
    with patch("builtins.open", return_data="key;value\n1;2") as f:
        with patch("csv.DictReader", f) as mock_result:
            result = read_csv_file("mock_file.csv")
    assert result == list(mock_result.return_value)


def test_read_csv_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_csv_file("wrong_path")
    assert result == []


def test_read_csv_file_value_error():
    with patch("builtins.open", side_effect=ValueError):
        result = read_csv_file("wrong_file")
    assert result == []


def test_read_file_by_pandas_ok():
    file_data = {"key": ["value1", "value2"]}
    mock_pd = pd.DataFrame(file_data)
    with patch("pandas.read_excel", return_value=mock_pd) as f:
        result = read_file_by_pandas("file")
    assert result == f.return_value.to_dict(orient="records")


def test_read_file_by_pandas_not_found():
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_file_by_pandas("file")
    assert result == []


def test_read_file_by_pandas_val_err():
    with patch("pandas.read_excel", side_effect=ValueError):
        result = read_file_by_pandas("file")
    assert result == []
