"""ProgressionQABuilder realization."""

import random

from brain_games.qa import QA
from icontract import ensure, require

START_INTERVAL = (1, 50)
STEP_INTERVAL = (1, 10)
SAMPLE_LENGTH = 10
HOW_TO_ANSWER_INSTRUCTION = 'What number is missing in the progression?'


@ensure(lambda result: len(result) == SAMPLE_LENGTH)
def _first_numbers_sample(start: int, step: int):
    return [
        start + (step * index)
        for index in range(SAMPLE_LENGTH)
    ]


@require(lambda masked_index: 0 <= masked_index < SAMPLE_LENGTH)
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
    sample = _first_numbers_sample(start, step)
    sample_masked = [
        '..' if index == masked_index else str(sample[index])
        for index in range(SAMPLE_LENGTH)
    ]
    question = ' '.join(sample_masked)
    answer = str(sample[masked_index])
    return QA(question, answer)


def gen_random_qa():
    """Create builder for random operands."""
    return gen_progression_qa(
        start=random.randint(*START_INTERVAL),
        step=random.randint(*STEP_INTERVAL),
        masked_index=random.randint(0, SAMPLE_LENGTH - 1),
    )
