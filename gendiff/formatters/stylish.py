from gendiff.data_mapping import bool_to_str
from gendiff.data_mapping import map_prefix


def format_stylish(total_dict, indent):
    all_keys = tuple(sorted(total_dict))

    result_string = '{\n'
    for key in all_keys:
        # отступ для печати вложенных данных
        temp_indent = indent
        # доп.строка для печати второго значения когда данные изменены
        additional_string = ''

        if isinstance(total_dict[key], dict):
            temp_indent = indent + 3
            temp_value = format_stylish(total_dict[key],
                                        indent + 4)
            prefix1 = ''
        elif total_dict[key][0] == 'changed':
            prefix1, prefix2, temp_value, additional_string = \
                get_changed_values(total_dict[key][1],
                                   total_dict[key][2],
                                   key, indent)
        elif isinstance(total_dict[key][1], dict):
            prefix1 = map_prefix(total_dict[key][0])
            temp_value = format_stylish(total_dict[key][1],
                                        indent + 4)
        else:
            prefix1 = map_prefix(total_dict[key][0])
            temp_value = bool_to_str(str(total_dict[key][1]))
        result_indent = ' ' * temp_indent
        result_string += f"{result_indent}{prefix1}{str(key)}: " \
                         f"{temp_value}\n{additional_string}"

    total_indent = ' ' * (indent - 1)
    result_string = f"{result_string[:-1]}\n{total_indent}" + '}'
    return result_string


def get_changed_values(new_value, old_value, key, indent):
    if isinstance(new_value, dict):
        prefix1 = ' - '
        prefix2 = ' + '
        temp_value = format_stylish(new_value, indent + 4)
        old_value = bool_to_str(str(old_value))

    elif isinstance(old_value, dict):
        prefix1 = ' - '
        prefix2 = ' + '
        temp_value = bool_to_str(str(new_value))
        old_value = format_stylish(old_value, indent + 4)

    else:
        prefix1 = ' - '
        prefix2 = ' + '
        temp_value = bool_to_str(str(new_value))
        old_value = bool_to_str(str(old_value))

    total_indent = ' ' * indent
    additional_string = f"{total_indent}{prefix2}{str(key)}: {old_value}\n"
#    additional_string = ' ' * indent + prefix2 + str(key) + \
#                        ': ' + old_value + '\n'
    return prefix1, prefix2, temp_value, additional_string
