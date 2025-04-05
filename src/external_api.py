import os

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("APIKEY")
headers = {"apikey": apikey}


def amount_transaction(transactions):
    """Получение/конвертация суммы транзакции в RUB"""
    converted_transactions = []
    for transaction in transactions:
        if transaction:
            if "currency_code" in transaction:
                type_of_dict = 1
                code = transaction["currency_code"]
                summ = transaction["amount"]
            else:
                type_of_dict = 2
                code = transaction["operationAmount"]["currency"]["code"]
                summ = transaction["operationAmount"]["amount"]
            if code != "RUB":
                response = requests.request(
                    "GET",
                    f"https://api.apilayer.com/exchangerates_data/convert?"
                    f"to={'RUB'}&"
                    f"from={code}&"
                    f"amount={summ}",
                    headers=headers,
                )
                status_code = response.status_code
                if status_code == 200:
                    converted_transaction = response.json()
                    if type_of_dict == 1:
                        transaction["currency_code"] = "RUB"
                        transaction["amount"] = float(converted_transaction["result"])
                        converted_transactions.append(transaction)
                    elif type_of_dict == 2:
                        transaction["operationAmount"]["currency"]["code"] = "RUB"
                        transaction["operationAmount"]["amount"] = float(converted_transaction["result"])
                        converted_transactions.append(transaction)
                else:
                    print(f"Status code: {response.status_code}")
            else:
                converted_transactions.append(transaction)
    return converted_transactions
