#!/usr/bin/env python

import json
import pathlib
from pathlib import Path

from gendiff.parser import run


def main():
    args = run()
    diff_json = generate_diff(args.first_file, args.second_file)


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


def generate_diff(new_f, old_f):
    new_file = make_path_file(new_f)
    old_file = make_path_file(old_f)
    new = json.load(open(new_file))
    old = json.load(open(old_file))
    result = generate_difference(new, old)
    return result


def edit_keyword_conversion(value):
    bool_keywords = {'True': 'true',
                     'False': 'false',
                     'None': 'null'}
    if value in set(bool_keywords):
        return bool_keywords[value]
    else:
        return value


def generate_difference(new, old):
    all_keys = tuple(sorted(set(new).union(set(old))))
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))
    both_in_files = set(new).intersection(set(old))

    value_second = ''
    diff_json_str = generate_difference_for_key(first_run=True)

    for i in all_keys:
        # ключ присутствует в обоих файлах
        if i in both_in_files and new[i] == old[i]:
            # значение не изменилось
            is_both = False
            prefix = ' ' * 3
            value = edit_keyword_conversion(str(new[i]))
            # значения разные
        elif i in both_in_files and new[i] != old[i]:
            is_both = True
            prefix = ' - '
            prefix_second = ' + '
            value = edit_keyword_conversion(str(new[i]))
            value_second = edit_keyword_conversion(str(old[i]))
        # ключ присутствует только в новом файле
        elif i in only_in_first_file:
            is_both = False
            prefix = ' - '
            value = edit_keyword_conversion(str(new[i]))
        # ключ присутсвует только в старом файле
        elif i in only_in_second_file:
            is_both = False
            prefix = ' + '
            value = edit_keyword_conversion(str(old[i]))

        # собираем строку
        diff_json_str += generate_difference_for_key(prefix, str(i), value)
        if is_both:
            diff_json_str += generate_difference_for_key(prefix_second,
                                                         str(i), value_second)
    diff_json_str = \
        diff_json_str[:-2] + generate_difference_for_key(last_run=True)
    return diff_json_str


if __name__ == '__main__':
    main()
