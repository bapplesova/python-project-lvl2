import json
import yaml
from yaml.loader import SafeLoader


# def read_file(file_path):
#    with open(file_path) as file:
#        return file.read()
def read_file(file_path):
    files_data = open(file_path)
    return files_data


def parse(file_data, file_type):
    if file_type == 'json':
        file_data = json.load(file_data)
    elif file_type in 'yaml' or file_type in 'yml':
        file_data = yaml.load(file_data, Loader=SafeLoader)
    return file_data


def get_file_type(file_path):
    file_extension = str(file_path).split('.')
    if file_extension[-1] == 'json':
        return 'json'
    elif file_extension[-1] in ('yaml', 'yml'):
        return 'yaml'
    else:
        raise Exception('Invalid file format.')
