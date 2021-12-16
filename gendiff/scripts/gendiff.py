#!/usr/bin/env python

import argparse
import json
import pathlib
from pathlib import Path


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


def generate_diff(new_f, old_f):
    new_file = path_file(new_f)
    old_file = path_file(old_f)
    new = json.load(open(new_file))
    old = json.load(open(old_file))

    all_keys = tuple(sorted(set(new) | set(old)))
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))
    both_in_files = set(new).intersection(set(old))

    diff_json_str = '''{\n'''
    for i in all_keys:
        if i in both_in_files:
            if new[i] == old[i]:
                diff_json_str += ' ' * 3 + str(i) + ' : ' + str(new[i]) + '\n'
            else:
                diff_json_str += ' - ' + str(i) + ' : ' + str(new[i]) + '\n'
                diff_json_str += ' + ' + str(i) + ' : ' + str(old[i]) + '\n'
        elif i in only_in_first_file:
            diff_json_str += ' - ' + str(i) + ' : ' + str(new[i]) + '\n'
        elif i in only_in_second_file:
            diff_json_str += ' + ' + str(i) + ' : ' + str(old[i]) + '\n'
    diff_json_str += '}'
    return diff_json_str


if __name__ == '__main__':
    main()
