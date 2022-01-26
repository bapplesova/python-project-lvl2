#!/usr/bin/env python
import json

from gendiff.formatters.stylish import collect_stylish_result
from gendiff.formatters.plain import collect_plain_result
from gendiff.formatters.json import collect_json_result


def choose_format(dictionary_difference, required_format):
    indent = 1
    if required_format == 'plain':
        result = collect_plain_result(dictionary_difference, '')
    elif required_format == 'json':
        result = collect_json_result(dictionary_difference)
        json.dumps(result)
    else:
        result = collect_stylish_result(dictionary_difference, indent)
    return result
