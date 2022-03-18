from gendiff.data_mapping import bool_to_str


def format_plain(total_dict):
    return format_plain_internal(total_dict, '', '')[:-1]


def format_plain_internal(total_dict, key_parents, lines=''):
    each_line = "Property '" + key_parents
    all_keys = tuple(sorted(total_dict))
    for key in all_keys:
        value = total_dict[key]
        if isinstance(value, list):
            if value[0] == 'removed':
                lines += f"{each_line}{key}' was removed\n"
            elif value[0] == 'added':
                if isinstance(value[-1],dict):
                    lines += f"{each_line}{key}' was added with value: [complex value]\n"
                else:
                    lines += f"{each_line}{key}' was added with value: {format_value(value[-1])}\n"
            elif value[0] == 'changed':
                lines += f"{each_line}{key}' was updated. From {format_value(value[1])} to {format_value(value[2])}\n"
        elif isinstance(value, dict):
            lines += format_plain_internal(value, key_parents + key + '.', '')
    return lines


def format_value(value):
    if isinstance(value, str):
        return "'" + value + "'"
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return bool_to_str(str(value))
