#!/usr/bin/env python
import json

from gendiff.formatters.stylish import collect_stylish_result
from gendiff.formatters.plain import collect_plain_result


def choose_format(dictionary_difference, required_format):
    indent = 1
    if required_format == 'plain':
        result = collect_plain_result(dictionary_difference, '')
    elif required_format == 'json':
        result = json.dumps(dictionary_difference)
        print('TYPE_CHOOSE', type(result))
    else:
        result = collect_stylish_result(dictionary_difference, indent)
    return result
