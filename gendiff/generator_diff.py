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
    new_file = read_file(first_file_data, new_file_type)
    old_file = read_file(second_file_data, old_file_type)
    # сравниваем 2 файла, формируем словарь с отличиями
    dictionary_difference = generate_difference(new_file, old_file)
    required_format = str(format).lower()
    # выводим отличия по заданному виду
    result = choose_format(dictionary_difference, required_format)
    print(result)
    return result


def find_files_difference(analyzed_file, only_in_one_file, status):
    temp_dict = {}
    for i in only_in_one_file:
        if isinstance(analyzed_file[i], dict):
            temp_dict[i] = (status, generate_difference(analyzed_file[i],
                                                        analyzed_file[i]))
        else:
            temp_dict[i] = (status, analyzed_file[i])
    return temp_dict


def find_files_intersection(new_file, old_file):
    temp_dict = {}

    both_in_files = set(new_file).intersection(set(old_file))

    for i in both_in_files:
        # ключ есть в обоих файлах, оба значения - вложенные словари
        if isinstance(new_file[i], dict) and isinstance(old_file[i], dict):
            temp_dict[i] = generate_difference(new_file[i], old_file[i])
        # ключ присутствует в обоих файлах, значение не изменилось
        elif new_file[i] == old_file[i]:
            temp_dict[i] = ["unchanged", new_file[i]]
        # ключ присутствует в обоих файлах, значения разные
        elif new_file[i] != old_file[i]:
            value1, value2 = make_temp_dict(new_file[i], old_file[i])
            temp_dict[i] = ["edited", value1, value2]
    return temp_dict


def generate_difference(new, old):
    # формируем множества из ключей файлов
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))

    total_diff_dictionary = find_files_difference(new,
                                                  only_in_first_file,
                                                  'removed')
    total_diff_dictionary.update(find_files_difference(old,
                                                       only_in_second_file,
                                                       'added'))
    total_diff_dictionary.update(find_files_intersection(new, old))
    return total_diff_dictionary


def make_temp_dict(new_file_value, old_file_value):
    if isinstance(new_file_value, dict):
        value1 = generate_difference(new_file_value, new_file_value)
        value2 = old_file_value
    elif isinstance(old_file_value, dict):
        value1 = new_file_value
        value2 = generate_difference(old_file_value, old_file_value)
    else:
        value1 = new_file_value
        value2 = old_file_value
    return value1, value2
