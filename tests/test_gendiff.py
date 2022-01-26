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
answer_stylish_simple = open(file_stylish_simple, "r").read()
file_stylish_nested = 'tests/fixtures/answer_stylish_nested'
answer_stylish_nested = open(file_stylish_nested, "r").read()

file_plain_simple = 'tests/fixtures/answer_plain_simple'
answer_plain_simple = open(file_plain_simple, "r").read()
file_plain_nested = 'tests/fixtures/answer_plain_nested'
answer_plain_nested = open(file_plain_nested, "r").read()

file_json_simple = 'tests/fixtures/answer_json_simple.json'
answer_json_simple = open(file_json_simple, "r").read()
file_json_nested = 'tests/fixtures/answer_json_nested.json'
answer_json_nested = open(file_json_nested, "r").read()


@pytest.mark.parametrize(
    "file1, file2, output_format, expected",
    [(file1_simple_json, file2_simple_json, format_stylish, answer_stylish_simple),
     (file1_simple_json, file2_simple_yaml, format_stylish, answer_stylish_simple),
     (file1_simple_yaml, file2_simple_json, format_stylish, answer_stylish_simple),
     (file1_simple_yaml, file2_simple_yaml, format_stylish, answer_stylish_simple),

     (file1_simple_json, file2_simple_json, format_plain, answer_plain_simple),
     (file1_simple_json, file2_simple_yaml, format_plain, answer_plain_simple),
     (file1_simple_yaml, file2_simple_json, format_plain, answer_plain_simple),
     (file1_simple_yaml, file2_simple_yaml, format_plain, answer_plain_simple),

     (file1_simple_json, file2_simple_json, format_json, answer_json_simple),
     (file1_simple_json, file2_simple_yaml, format_json, answer_json_simple),
     (file1_simple_yaml, file2_simple_json, format_json, answer_json_simple),
     (file1_simple_yaml, file2_simple_yaml, format_json, answer_json_simple),

     (file1_nested_json, file2_nested_json, format_stylish, answer_stylish_nested),
     (file1_nested_json, file2_nested_yaml, format_stylish, answer_stylish_nested),
     (file1_nested_yaml, file2_nested_json, format_stylish, answer_stylish_nested),
     (file1_nested_yaml, file2_nested_yaml, format_stylish, answer_stylish_nested),

     (file1_nested_json, file2_nested_json, format_plain, answer_plain_nested),
     (file1_nested_json, file2_nested_yaml, format_plain, answer_plain_nested),
     (file1_nested_yaml, file2_nested_json, format_plain, answer_plain_nested),
     (file1_nested_yaml, file2_nested_yaml, format_plain, answer_plain_nested),

     (file1_nested_json, file2_nested_json, format_json, answer_json_nested),
     (file1_nested_json, file2_nested_yaml, format_json, answer_json_nested),
     (file1_nested_yaml, file2_nested_json, format_json, answer_json_nested),
     (file1_nested_yaml, file2_nested_yaml, format_json, answer_json_nested)])
def test_generate(file1, file2, output_format, expected):
    diff_result = str(generate_diff(file1, file2, output_format))
    assert diff_result == expected
