import pytest
from gendiff.scripts.gendiff import generate_diff

file1_simple_json = 'tests/fixtures/file1.json'
file2_simple_json = 'tests/fixtures/file2.json'
file1_simple_yaml = 'tests/fixtures/file1.yaml'
file2_simple_yaml = 'tests/fixtures/file2.yaml'

file1_nested_json = 'tests/fixtures/f1.json'
file2_nested_json = 'tests/fixtures/f2.json'
file1_nested_yaml = 'tests/fixtures/f1.yaml'
file2_nested_yaml = 'tests/fixtures/f2.yaml'

format_stylish = 'stylish'
format_plain = 'plain'
format_json = 'json'

file_stylish_simple = 'tests/fixtures/answer_stylish_simple'
file_stylish_nested = 'tests/fixtures/answer_stylish_nested'

file_plain_simple = 'tests/fixtures/answer_plain_simple'
file_plain_nested = 'tests/fixtures/answer_plain_nested'

file_json_simple = 'tests/fixtures/answer_json_simple.json'
file_json_nested = 'tests/fixtures/answer_json_nested.json'


@pytest.mark.parametrize(
    "file1, file2, output_format, answer_file",
    [(file1_simple_json, file2_simple_json, format_stylish, file_stylish_simple),
     (file1_simple_json, file2_simple_yaml, format_stylish, file_stylish_simple),
     (file1_simple_yaml, file2_simple_json, format_stylish, file_stylish_simple),
     (file1_simple_yaml, file2_simple_yaml, format_stylish, file_stylish_simple),

     (file1_simple_json, file2_simple_json, format_plain, file_plain_simple),
     (file1_simple_json, file2_simple_yaml, format_plain, file_plain_simple),
     (file1_simple_yaml, file2_simple_json, format_plain, file_plain_simple),
     (file1_simple_yaml, file2_simple_yaml, format_plain, file_plain_simple),

     (file1_simple_json, file2_simple_json, format_json, file_json_simple),
     (file1_simple_json, file2_simple_yaml, format_json, file_json_simple),
     (file1_simple_yaml, file2_simple_json, format_json, file_json_simple),
     (file1_simple_yaml, file2_simple_yaml, format_json, file_json_simple),

     (file1_nested_json, file2_nested_json, format_stylish, file_stylish_nested),
     (file1_nested_json, file2_nested_yaml, format_stylish, file_stylish_nested),
     (file1_nested_yaml, file2_nested_json, format_stylish, file_stylish_nested),
     (file1_nested_yaml, file2_nested_yaml, format_stylish, file_stylish_nested),

     (file1_nested_json, file2_nested_json, format_plain, file_plain_nested),
     (file1_nested_json, file2_nested_yaml, format_plain, file_plain_nested),
     (file1_nested_yaml, file2_nested_json, format_plain, file_plain_nested),
     (file1_nested_yaml, file2_nested_yaml, format_plain, file_plain_nested),

     (file1_nested_json, file2_nested_json, format_json, file_json_nested),
     (file1_nested_json, file2_nested_yaml, format_json, file_json_nested),
     (file1_nested_yaml, file2_nested_json, format_json, file_json_nested),
     (file1_nested_yaml, file2_nested_yaml, format_json, file_json_nested)])
def test_generate(file1, file2, output_format, answer_file):
    diff_result = str(generate_diff(file1, file2, output_format))
    assert diff_result == get_answer(answer_file)


def get_answer(file_name):
    return open(file_name, "r").read()
