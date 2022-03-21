from gendiff.parser import read_file
from gendiff.parser import parse
from gendiff.parser import get_file_type
from gendiff.formatters.formatter import format_diff


def generate_diff(first_file, second_file, format='stylish'):
    new_file_type = get_file_type(first_file)
    old_file_type = get_file_type(second_file)
    first_file_data = read_file(first_file)
    second_file_data = read_file(second_file)
    new_file = parse(first_file_data, new_file_type)
    old_file = parse(second_file_data, old_file_type)
    dictionary_difference = generate_diff_dict(new_file, old_file)
#    print('!!!DD!!!', dictionary_difference)

    result = format_diff(dictionary_difference, format)
    return result


def generate_diff_dict(new_file, old_file):
    diff_dict = {}
    keys_new = new_file.keys()
    keys_old = old_file.keys()

    added = keys_old - keys_new
    for key in added:
        diff_dict[key] = ['added',
                          generate_diff_dict(old_file[key], old_file[key])
                          if isinstance(old_file[key], dict) else old_file[key]]

    removed = keys_new - keys_old
    for key in removed:
        diff_dict[key] = ['removed',
                          generate_diff_dict(new_file[key], new_file[key])
                          if isinstance(new_file[key], dict) else new_file[key]]

    both = keys_new & keys_old
    for key in both:
        if isinstance(new_file[key], dict) and isinstance(old_file[key], dict):
            diff_dict[key] = generate_diff_dict(new_file[key], old_file[key])
        elif new_file[key] == old_file[key]:
            diff_dict[key] = ['unchanged', new_file[key]]
        else:
            diff_dict[key] = ['changed',
                              generate_diff_dict(new_file[key], new_file[key])
                              if isinstance(new_file[key], dict)
                              else new_file[key],
                              generate_diff_dict(old_file[key], old_file[key])
                              if isinstance(old_file[key], dict)
                              else old_file[key]]
    return diff_dict
