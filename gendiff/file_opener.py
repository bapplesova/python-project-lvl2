import pathlib
from pathlib import Path


def make_path_file(file_path):
    # Получаем строку, содержащую путь к рабочей директории
    dir_path = pathlib.Path.cwd()
    if str(dir_path) in file_path:
        return file_path
    else:
        # Объединяем полученную строку с недостающими частями пути
        path = Path(dir_path, file_path)
        return path
