from datetime import datetime

from external_api import amount_transaction
from filter_by_target import filter_by_description, filter_by_state
from read_data import read_csv_file, read_file_by_pandas
from utils import read_json
from widget import mask_account_card

path_csv_file = "../transactions.csv"
path_xlsx_file = "../transactions_excel.xlsx"

# Чтение файла
print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
print(
    "Выберите необходимый пункт меню:\n"
    "1. Получить информацию о транзакциях из JSON-файла\n"
    "2. Получить информацию о транзакциях из CSV-файла\n"
    "3. Получить информацию о транзакциях из XLSX-файла"
)
user_choice = input("Пользователь: ")
if user_choice == "1":
    transactions = read_json()
elif user_choice == "2":
    transactions = read_csv_file(path_csv_file)
else:
    transactions = read_file_by_pandas(path_xlsx_file)

# Фильтруем транзакции по статусу
print(
    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
)
while True:
    user_choice = input("Пользователь: ")
    user_choice = user_choice.upper()
    if user_choice in ["EXECUTED", "CANCELED", "PENDING"]:
        break
    else:
        print(f'Статус операции "{user_choice}" недоступен.')
transactions = filter_by_state(transactions, user_choice)
print(f'Операции отфильтрованы по статусу: "{user_choice}"')

# Сортировка данных
print("Отсортировать операции по дате? Да/Нет")
user_choice = input("Пользователь: ")
if user_choice.upper() == "ДА":
    print("Отсортировать по возрастанию или по убыванию?")
    user_choice = input("Пользователь: ")
    if user_choice.upper() == "ПО ВОЗРАСТАНИЮ":
        transactions.sort(key=lambda x: x["date"], reverse=False)
    elif user_choice.upper() == "ПО УБЫВАНИЮ":
        transactions.sort(key=lambda x: x["date"], reverse=True)
    else:
        print(f'Указан невернвый тип сортировки: "{user_choice}".\n' f"Данные не были отсортированы!")

# Конвертация валюты
print("Выводить только рублевые тразакции? Да/Нет")
user_choice = input("Пользователь: ")
if user_choice.upper() == "ДА":
    transactions = amount_transaction(transactions)

# Фильтрация по описанию
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
user_choice = input("Пользователь: ")
if user_choice.upper() == "ДА":
    list_of_type_description = []
    cnt = 1
    print("Доступные описания из списка транзакций:")
    for transaction in transactions:
        if "description" in transaction and transaction["description"] not in list_of_type_description:
            list_of_type_description.append(transaction["description"])
    for description in list_of_type_description:
        print(f"{cnt}. {description}")
        cnt += 1
    user_choice = input("Введите слово для фильтрации: ")
    transactions = filter_by_description(transactions, user_choice)

print("Распечатываю итоговый список транзакций...\n")

# Выводим результат
if transactions:
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")
    for transaction in transactions:
        data = datetime.fromisoformat(transaction["date"]).strftime("%d.%m.%Y")
        print(
            f'{data} {transaction["description"]}\n'
            f'{mask_account_card(transaction["from"] if "from" in transaction else None)}'
            f'{" -> " + mask_account_card(transaction["to"])
                if "to" in transaction and transaction["to"] != '' else None}\n'
            f'Сумма: {transaction["amount"] if "amount" in transaction else transaction["operationAmount"]["amount"]} '
            f'{transaction["currency_name"]
                if "currency_name" in transaction else transaction["operationAmount"]["currency"]["name"]}\n'
        )
else:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
