"""Game logic, like generating quesions and answers, not touching IO."""

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class QA:
    """
    Pair of question and expected answer.

    Exists to be asked to user in quiz game.
    """

    question: str
    correct_answer: str


class GameQABuilder(ABC):
    """Building QA suitable for game."""

    help_text: Optional[str]

    @classmethod
    @abstractmethod
    def from_random(cls):
        """Create builder filled with random data."""

    @abstractmethod
    def get_result(self) -> QA:
        """Return builded QA."""


@dataclass
class BrainEvenQABuilder(GameQABuilder):
    """Build QA suitable for brain_even game."""

    number: int

    number_interval = (1, 100)
    help_text = 'Answer "yes" if the number is even, otherwise answer "no".'

    @classmethod
    def from_random(cls):
        """Create builder for random number in cls.number_interval."""
        return cls(random.randint(*cls.number_interval))  # noqa: S311

    def get_result(self) -> QA:
        """Return builded QA."""
        number_even = not bool(self.number % 2)
        return QA(str(self.number), 'yes' if number_even else 'no')
