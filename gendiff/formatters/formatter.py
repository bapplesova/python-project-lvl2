#!/usr/bin/env python

from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_diff(dictionary_difference, required_format):
    indent = 1
    if required_format == 'plain':
        result = format_plain(dictionary_difference)
    elif required_format == 'json':
        result = format_json(dictionary_difference)
    else:
        result = format_stylish(dictionary_difference, indent)
    return result
