"""Building QA suitable for calculator game."""

import operator
import random

from brain_games.qa import QA
from icontract import require

NUMBER_INTERVAL = (1, 20)

HELP_TEXT = 'Answer the result of presented binary operation.'


# Binary operation from elementary ariphmetics used in Calculator game
BINARY_OPERATIONS = ('+', '-', '*')


@require(lambda operation: operation in BINARY_OPERATIONS)
def operation_to_python(operation: str):
    """Return python function performing this binary operation."""
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }[operation]


@require(lambda operation: operation in BINARY_OPERATIONS)
def gen_calculator_qa(operand1: int, operand2: int, operation: str):
    """Return builded QA."""
    question = '{0} {1} {2}'.format(
        operand1, operation, operand2,
    )
    python_op = operation_to_python(operation)
    answer = str(python_op(operand1, operand2))
    return QA(question, answer)


def gen_random_calculator_qa():
    """Create builder for random operands and operations."""
    return gen_calculator_qa(
        operand1=random.randint(*NUMBER_INTERVAL),
        operand2=random.randint(*NUMBER_INTERVAL),
        operation=random.choice(BINARY_OPERATIONS),
    )
