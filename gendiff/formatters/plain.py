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
    if value[0] == 'removed':
        line += f"{each_line}{key}' was removed\n"
    elif value[0] == 'added' and isinstance(value[-1], dict):
        line += f"{each_line}{key}" \
                f"' was added with value: [complex value]\n"
    elif value[0] == 'added':
        line += f"{each_line}{key}' was added with value: " \
                f"{format_value(value[-1])}\n"
    elif value[0] == 'changed':
        line += f"{each_line}{key}' was updated. " \
                f"From {format_value(value[1])} to " \
                f"{format_value(value[2])}\n"
    return line


def format_value(value):
    if isinstance(value, str):
        return "'" + value + "'"
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return bool_to_str(str(value))
