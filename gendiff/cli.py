import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output (default: stylish)')
    args = parser.parse_args()
    return args
