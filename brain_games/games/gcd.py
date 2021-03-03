"""Building QA suitable for GCD game."""

import math
import random

from brain_games.qa import QA

NUMBER_INTERVAL = (1, 100)
HELP_TEXT = 'Find the greatest common divisor of given numbers.'


def gen_gcd_qa(operand1: int, operand2: int):
    """Create QA."""
    question = '{0} {1}'.format(
        operand1, operand2,
    )
    answer = str(math.gcd(operand1, operand2))
    return QA(question, answer)


def gen_random_qa():
    """Create random QA."""
    return gen_gcd_qa(
        operand1=random.randint(*NUMBER_INTERVAL),
        operand2=random.randint(*NUMBER_INTERVAL),
    )
