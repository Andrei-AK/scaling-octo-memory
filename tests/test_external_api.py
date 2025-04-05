from unittest.mock import patch, Mock

from src.external_api import amount_transaction


@patch("os.getenv")
def test_amount_transaction_rub(mock_getenv):
    mock_getenv.return_value = "fake_apikey"
    transactions = [{"operationAmount": {"amount": "10.0", "currency": {"code": "RUB"}}}]
    result = amount_transaction(transactions)
    assert result == transactions


def test_amount_transaction_conversion():
    transactions = [{"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}]
    with patch("os.getenv", return_value="apikey"):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": 75.5,
            "success": True
        }
        with patch("requests.request", return_value=mock_response) as req:
            result = amount_transaction(transactions)
    assert result == [{'operationAmount': {'amount': 75.5, 'currency': {'code': 'RUB'}}}]


@patch("requests.request")
def test_keep_rub_transaction(mock_request):
    test_transactions = [{
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "RUB"}
        }
    }]
    result = amount_transaction(test_transactions)
    mock_request.assert_not_called()
    assert result == test_transactions

def test_empty_transaction():
    result = amount_transaction([None])
    assert result == []
