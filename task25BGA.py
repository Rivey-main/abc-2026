#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.

import os
import pickle

# Имя файла для сохранения по умолчанию
SAVE_FILE = "pole_chudes_save.pkl"


def save_game(game_state, filename=SAVE_FILE):
    """Сериализует и сохраняет состояние игры в файл."""
    try:
        with open(filename, "wb") as file:
            pickle.dump(game_state, file)
        print(f" Игра успешно сохранена в файл '{filename}'!")
        return True
    except Exception as e:
        print(f" Ошибка при сохранении игры: {e}")
        return False


def load_game(filename=SAVE_FILE):
    """Загружает и десериализует состояние игры из файла."""
    if not os.path.exists(filename):
        print(f" Файл сохранения '{filename}' не найден.")
        return None

    try:
        with open(filename, "rb") as file:
            game_state = pickle.load(file)
        print(f" Игра успешно загружена из файла '{filename}'!")
        return game_state
    except Exception as e:
        print(f" Ошибка при загрузке игры: {e}")
        return None

