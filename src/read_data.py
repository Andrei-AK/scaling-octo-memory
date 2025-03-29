import csv
import logging

import pandas as pd

file_handler = logging.FileHandler(filename="../logs/read_data.log", mode="w", encoding="UTF-8")
logging.basicConfig(level="DEBUG", encoding="UTF-8", handlers=[file_handler])
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger = logging.getLogger()
logger.addHandler(file_handler)

path_csv_file = "C:/Users/ggrea/Desktop/ST PY/pj/transactions.csv"
path_xlsx_file = "C:/Users/ggrea/Desktop/ST PY/pj/transactions_excel.xlsx"


def read_csv_file(path_file):
    """Функция считывает csv и преобразует в список словарей"""
    logger.debug(f"Функция {read_csv_file.__name__} начала работу")
    try:
        with open(path_file, encoding="UTF-8") as f:
            list_from_csv = list(csv.DictReader(f, delimiter=";"))
        logger.debug(f"Функция {read_csv_file.__name__} успешно закончила работу")
        return list_from_csv
    except FileNotFoundError:
        logger.error(f"Файл {path_file} не найден")
        return []
    except ValueError:
        logger.error(f"Формат файла {path_file} не .csv")
        return []


def read_file_by_pandas(path_file):
    """Читаем файл excel с помощью pandas, возвращаем список словарей"""
    logger.debug(f"Функция {read_csv_file.__name__} начала работу")
    try:
        data = pd.read_excel(path_file)
        new_list = data.to_dict(orient="records")
        logger.debug(f"Функция {read_csv_file.__name__} успешно закончила работу")
        return new_list
    except FileNotFoundError:
        logger.error(f"Файл {path_file} не найден")
        return []
    except ValueError:
        logger.error(f"Формат файла {path_file} не .csv")
        return []
