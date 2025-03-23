from unittest.mock import patch

from src.external_api import amount_transaction


@patch("os.getenv")
def test_amount_transaction_rub(mock_getenv):
    mock_getenv.return_value = "fake_apikey"
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    result = amount_transaction(transaction)
    assert result == 100.0


@patch("requests.request")
@patch("os.getenv")
def test_amount_transaction_conversion(mock_getenv, mock_response):
    mock_getenv.return_value = "fake_apikey"
    mock_response.return_value.json.return_value = {"result": 75.5}
    mock_response.return_value.status_code = 200
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = amount_transaction(transaction)
    print(result)
    assert result == 75.5


@patch("requests.request")
@patch("os.getenv")
def test_amount_transaction_failed_api(mock_getenv, mock_response):
    mock_getenv.return_value = "fake_apikey"
    mock_response.return_value.status_code = 500
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = amount_transaction(transaction)
    assert result is None
