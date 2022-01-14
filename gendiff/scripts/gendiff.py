#!/usr/bin/env python

from gendiff.parser import run
from gendiff.file_opener import read_file
from gendiff.file_opener import make_path_file


def main():
    args = run()
    generate_diff(args.first_file, args.second_file, args.format)


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
            temp_dict[i] = ['   ', new_file[i]]
        # ключ присутствует в обоих файлах, значения разные
        elif new_file[i] != old_file[i] and isinstance(new_file[i], dict):
            temp_dict[i] = [' ', generate_difference(new_file[i], new_file[i]),
                            old_file[i]]
        elif new_file[i] != old_file[i] and isinstance(old_file[i], dict):
            temp_dict[i] = [' ', new_file[i],
                            generate_difference(old_file[i], old_file[i])]
        else:
            temp_dict[i] = [' ', new_file[i], old_file[i]]
    return temp_dict


def generate_difference(new, old):
    # словарь для хранения отличий
    total_diff_dictionary = {}

    # формируем множества из ключей файлов
#    all_keys = set(sorted(set(new).union(set(old))))
    only_in_first_file = set(new).difference(set(old))
    only_in_second_file = set(old).difference(set(new))

    total_diff_dictionary = find_files_difference(new,
                                                  only_in_first_file, ' - ')
    total_diff_dictionary.update(find_files_difference(old,
                                                       only_in_second_file,
                                                       ' + '))
    total_diff_dictionary.update(find_files_intersection(new, old))
    return total_diff_dictionary


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
