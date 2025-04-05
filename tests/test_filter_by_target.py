import re

from src.filter_by_target import filter_by_description, filter_by_state, count_transaction
from unittest.mock import patch

def test_filter_by_description_ok(date_for_generators):
    target_description = "Перевод организации"
    result = filter_by_description(date_for_generators, target_description)
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

def test_filter_by_state_ok(date_for_generators):
    target_description = "a"
    result = filter_by_state(date_for_generators, target_description)
    assert result == [{'date': '2018-09-12T21:27:25.241689',
  'description': 'Перевод организации',
  'from': 'Visa Platinum 1246377376343588',
  'id': 594226727,
  'operationAmount': {'amount': '67314.70',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'CANCELED',
  'to': 'Счет 14211924144426031657'}]


def test_count_transaction():
    result = count_transaction([{"description":"a"},{"description":"a"},{"description":"b"}], ["b","a"])
    assert result == {'a': 2, 'b': 1}
