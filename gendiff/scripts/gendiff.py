#!/usr/bin/env python

import pathlib
from pathlib import Path

from gendiff.parser import run
from gendiff.file_opener import read_file


def main():
    args = run()
    generate_diff(args.first_file, args.second_file, args.format)


def make_path_file(file_path):
    # Получаем строку, содержащую путь к рабочей директории:
    dir_path = pathlib.Path.cwd()
    if str(dir_path) in file_path:
        return file_path
    else:
        # Объединяем полученную строку с недостающими частями пути
        path = Path(dir_path, file_path)
        return path


def generate_difference_for_key(*args, first_run=False, last_run=False):
    if len(args) != 0 and first_run is False and last_run is False:
        prefix = args[0]
        key = args[1]
        value = str(args[2])
        new_part_str = prefix + key + ': ' + value + ',\n'
    elif first_run:
        new_part_str = '''{\n'''
    elif last_run:
        new_part_str = '\n}'
    return new_part_str


def generate_diff(first_file, second_file, format):
    new_file_path = make_path_file(first_file)
    old_file_path = make_path_file(second_file)
    new_file = read_file(new_file_path)
    old_file = read_file(old_file_path)
    result = generate_difference(new_file, old_file)
    print('RESULT \n' + result)
    return result


def edit_keyword_conversion(value):
    bool_keywords = {'True': 'true',
                     'False': 'false',
                     'None': 'null'}
    if value in set(bool_keywords):
        return bool_keywords[value]
    else:
        return value


def collect_result(total_dict, all_keys):
    result_string = '{\n'
    for key in all_keys:
        new_value = edit_keyword_conversion(str(total_dict[key][0]))
        old_value = edit_keyword_conversion(str(total_dict[key][1]))
        if total_dict[key][0] == total_dict[key][1]:
            result_string += ' ' * 3 + str(key) + ': ' + new_value + ',\n'
        elif total_dict[key][1] is None:
            result_string += ' - ' + str(key) + ': ' + new_value + ',\n'
        elif total_dict[key][0] is None:
            result_string += ' + ' + str(key) + ': ' + old_value + ',\n'
        elif total_dict[key][0] != total_dict[key][1]:
            result_string += ' - ' + str(key) + ': ' + new_value + ',\n'
            result_string += ' + ' + str(key) + ': ' + old_value + ',\n'
    result_string = result_string[:-2] + '\n}'
    return result_string


def generate_difference(new, old):
    all_keys = tuple(sorted(set(new).union(set(old))))
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))
    both_in_files = set(new).intersection(set(old))

    difference_dictionary = {}

    for i in all_keys:
        # if str(type(new[i])).lower() in ["<class 'dict'>"]:
        # generate_difference(new[i], old[i])
        # ключ присутствует в обоих файлах, значение не изменилось
        if i in both_in_files and new[i] == old[i]:
            difference_dictionary[i] = [new[i], old[i]]
        # ключ присутствует в обоих файлах, значения разные
        elif i in both_in_files and new[i] != old[i]:
            difference_dictionary[i] = [new[i], old[i]]
        # ключ присутствует только в новом файле
        elif i in only_in_first_file:
            difference_dictionary[i] = [new[i], None]
        # ключ присутсвует только в старом файле
        elif i in only_in_second_file:
            difference_dictionary[i] = [None, old[i]]

    result = collect_result(difference_dictionary, all_keys)
    return result


def combine_str(key, prefix, value, is_both, prefix_second, value_second):
    temp_str = generate_difference_for_key(prefix, key, value)
    if is_both:
        temp_str += generate_difference_for_key(prefix_second, key,
                                                value_second)
    return temp_str


if __name__ == '__main__':
    main()
