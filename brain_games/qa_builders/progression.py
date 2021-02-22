"""ProgressionQABuilder realization."""

import random
from dataclasses import dataclass

from brain_games.qa import QA
from brain_games.qa_builders.abstract import GameQABuilder
from icontract import ensure, invariant


@invariant(lambda self: 0 <= self.masked_index < self.sample_length)
@dataclass
class ProgressionQABuilder(GameQABuilder):
    """
    Building QA suitable for Progression game.

    Each question is sample of first numbers of ariphmetic progression
    with some number masked. The correct answer is masked number.
    """

    start: int  # Progression is defined by two params
    step: int
    masked_index: int  # Index of sample array to be masked in question

    start_interval = (1, 50)
    step_interval = (1, 10)
    sample_length = 10
    help_text = 'What number is missing in the progression?'

    @classmethod
    def from_random(cls):
        """Create builder for random operands."""
        return cls(
            start=random.randint(*cls.start_interval),
            step=random.randint(*cls.step_interval),
            masked_index=random.randint(0, cls.sample_length - 1),
        )

    def get_result(self):
        """Return builded QA."""
        sample = self._first_numbers_sample()
        sample_masked = [
            '..' if index == self.masked_index else str(sample[index])
            for index in range(self.sample_length)
        ]
        question = ' '.join(sample_masked)
        answer = str(sample[self.masked_index])
        return QA(question, answer)

    @ensure(lambda result, self: len(result) == self.sample_length)
    def _first_numbers_sample(self):
        return [
            self.start + (self.step * index)
            for index in range(self.sample_length)
        ]
