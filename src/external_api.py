import os

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("APIKEY")
headers = {"apikey": apikey}


def amount_transaction(transaction):
    """Получение/конвертация суммы транзакции в RUB"""
    if transaction:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            response = requests.request(
                "GET",
                f"https://api.apilayer.com/exchangerates_data/convert?"
                f"to={'RUB'}&"
                f"from={transaction['operationAmount']['currency']['code']}&"
                f"amount={transaction['operationAmount']['amount']}",
                headers=headers,
            )
            print(response)
            status_code = response.status_code
            print(status_code, type(status_code))
            if status_code == 200:
                converted_transaction = response.json()
                return float(converted_transaction["result"])
            else:
                print(f"Status code: {response.status_code}")
        else:
            return float(transaction["operationAmount"]["amount"])
