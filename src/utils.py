import json
import logging

logging.basicConfig(encoding="UTF-8")
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json():
    """Чтение файла формата json"""
    file_path = "C:/Users/ggrea/Desktop/ST PY/pj/data/operations.json"
    logger.debug("Функция начала работу")
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            logger.debug("Файл открылся успешно")
            file_data = f.read()
            if file_data:
                json_data = json.loads(file_data)
                logger.debug("JSON успешно прочитан")
                return json_data
            else:
                logger.error("Файл не содержит список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл по пути {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Невозможно декодировать (преобразовать) JSON-данные.")
        return []
