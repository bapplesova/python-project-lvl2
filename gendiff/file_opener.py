#!/usr/bin/env python
import json
import yaml
from yaml.loader import SafeLoader
import pathlib
from pathlib import Path


def read_file(file_path):
    file_type = get_file_type(file_path)
    if file_type == 'json':
        file_data = json.load(open(file_path))
    elif file_type in 'yaml':
        file_data = yaml.load(open(file_path), Loader=SafeLoader)
    return file_data


def get_file_type(file_path):
    file_extension = str(file_path).split('.')
    if file_extension[-1] == 'json':
        return 'json'
    elif file_extension[-1] in ('yaml', 'yml'):
        return 'yaml'
    else:
        raise Exception('Invalid file format.')


def make_path_file(file_path):
    # Получаем строку, содержащую путь к рабочей директории
    dir_path = pathlib.Path.cwd()
    if str(dir_path) in file_path:
        return file_path
    else:
        # Объединяем полученную строку с недостающими частями пути
        path = Path(dir_path, file_path)
        return path
