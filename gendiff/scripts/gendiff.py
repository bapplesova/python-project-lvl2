#!/usr/bin/env python

import json

from gendiff.parser import run
from gendiff.file_opener import read_file
from gendiff.file_opener import make_path_file
from gendiff.formatters.stylish import collect_stylish_result
from gendiff.formatters.plain import collect_plain_result
from gendiff.formatters.json import collect_json_result


def main():
    args = run()
    generate_diff(args.first_file, args.second_file, args.format)


def generate_diff(first_file, second_file, *format):
    indent = 1
    # собираем путь до файла
    new_file_path = make_path_file(first_file)
    old_file_path = make_path_file(second_file)
    # считываем файлы
    new_file = read_file(new_file_path)
    old_file = read_file(old_file_path)
    # сравниваем 2 файла, формируем словарь с отличиями
    dictionary_difference = generate_difference(new_file, old_file)
    # выводим отличия по заданному виду
    required_format = str(format[0]).lower()
    print('FORMAT', format, type(format), required_format)
    if required_format == 'plain':
        result = collect_plain_result(dictionary_difference, '')
    elif required_format == 'json':
        result = collect_json_result(dictionary_difference)
        json.dumps(result)
    else:
        result = collect_stylish_result(dictionary_difference, indent)
    print('RESULT \n', result)
    return result


def find_files_difference(analyzed_file, only_in_one_file, prefix):
    temp_dict = {}
    for i in only_in_one_file:
        if isinstance(analyzed_file[i], dict):
            temp_dict[i] = [prefix, generate_difference(analyzed_file[i],
                                                        analyzed_file[i])]
        else:
            temp_dict[i] = [prefix, analyzed_file[i]]
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
            temp_dict[i] = ["   ", new_file[i]]
        # ключ присутствует в обоих файлах, значения разные
        elif new_file[i] != old_file[i] and isinstance(new_file[i], dict):
            temp_dict[i] = [" ", generate_difference(new_file[i], new_file[i]),
                            old_file[i]]
        elif new_file[i] != old_file[i] and isinstance(old_file[i], dict):
            temp_dict[i] = [" ", new_file[i],
                            generate_difference(old_file[i], old_file[i])]
        else:
            temp_dict[i] = [" ", new_file[i], old_file[i]]
    return temp_dict


def generate_difference(new, old):
    # словарь для хранения отличий
    total_diff_dictionary = {}

    # формируем множества из ключей файлов
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))

    total_diff_dictionary = find_files_difference(new,
                                                  only_in_first_file, ' - ')
    total_diff_dictionary.update(find_files_difference(old,
                                                       only_in_second_file,
                                                       ' + '))
    total_diff_dictionary.update(find_files_intersection(new, old))
    return total_diff_dictionary


if __name__ == '__main__':
    main()
