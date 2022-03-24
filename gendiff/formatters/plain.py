from gendiff.formatters.data_map import bool_to_str


def format_plain(total_dict):
    return format_plain_internal(total_dict, '', '')[:-1]


def format_plain_internal(total_dict, key_parents, lines=''):
    each_line = "Property '" + key_parents
    all_keys = tuple(sorted(total_dict))
    for key in all_keys:
        value = total_dict[key]
        if isinstance(value, list):
            lines += get_list_value(value, each_line, key)
        elif isinstance(value, dict):
            lines += format_plain_internal(value, key_parents + key + '.', '')
    return lines


def get_list_value(value, each_line, key):
    line = ''
    string_status = value[0]
    old_value = format_value(value[1])

    if string_status == 'removed':
        line += f"{each_line}{key}' was removed\n"
    elif string_status == 'added' and isinstance(old_value, dict):
        line += f"{each_line}{key}" \
                f"' was added with value: [complex value]\n"
    elif string_status == 'added':
        line += f"{each_line}{key}' was added with value: " \
                f"{old_value}\n"
    elif string_status == 'changed':
        new_value = format_value(value[2])
        line += f"{each_line}{key}' was updated. " \
                f"From {old_value} to {new_value}\n"
    return line


def format_value(value):
    if isinstance(value, str):
        return "'" + value + "'"
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return bool_to_str(str(value))
