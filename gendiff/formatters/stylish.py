from gendiff.cli import edit_keyword_conversion


def collect_stylish_result(total_dict, indent):
    all_keys = tuple(sorted(total_dict))

    result_string = '{\n'
    for key in all_keys:
        # отступ для печати вложенных данных
        temp_indent = indent
        # доп.строка для печати второго значения когда данные изменены
        additional_string = ''

        if isinstance(total_dict[key], dict):
            temp_indent = indent + 3
            temp_value = collect_stylish_result(total_dict[key], indent + 4)
            prefix1 = ''
        elif total_dict[key][0] == ' ':
            prefix1, prefix2, temp_value, additional_string = \
                prepare_different_value(total_dict[key][1],
                                        total_dict[key][2],
                                        key, indent)
        elif isinstance(total_dict[key][1], dict):
            prefix1 = total_dict[key][0]
            temp_value = collect_stylish_result(total_dict[key][1], indent + 4)
        else:
            prefix1 = total_dict[key][0]
            temp_value = edit_keyword_conversion(str(total_dict[key][1]))
        result_string += ' ' * temp_indent + prefix1 + str(key) +\
                         ': ' + temp_value + '\n' + additional_string

    result_string = result_string[:-1] + '\n' + ' ' * (indent - 1) + '}'
    return result_string


def prepare_different_value(new_value, old_value, key, indent):
    if isinstance(new_value, dict):
        prefix1 = ' - '
        prefix2 = ' + '
        temp_value = collect_stylish_result(new_value, indent + 4)
        old_value = edit_keyword_conversion(str(old_value))
        additional_string = ' ' * indent + prefix2 + str(key) + \
                            ': ' + old_value + '\n'
    elif isinstance(old_value, dict):
        prefix1 = ' - '
        prefix2 = ' + '
        temp_value = edit_keyword_conversion(str(new_value))
        old_value = collect_stylish_result(old_value, indent + 4)
        additional_string = ' ' * indent + prefix2 + str(key) + \
                            ': ' + old_value + '\n'
    else:
        prefix1 = ' - '
        prefix2 = ' + '
        temp_value = edit_keyword_conversion(str(new_value))
        old_value = edit_keyword_conversion(str(old_value))
        additional_string = ' ' * indent + prefix2 + str(key) + \
                            ': ' + old_value + '\n'
    return prefix1, prefix2, temp_value, additional_string
