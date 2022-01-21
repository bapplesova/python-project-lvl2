from gendiff.cli import edit_keyword_conversion


def collect_json_result(total_dict):
    result = collect_internal_json_res(total_dict)
    result = result[:-1].replace(',,', ',')
    result = result.replace(',}', '}')
    return result


def collect_internal_json_res(total_dict):
    result = make_brackets(True)
    all_keys = tuple(sorted(total_dict))

    for key in all_keys:
        additional_string = ''
        if isinstance(total_dict[key], dict):
            prefix = ''
            value = collect_internal_json_res(total_dict[key])
        elif total_dict[key][0] == ' ':
            prefix = ' - '
            value = get_value(total_dict[key][1])
            additional_string = '" + ' + key + '": ' + get_value(total_dict[key][2]) + ','
        else:
            prefix = total_dict[key][0]
            value = get_value(total_dict[key][1])
        result += '"' + prefix + key + '": ' + value + ',' + additional_string
    result = result[:-1] + make_brackets(False)
    return result


def get_value(value):
    if isinstance(value, dict):
        return collect_internal_json_res(value)
    elif isinstance(value, str):
        return '"' + value + '"'
    else:
        return edit_keyword_conversion(str(value))


def make_brackets(is_first_call):
    if is_first_call is True:
        return '{'
    else:
        return '},'