from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.right_answers import right_json


def test_generate_diff():
    diff_result = str(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
    assert diff_result == right_json

