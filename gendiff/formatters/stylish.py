from gendiff.cli import edit_keyword_conversion


def collect_stylish_result(total_dict, indent): # noqa: max-complexity: 7
    all_keys = tuple(sorted(total_dict))

    result_string = '{\n'
    for key in all_keys:
        print('key', key, total_dict[key])
        flag = False
        temp_indent = indent
        if isinstance(total_dict[key], dict):
            temp_indent = indent + 3
            temp_value = collect_stylish_result(total_dict[key], indent + 4)
            prefix1 = ''
        elif isinstance(total_dict[key][1], dict) and total_dict[key][0] == ' ':
            flag = True
            prefix1 = ' - '
            prefix2 = ' + '
            temp_value = collect_stylish_result(total_dict[key][1], indent + 4)
            old_value = edit_keyword_conversion(str(total_dict[key][2]))
        elif isinstance(total_dict[key][1], dict):
            prefix1 = total_dict[key][0]
            temp_value = collect_stylish_result(total_dict[key][1], indent + 4)
        elif total_dict[key][0] == ' ':
            flag = True
            prefix1 = ' - '
            prefix2 = ' + '
            temp_value = edit_keyword_conversion(str(total_dict[key][1]))
            old_value = edit_keyword_conversion(str(total_dict[key][2]))
        else:
            prefix1 = total_dict[key][0]
            temp_value = edit_keyword_conversion(str(total_dict[key][1]))
        result_string += ' ' * temp_indent + prefix1 + str(key) + ': ' \
                         + temp_value + '\n'
        if flag is True:
            result_string += ' ' * temp_indent + prefix2 + str(key) + ': ' \
                             + old_value + '\n'
    result_string = result_string[:-1] + '\n' + ' ' * (indent - 1) + '}'
    return result_string