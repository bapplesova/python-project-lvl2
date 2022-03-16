from gendiff.cli import get_arg_parser
from gendiff.generator_diff import generate_diff


def main():
    args = get_arg_parser()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
