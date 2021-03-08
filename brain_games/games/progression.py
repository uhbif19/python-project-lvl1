"""
Building QA suitable for progression game.

In this file by "progression" we name not ariphmetical progression in math
sense, but array of first numbers of such progression.
"""

import random

from brain_games.qa import QA
from icontract import ensure, require

START_INTERVAL = (1, 50)
STEP_INTERVAL = (1, 10)
PROGRESSION_LENGTH = 10
HOW_TO_ANSWER_INSTRUCTION = 'What number is missing in the progression?'


@ensure(lambda result: len(result) == PROGRESSION_LENGTH)
def _construct_progression(start: int, step: int):
    return [
        start + (step * index)
        for index in range(PROGRESSION_LENGTH)
    ]


@require(lambda masked_index: 0 <= masked_index < PROGRESSION_LENGTH)
def gen_progression_qa(start: int, step: int, masked_index: int):
    """
    Build QA suitable for Progression game.

    Each question is sample of first numbers of ariphmetic progression
    with some number masked. The correct answer is masked number.

    Args:
        start: First number of progression
        step: Step of progression
        masked_index: index of sampled numbers array to be masked in question
    """
    progression = _construct_progression(start, step)
    progression_with_masked_element = [
        '..' if index == masked_index else str(progression[index])
        for index in range(PROGRESSION_LENGTH)
    ]
    question = ' '.join(progression_with_masked_element)
    answer = str(progression[masked_index])
    return QA(question, answer)


def gen_random_qa():
    """Create builder for random operands."""
    return gen_progression_qa(
        start=random.randint(*START_INTERVAL),
        step=random.randint(*STEP_INTERVAL),
        masked_index=random.randint(0, PROGRESSION_LENGTH - 1),
    )
