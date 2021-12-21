#!/usr/bin/env python

import argparse
import json
import pathlib
from pathlib import Path


BOOL_KEYWORDS = {'True': 'true',
                 'False': 'false',
                 'None': 'null'}


def main():
    args = run()
    diff_json = generate_diff(args.first_file, args.second_file)
    print(diff_json)


def path_file(file_path):
    # Получаем строку, содержащую путь к рабочей директории:
    dir_path = pathlib.Path.cwd()
    if str(dir_path) in file_path:
        return file_path
    else:
        # Объединяем полученную строку с недостающими частями пути
        path = Path(dir_path, file_path)
        return path


def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def generate_difference_string(*args, first_run=False, last_run=False):
    if len(args) != 0:
        prefix = args[0]
        key = args[1]
        value = str(args[2])
    if first_run is False and last_run is False:
        new_part_str = prefix + key + ': ' + value + ',\n'
    elif first_run:
        new_part_str = '''{\n'''
    elif last_run:
        new_part_str = '\n}'
    return new_part_str


def generate_diff(new_f, old_f):
    new_file = path_file(new_f)
    old_file = path_file(old_f)
    new = json.load(open(new_file))
    old = json.load(open(old_file))

    all_keys = tuple(sorted(set(new) | set(old)))
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))
    both_in_files = set(new).intersection(set(old))

    value_second = ''
    diff_json_str = generate_difference_string(first_run=True)

    for i in all_keys:
        # ключ присутствует в обоих файлах
        if i in both_in_files:
            # значение не изменилось
            if new[i] == old[i]:
                is_both = False
                prefix = ' ' * 3
                value = str(new[i])
            # значения разные
            else:
                is_both = True
                prefix = ' - '
                prefix_second = ' + '
                value = str(new[i])
                value_second = str(old[i])
        # ключ присутствует только в новом файле
        elif i in only_in_first_file:
            is_both = False
            prefix = ' - '
            value = str(new[i])
        # ключ присутсвует только в старом файле
        elif i in only_in_second_file:
            is_both = False
            prefix = ' + '
            value = str(old[i])

        if value in ('True', 'False'):
            value = value.lower()
            value_second = value_second.lower()

        # собираем строку
        diff_json_str += generate_difference_string(prefix, str(i), value)
        if is_both:
            diff_json_str += generate_difference_string(prefix_second,
                                                        str(i), value_second)
    diff_json_str = \
        diff_json_str[:-2] + generate_difference_string(last_run=True)
    return diff_json_str


if __name__ == '__main__':
    main()
