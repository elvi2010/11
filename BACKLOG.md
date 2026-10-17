"""Загрузка и сохранение задач в текстовый файл."""


def load_collection(file_name):
    """Загружает задачи из txt-файла; если его нет, возвращает пустой список."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_collection(collection, file_name):
    """Сохраняет задачи в txt-файл. Ошибки ввода-вывода передаются вызывающему коду."""
    with open(file_name, "w", encoding="utf-8") as file:
        for task in collection:
            file.write(f"{task}\n")
