"""Game logic, like generating quesions and answers, not touching IO."""

import math
import operator
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional

from brain_games.math import is_prime
from icontract import ensure, invariant


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
class NumberPredicateQABuilder(GameQABuilder):
    """
    ABC for QA builders which ask questions on number.

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


class BinaryOp(Enum):
    """Binary operation from elementary ariphmetics used in Calculator game."""

    # XXX: known issue in WPS

    ADD = '+'  # noqa: WPS115
    SUB = '-'  # noqa: WPS115
    MUL = '*'  # noqa: WPS115

    def to_python(self) -> Callable:
        """Return python function performing this binary operation."""
        return {
            self.ADD: operator.add,
            self.SUB: operator.sub,
            self.MUL: operator.mul,
        }[self]


@dataclass
class CalculatorQABuilder(GameQABuilder):
    """Building QA suitable for calculator game."""

    operand1: int
    operand2: int
    operation: BinaryOp

    number_interval = (1, 20)
    help_text = 'Answer the result of presented binary operation.'

    @classmethod
    def from_random(cls):
        """Create builder for random operands and operations."""
        return cls(
            operand1=random.randint(*cls.number_interval),
            operand2=random.randint(*cls.number_interval),
            operation=random.choice(list(BinaryOp)),
        )

    def get_result(self):
        """Return builded QA."""
        question = '{0} {1} {2}'.format(
            self.operand1, self.operation.value, self.operand2,
        )
        python_op = self.operation.to_python()
        answer = str(python_op(self.operand1, self.operand2))
        return QA(question, answer)


@dataclass
class GCDQABuilder(GameQABuilder):
    """Building QA suitable for GCD game."""

    operand1: int
    operand2: int

    number_interval = (1, 100)
    help_text = 'Find the greatest common divisor of given numbers.'

    @classmethod
    def from_random(cls):
        """Create builder for random operands."""
        return cls(
            operand1=random.randint(*cls.number_interval),
            operand2=random.randint(*cls.number_interval),
        )

    def get_result(self):
        """Return builded QA."""
        question = '{0} {1}'.format(
            self.operand1, self.operand2,
        )
        answer = str(math.gcd(self.operand1, self.operand2))
        return QA(question, answer)


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
