import pytest
from brain_games.math import is_prime


@pytest.mark.parametrize(
    'num, expected_result',
    [
        (1, False),
        (5, True),
        (57, False),
    ],
)
def test_is_prime(num, expected_result):
    assert is_prime(num) is expected_result
