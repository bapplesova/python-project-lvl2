#!/usr/bin/env python
import json
import yaml
from yaml.loader import SafeLoader


def read_file(file_path):
    file_type = get_file_type(file_path)
    if file_type == 'json':
        file_data = json.load(open(file_path))
    elif file_type in 'yaml':
        file_data = yaml.load(open(file_path), Loader=SafeLoader)
    return file_data


def get_file_type(file_path):
    file_extension = str(file_path).split('.')
    if file_extension[-1] == 'json':
        return 'json'
    elif file_extension[-1] in ('yaml', 'yml'):
        return 'yaml'
    else:
        raise Exception('Invalid file format.')
