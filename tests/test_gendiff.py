from gendiff.scripts.gendiff import generate_diff

FILE1_SIMPLE_JSON = 'tests/fixtures/file1.json'
FILE2_SIMPLE_JSON = 'tests/fixtures/file2.json'
FILE1_SIMPLE_YAML = 'tests/fixtures/file1.yaml'
FILE2_SIMPLE_YAML = 'tests/fixtures/file2.yaml'

FILE1_NESTED_JSON = 'tests/fixtures/f1.json'
FILE2_NESTED_JSON = 'tests/fixtures/f2.json'
FILE1_NESTED_YAML = 'tests/fixtures/f1.yaml'
FILE2_NESTED_YAML = 'tests/fixtures/f2.yaml'

file_stylish_simple = 'tests/fixtures/answer_stylish_simple'
ANSWER_STYLISH_SIMPLE = open(file_stylish_simple, "r").read()
file_stylish_nested = 'tests/fixtures/answer_stylish_nested'
ANSWER_STYLISH_NESTED = open(file_stylish_nested, "r").read()

file_plain_simple = 'tests/fixtures/answer_plain_simple'
ANSWER_PLAIN_SIMPLE = open(file_plain_simple, "r").read()
file_plain_nested = 'tests/fixtures/answer_plain_nested'
ANSWER_PLAIN_NESTED = open(file_plain_nested, "r").read()

file_json_simple = 'tests/fixtures/answer_json_simple.json'
ANSWER_JSON_SIMPLE = open(file_json_simple, "r").read()
file_json_nested = 'tests/fixtures/answer_json_nested.json'
ANSWER_JSON_NESTED = open(file_json_nested, "r").read()


def test_generate_stylish_simple():
    tested_format = 'stylish'
    diff_result = str(generate_diff(FILE1_SIMPLE_JSON, FILE2_SIMPLE_JSON, tested_format))
    assert diff_result == ANSWER_STYLISH_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_YAML, FILE2_SIMPLE_YAML, tested_format))
    assert diff_result == ANSWER_STYLISH_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_JSON, FILE2_SIMPLE_YAML, tested_format))
    assert diff_result == ANSWER_STYLISH_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_YAML, FILE2_SIMPLE_JSON, tested_format))
    assert diff_result == ANSWER_STYLISH_SIMPLE


def test_generate_stylish_nested():
    tested_format = 'stylish'
    diff_result = str(generate_diff(FILE1_NESTED_JSON, FILE2_NESTED_JSON, tested_format))
    assert diff_result == ANSWER_STYLISH_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_YAML, FILE2_NESTED_YAML, tested_format))
    assert diff_result == ANSWER_STYLISH_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_JSON, FILE2_NESTED_YAML, tested_format))
    assert diff_result == ANSWER_STYLISH_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_YAML, FILE2_NESTED_JSON, tested_format))
    assert diff_result == ANSWER_STYLISH_NESTED


def test_generate_plain_simple():
    tested_format = 'plain'
    diff_result = str(generate_diff(FILE1_SIMPLE_JSON, FILE2_SIMPLE_JSON, tested_format))
    assert diff_result == ANSWER_PLAIN_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_YAML, FILE2_SIMPLE_YAML, tested_format))
    assert diff_result == ANSWER_PLAIN_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_JSON, FILE2_SIMPLE_YAML, tested_format))
    assert diff_result == ANSWER_PLAIN_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_YAML, FILE2_SIMPLE_JSON, tested_format))
    assert diff_result == ANSWER_PLAIN_SIMPLE


def test_generate_plain_nested():
    tested_format = 'plain'
    diff_result = str(generate_diff(FILE1_NESTED_JSON, FILE2_NESTED_JSON, tested_format))
    assert diff_result == ANSWER_PLAIN_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_YAML, FILE2_NESTED_YAML, tested_format))
    assert diff_result == ANSWER_PLAIN_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_JSON, FILE2_NESTED_YAML, tested_format))
    assert diff_result == ANSWER_PLAIN_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_YAML, FILE2_NESTED_JSON, tested_format))
    assert diff_result == ANSWER_PLAIN_NESTED


def test_generate_json_simple():
    tested_format = 'json'
    diff_result = str(generate_diff(FILE1_SIMPLE_JSON, FILE2_SIMPLE_JSON, tested_format))
    assert diff_result == ANSWER_JSON_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_YAML, FILE2_SIMPLE_YAML, tested_format))
    assert diff_result == ANSWER_JSON_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_JSON, FILE2_SIMPLE_YAML, tested_format))
    assert diff_result == ANSWER_JSON_SIMPLE

    diff_result = str(generate_diff(FILE1_SIMPLE_YAML, FILE2_SIMPLE_JSON, tested_format))
    assert diff_result == ANSWER_JSON_SIMPLE


def test_generate_json_nested():
    tested_format = 'json'
    diff_result = str(generate_diff(FILE1_NESTED_JSON, FILE2_NESTED_JSON, tested_format))
    assert diff_result == ANSWER_JSON_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_YAML, FILE2_NESTED_YAML, tested_format))
    assert diff_result == ANSWER_JSON_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_JSON, FILE2_NESTED_YAML, tested_format))
    assert diff_result == ANSWER_JSON_NESTED

    diff_result = str(generate_diff(FILE1_NESTED_YAML, FILE2_NESTED_JSON, tested_format))
    assert diff_result == ANSWER_JSON_NESTED
