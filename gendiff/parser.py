import argparse


def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['json', 'plain', 'stylish'],
                        help='set format of output (default: stylish)')
    args = parser.parse_args()
    return args
