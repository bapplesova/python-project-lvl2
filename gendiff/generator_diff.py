#!/usr/bin/env python

from gendiff.parser import open_file
from gendiff.parser import read_file
from gendiff.parser import get_file_type
from gendiff.formatters.format_chooser import choose_format


def generate_diff(first_file, second_file, format='stylish'):
    # определяем тип файла
    new_file_type = get_file_type(first_file)
    old_file_type = get_file_type(second_file)
    # считываем файлы
    first_file_data = open_file(first_file)
    second_file_data = open_file(second_file)
    # parsing
    new_file = read_file(first_file_data, new_file_type)
    old_file = read_file(second_file_data, old_file_type)
    # сравниваем 2 файла, формируем словарь с отличиями
    dictionary_difference = generate_diff_dict(new_file, old_file)

    required_format = str(format).lower()
    # выводим отличия по заданному виду
    result = choose_format(dictionary_difference, required_format)
    print(result)
    return result


def generate_diff_dict(new_file, old_file):
    diff_dict = {}
    keys_new = new_file.keys()
    keys_old = old_file.keys()

    added = keys_old - keys_new
    for key in added:
        diff_dict[key] = ['added', get_value(old_file[key])]

    removed = keys_new - keys_old
    for key in removed:
        diff_dict[key] = ['removed', get_value(new_file[key])]

    both = keys_new & keys_old
    for key in both:
        if isinstance(new_file[key], dict) and isinstance(old_file[key], dict):
            diff_dict[key] = generate_diff_dict(new_file[key], old_file[key])
        elif new_file[key] == old_file[key]:
            diff_dict[key] = ['unchanged', new_file[key]]
        else:
            diff_dict[key] = ['changed', get_value(new_file[key]),
                              get_value(old_file[key])]
    return diff_dict


def get_value(value):
    if isinstance(value, dict):
        return generate_diff_dict(value, value)
    else:
        return value
