def bool_to_str(value):
    bool_keywords = {'True': 'true',
                     'False': 'false',
                     'None': 'null'}
    if value in set(bool_keywords):
        return bool_keywords[value]
    else:
        return value


def map_prefix(status):
    prefix_dict = {'removed': ' - ',
                   'added': ' + ',
                   'unchanged': '   ',
                   'changed': ' '}
    return prefix_dict[status]
