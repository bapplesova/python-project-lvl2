from gendiff.cli import edit_keyword_conversion


def collect_plain_result(total_dict, key_parents):
    result = collect_internal_plain_result(total_dict, key_parents)
    return result[:-1]


def collect_internal_plain_result(total_dict, key_parents):
    result = ''
    all_keys = tuple(sorted(total_dict))
    for key in all_keys:
        if isinstance(total_dict[key], dict):
            new_key_parents = get_new_key_parents(key_parents, key)
            result += collect_internal_plain_result(total_dict[key],
                                                    new_key_parents)
        elif total_dict[key][0] == 'unchanged':
            continue
        else:
            end_of_string = get_end_of_string(total_dict[key])
            result += 'Property \'' + key_parents + key + '\' was ' +\
                      end_of_string
    return result


def get_new_key_parents(key_parents, key):
    if key_parents == '':
        new_key_parents = key + '.'
    else:
        new_key_parents = key_parents + key + '.'
    return new_key_parents


def get_end_of_string(total_dict_key):
    id_new_value = 1
    value = get_value(total_dict_key, id_new_value)
    if total_dict_key[0] == 'removed':
        end_of_string = total_dict_key[0] + '\n'
    elif total_dict_key[0] == 'added':
        end_of_string = 'added with value: ' + value + '\n'
    elif total_dict_key[0] == 'changed':
        id_old_value = 2
        value2 = get_value(total_dict_key, id_old_value)
        end_of_string = 'updated. From ' + value + ' to ' + value2 + '\n'
    else:
        end_of_string = ''
    return end_of_string


def get_value(dict_key, item_id):
    if isinstance(dict_key[item_id], dict):
        return '[complex value]'
    elif isinstance(dict_key[item_id], str):
        return '\'' + dict_key[item_id] + '\''
    else:
        return edit_keyword_conversion(str(dict_key[item_id]))
