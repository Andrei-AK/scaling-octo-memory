import pytest
from src.widget import *

# 1-card number, 2-account number, 0-fail input
@pytest.mark.parametrize('user_data, result',
                         [('Maestro 1596837868705199', 1),
                         ('Счет 64686473678894779589', 2),
                         ('MasterCard 754664158300734726758', 0),
                         ('Счет 35383033474447895560', 2),
                         ('Visa Classic 06831982476737658', 0),
                         ('', 0),
                         ('Visa Gold 59994142284263*53', 0),
                         ('Счет 73654108430135874305', 2)
                          ])
def test_check_correct_data(user_data, result):
    assert check_correct_data(user_data) == result


@pytest.mark.parametrize('date_valid, returned_date',
                         [('2024-03-11T02:26:18.671407', '11.03.2024'),
                          ('2022-01-12T02:26:18.671407', '12.01.2022')])
def test_date_valid(date_valid, returned_date):
    assert get_date(date_valid) == returned_date
