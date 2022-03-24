from gendiff.file_reader import read_file
from gendiff.file_reader import get_file_type
from gendiff.parser import parse
from gendiff.formatters.formatter import format_diff


def generate_diff(first_file, second_file, format='stylish'):
    new_data_type = get_file_type(first_file)
    old_data_type = get_file_type(second_file)
    first_data = read_file(first_file)
    second_data = read_file(second_file)
    new_file = parse(first_data, new_data_type)
    old_file = parse(second_data, old_data_type)
    dictionary_difference = generate_diff_dict(new_file, old_file)

    result = format_diff(dictionary_difference, format)
    return result


def generate_diff_dict(new_data, old_data):
    diff_dict = {}
    keys_new = new_data.keys()
    keys_old = old_data.keys()

    added = keys_old - keys_new
    for key in added:
        diff_dict[key] = ['added',
                          generate_diff_dict(old_data[key], old_data[key])
                          if isinstance(old_data[key], dict) else old_data[key]]

    removed = keys_new - keys_old
    for key in removed:
        diff_dict[key] = ['removed',
                          generate_diff_dict(new_data[key], new_data[key])
                          if isinstance(new_data[key], dict) else new_data[key]]

    both = keys_new & keys_old
    for key in both:
        if isinstance(new_data[key], dict) and isinstance(old_data[key], dict):
            diff_dict[key] = generate_diff_dict(new_data[key], old_data[key])
        elif new_data[key] == old_data[key]:
            diff_dict[key] = ['unchanged', new_data[key]]
        else:
            diff_dict[key] = ['changed',
                              generate_diff_dict(new_data[key], new_data[key])
                              if isinstance(new_data[key], dict)
                              else new_data[key],
                              generate_diff_dict(old_data[key], old_data[key])
                              if isinstance(old_data[key], dict)
                              else old_data[key]]
    return diff_dict
