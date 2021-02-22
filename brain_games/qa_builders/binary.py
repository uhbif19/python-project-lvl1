"""QA builders asking for result of binary operation."""

import math
import operator
import random
from dataclasses import dataclass
from enum import Enum
from typing import Callable

from brain_games.qa import QA
from brain_games.qa_builders.abstract import GameQABuilder


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
