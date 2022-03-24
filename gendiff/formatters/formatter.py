#!/usr/bin/env python

from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_diff(dictionary_difference, required_format):
    if required_format == 'plain':
        result = format_plain(dictionary_difference)
    elif required_format == 'json':
        result = format_json(dictionary_difference)
    elif required_format == 'stylish':
        result = format_stylish(dictionary_difference)
    else:
        raise Exception('Invalid format. Valid "json", "plain" or "stylish".')
    return result
