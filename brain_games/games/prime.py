"""Build QA suitable for Prime game."""

import math
import random

from brain_games.qa import QA
from icontract import require

NUMBER_INTERVAL = (1, 100)
HELP_TEXT = 'Answer "yes" if the number is prime, otherwise answer "no".'


@require(lambda num: num > 0)
def is_prime(num: int) -> bool:
    """
    Super simple realization of prime checker.

    Args:
        num: number to check if it is prime
    """
    if num == 1:
        return False
    for possible_multiply in range(2, math.ceil(num / 2) + 1):
        if num % possible_multiply == 0:
            return False
    return True


def gen_prime_qa(number: int) -> QA:
    """Create random QA for Prime game."""
    answer = 'yes' if is_prime(number) else 'no'
    return QA(str(number), answer)


def gen_random_qa():
    """Create QA for Prime game."""
    return gen_prime_qa(random.randint(*NUMBER_INTERVAL))
