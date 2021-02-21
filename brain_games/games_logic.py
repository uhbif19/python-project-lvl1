"""Game logic, like generating quesions and answers, not touching IO."""

import operator
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional


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
            operand1=random.randint(*cls.number_interval),  # noqa: S311
            operand2=random.randint(*cls.number_interval),  # noqa: S311
            operation=random.choice(list(BinaryOp)),  # noqa: S311
        )

    def get_result(self):
        """Return builded QA."""
        question = '{0} {1} {2}'.format(
            self.operand1, self.operation.value, self.operand2,
        )
        python_op = self.operation.to_python()
        answer = str(python_op(self.operand1, self.operand2))
        return QA(question, answer)
