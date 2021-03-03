from brain_games.games.prime import is_prime
from hypothesis import given, strategies

EXAMPLES = (
    (1, False),
    (4, False),
    (5, True),
    (57, False),
)


def test_is_prime():
    for num, expected_result in EXAMPLES:
        assert is_prime(num) is expected_result


non_trivial_multiple = strategies.integers(
    # XXX: for too big numbers prime checking will be slow
    min_value=2, max_value=10**6,
)


@given(non_trivial_multiple, non_trivial_multiple)
def test_is_prime_for_non_prime(mult1, mult2):
    assert not is_prime(mult1 * mult2)
