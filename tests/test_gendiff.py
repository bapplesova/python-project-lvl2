from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.right_answers import right_answer
from tests.fixtures.right_answers import right_nested_answer
from tests.fixtures.right_answers import right_t_answer
from tests.fixtures.right_answers import right_plain
from tests.fixtures.right_answers import right_plain_nested


def test_generate_diff_json():
    diff_result = str(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish'))
    assert diff_result == right_answer


def test_generate_diff_yaml():
    diff_result = str(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'stylish'))
    assert diff_result == right_answer


def test_generate_diff_json_yaml():
    diff_result = str(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yaml', 'stylish'))
    assert diff_result == right_answer


def test_generate_diff_yaml_json():
    diff_result = str(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.json', 'stylish'))
    assert diff_result == right_answer


def test_generate_diff_simple_nested_json():
    diff_result = str(generate_diff('tests/fixtures/t.json', 'tests/fixtures/tt.json', 'stylish'))
    assert diff_result == right_t_answer


def test_generate_diff_nested_json():
    diff_result = str(generate_diff('tests/fixtures/f1.json', 'tests/fixtures/f2.json', 'stylish'))
    assert diff_result == right_nested_answer


def test_generate_diff_nested_yaml():
    diff_result = str(generate_diff('tests/fixtures/f1.yaml', 'tests/fixtures/f2.yaml', 'stylish'))
    assert diff_result == right_nested_answer


def test_generate_diff_nested_json_yaml():
    diff_result = str(generate_diff('tests/fixtures/f1.json', 'tests/fixtures/f2.yaml', 'stylish'))
    assert diff_result == right_nested_answer


def test_generate_diff_nested_yaml_json():
    diff_result = str(generate_diff('tests/fixtures/f1.yaml', 'tests/fixtures/f2.json', 'stylish'))
    assert diff_result == right_nested_answer


def test_generate_diff_plain_json():
    diff_result = str(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain'))
    assert diff_result == right_plain


def test_generate_diff_plain_yaml():
    diff_result = str(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'plain'))
    assert diff_result == right_plain


def test_generate_diff_plain_json_yaml():
    diff_result = str(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yaml', 'plain'))
    assert diff_result == right_plain


def test_generate_diff_plain_yaml_json():
    diff_result = str(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.json', 'plain'))
    assert diff_result == right_plain


def test_generate_diff_nested_plain_json():
    diff_result = str(generate_diff('tests/fixtures/f1.json', 'tests/fixtures/f2.json', 'plain'))
    assert diff_result == right_plain_nested


def test_generate_diff_nested_plain_yaml():
    diff_result = str(generate_diff('tests/fixtures/f1.yaml', 'tests/fixtures/f2.yaml', 'plain'))
    assert diff_result == right_plain_nested


def test_generate_diff_nested_plain_json_yaml():
    diff_result = str(generate_diff('tests/fixtures/f1.json', 'tests/fixtures/f2.yaml', 'plain'))
    assert diff_result == right_plain_nested


def test_generate_diff_nested_plain_yaml_json():
    diff_result = str(generate_diff('tests/fixtures/f1.yaml', 'tests/fixtures/f2.json', 'plain'))
    assert diff_result == right_plain_nested
