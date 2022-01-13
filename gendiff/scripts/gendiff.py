#!/usr/bin/env python

import pathlib
from pathlib import Path

from gendiff.parser import run
from gendiff.file_opener import read_file


def main():
    args = run()
    generate_diff(args.first_file, args.second_file, args.format)


def make_path_file(file_path):
    # Получаем строку, содержащую путь к рабочей директории
    dir_path = pathlib.Path.cwd()
    if str(dir_path) in file_path:
        return file_path
    else:
        # Объединяем полученную строку с недостающими частями пути
        path = Path(dir_path, file_path)
        return path


def edit_keyword_conversion(value):
    bool_keywords = {'True': 'true',
                     'False': 'false',
                     'None': 'null'}
    if value in set(bool_keywords):
        return bool_keywords[value]
    else:
        return value


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
    result = collect_result(dictionary_difference, indent)
    print('RESULT \n' + result)
    return result


def generate_difference(new, old):
    # формируем множества из ключей файлов
    all_keys = tuple(sorted(set(new).union(set(old))))
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))
    both_in_files = set(new).intersection(set(old))

    # словарь для хранения отличий:  {ключ : [0 - значение в первом файле,
    # 1 - значение во втором файле, *2 - префикс для отображения]}
    difference_dictionary = {}

    for i in all_keys:
        # ключ присутствует в обоих файлах, оба значения - вложенные словари
        if i in both_in_files and isinstance(new[i], dict) \
                and isinstance(old[i], dict):
            difference_dictionary[i] = generate_difference(new[i], old[i])
        # ключ присутствует в обоих файлах, значение не изменилось
        elif i in both_in_files and new[i] == old[i]:
            difference_dictionary[i] = ['   ', new[i]]
        # ключ присутствует в обоих файлах, значения разные
        elif i in both_in_files and new[i] != old[i]:
            if isinstance(new[i], dict):
                difference_dictionary[i] = [' ', generate_difference(new[i],
                                                                     new[i]),
                                            old[i]]
            elif isinstance(old[i], dict):
                difference_dictionary[i] = [' ', new[i],
                                            generate_difference(old[i], old[i])]
            else:
                difference_dictionary[i] = [' ', new[i], old[i]]
        # ключ присутствует только в новом файле
        elif i in only_in_first_file:
            if isinstance(new[i], dict):
                difference_dictionary[i] = [' - ',
                                            generate_difference(new[i], new[i])]
            else:
                difference_dictionary[i] = [' - ', new[i]]
        # ключ присутсвует только в старом файле
        elif i in only_in_second_file and isinstance(old[i], dict):
            difference_dictionary[i] = [' + ',
                                        generate_difference(old[i], old[i])]
        elif i in only_in_second_file:
            difference_dictionary[i] = [' + ', old[i]]
    return difference_dictionary


def collect_result(total_dict, indent):
    all_keys = tuple(sorted(total_dict))
    result_string = '{\n'
    for key in all_keys:
        if type(total_dict[key]) is dict:
            result_string += ' ' * (indent + 3) + str(key) + ': ' \
                             + collect_result(total_dict[key],
                                              indent + 4) + '\n'
        else:
            new_value = edit_keyword_conversion(str(total_dict[key][1]))
            if type(total_dict[key][1]) is dict and total_dict[key][0] == ' ':
                old_value = edit_keyword_conversion(str(total_dict[key][2]))
                result_string += ' ' * indent + ' - ' + str(key) + ': ' \
                                 + collect_result(total_dict[key][1],
                                                  indent + 4) + '\n'
                result_string += ' ' * indent + ' + ' + str(key) + ': ' \
                                 + old_value + '\n'

            elif type(total_dict[key][1]) is dict:
                result_string += ' ' * indent + total_dict[key][0] + \
                                 str(key) + ': ' + \
                                 collect_result(total_dict[key][1],
                                                indent + 4) + '\n'

            elif total_dict[key][0] == ' ':
                old_value = edit_keyword_conversion(str(total_dict[key][2]))
                result_string += ' ' * indent + ' - ' + str(key) + ': ' \
                                 + new_value + '\n'
                result_string += ' ' * indent + ' + ' + str(key) + ': ' \
                                 + old_value + '\n'
            else:
                result_string += ' ' * indent + total_dict[key][0] + \
                                 str(key) + ': ' + new_value + '\n'
    result_string = result_string[:-1] + '\n' + ' ' * (indent - 1) + '}'
    return result_string


if __name__ == '__main__':
    main()
