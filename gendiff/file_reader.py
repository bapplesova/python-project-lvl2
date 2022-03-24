import os


def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def get_file_type(file_path):
    file_extension = os.path.splitext(file_path)
    if file_extension[1] == '.json':
        return 'json'
    elif file_extension[1] in ('.yaml', '.yml'):
        return 'yaml'
    else:
        raise Exception('Invalid file format.')
