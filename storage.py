"""Вспомогательные функции приложения."""


def check_confirm(message="Вы уверены?"):
    """Запрашивает подтверждение действия."""
    while True:
        answer = input(f"{message} (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Введите «да» или «нет».")
