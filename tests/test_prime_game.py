import pytest
from brain_games.games.prime import is_prime
from hypothesis import given, strategies


@pytest.mark.parametrize(
    'num, expected_result',
    [
        (1, False),
        (4, False),
        (5, True),
        (57, False),
    ],
)
def test_is_prime(num, expected_result):
    assert is_prime(num) is expected_result


non_trivial_multiple = strategies.integers(min_value=2)


@given(non_trivial_multiple, non_trivial_multiple)
def test_is_prime_for_non_prime(mult1, mult2):
    assert not is_prime(mult1 * mult2)
