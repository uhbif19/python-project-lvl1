"""Build QA suitable for Even game."""

import random

from brain_games.qa import QA

NUMBER_INTERVAL = (1, 100)
HELP_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def gen_even_qa(number: int) -> QA:
    """Create random QA for Even game.."""
    even = not bool(number % 2)
    answer = 'yes' if even else 'no'
    return QA(str(number), answer)


def gen_random_qa():
    """Create QA for Even game."""
    return gen_even_qa(random.randint(*NUMBER_INTERVAL))
