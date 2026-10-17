"""Основная логика Task Manager."""

from pathlib import Path

from storage import load_collection, save_collection
from utils import check_confirm
from view import show_collection, show_menu


def _save_changes(collection, file_name):
    """Сохраняет список и возвращает False при ошибке ввода-вывода."""
    try:
        save_collection(collection, file_name)
    except OSError as error:
        print(f"Не удалось сохранить задачи: {error}")
        return False
    return True


def add_task(collection, file_name):
    """Добавляет новую задачу и откатывает изменение, если сохранить не удалось."""
    task = input("Введите название и описание задачи: ").strip()
    if not task:
        print("Задача не может быть пустой.")
        return

    collection.append(task)
    if not _save_changes(collection, file_name):
        collection.pop()
        return
    print("Задача успешно добавлена.")


def edit_task(collection, file_name):
    """Редактирует выбранную задачу."""
    if not collection:
        print("Нет задач для редактирования.")
        return

    show_collection(collection)
    try:
        number = int(input("Введите номер задачи для редактирования: "))
    except ValueError:
        print("Введите номер числом.")
        return

    if number < 1 or number > len(collection):
        print("Задачи с таким номером нет.")
        return

    new_task = input("Введите новое название и описание задачи: ").strip()
    if not new_task:
        print("Задача не может быть пустой.")
        return

    old_task = collection[number - 1]
    collection[number - 1] = new_task
    if not _save_changes(collection, file_name):
        collection[number - 1] = old_task
        return
    print("Задача успешно изменена.")


def delete_task(collection, file_name):
    """Удаляет задачу после подтверждения пользователя."""
    if not collection:
        print("Нет задач для удаления.")
        return

    show_collection(collection)
    try:
        number = int(input("Введите номер задачи для удаления: "))
    except ValueError:
        print("Введите номер числом.")
        return

    if number < 1 or number > len(collection):
        print("Задачи с таким номером нет.")
        return

    task = collection[number - 1]
    if not check_confirm(f"Удалить задачу «{task}»?"):
        print("Удаление отменено.")
        return

    removed_task = collection.pop(number - 1)
    if not _save_changes(collection, file_name):
        collection.insert(number - 1, removed_task)
        return
    print("Задача успешно удалена.")


def run_app(file_name=None):
    """Запускает главный цикл; по умолчанию использует saves.txt рядом с проектом."""
    if file_name is None:
        file_name = str(Path(__file__).resolve().parent / "saves.txt")

    try:
        collection = load_collection(file_name)
    except OSError as error:
        print(f"Не удалось загрузить задачи: {error}")
        collection = []

    while True:
        show_menu()
        choice = input("Введите команду: ").strip()

        if choice == "1":
            show_collection(collection)
        elif choice == "2":
            add_task(collection, file_name)
        elif choice == "3":
            edit_task(collection, file_name)
        elif choice == "4":
            delete_task(collection, file_name)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверная команда. Выберите пункт от 1 до 5.")
