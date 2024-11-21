from hexlet_pytest.example import reverse
from pathlib import Path

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def get_fixture_path(filename):
    return Path(__file__).parent / 'fixtures' / filename

def read_file(filename):
    return get_fixture_path(filename).read_text()


def test_reverse_with_fixtures():
    before_reverse = read_file('before.txt')
    expected = read_file('result.txt')
    actual = reverse(before_reverse)

    assert actual == expected