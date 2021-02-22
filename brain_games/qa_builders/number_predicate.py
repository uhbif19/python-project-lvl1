"""QA builders asking questions if number matches predicate."""

import random
from abc import abstractmethod
from dataclasses import dataclass

from brain_games.math import is_prime
from brain_games.qa import QA
from brain_games.qa_builders.abstract import GameQABuilder


@dataclass
class NumberPredicateQABuilder(GameQABuilder):
    """
    ABC for QA builders which ask if numbere matches predicate.

    Question is number. If predicate for number is true, then answer is "yes".
    """

    number: int

    number_interval = (1, 100)

    @classmethod
    def from_random(cls):
        """Create builder for random number in cls.number_interval."""
        return cls(random.randint(*cls.number_interval))

    def get_result(self) -> QA:
        """Return builded QA."""
        answer = 'yes' if self._number_predicate() else 'no'
        return QA(str(self.number), answer)

    @abstractmethod
    def _number_predicate(self) -> bool:
        """See class docstring."""


class BrainEvenQABuilder(NumberPredicateQABuilder):
    """Build QA suitable for brain_even game."""

    help_text = 'Answer "yes" if the number is even, otherwise answer "no".'

    def _number_predicate(self) -> bool:
        """Check if number even."""
        return not bool(self.number % 2)


class PrimeQABuilder(NumberPredicateQABuilder):
    """Build QA suitable for Prime game."""

    help_text = 'Answer "yes" if the number is prime, otherwise answer "no".'

    def _number_predicate(self) -> bool:
        """Check if number is prime."""
        return is_prime(self.number)
