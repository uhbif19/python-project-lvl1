import pytest
from brain_games.games_logic import (
    BinaryOp,
    BrainEvenQABuilder,
    CalculatorQABuilder,
    GCDQABuilder,
    PrimeQABuilder,
    ProgressionQABuilder,
)


@pytest.mark.parametrize(
    'builder_class, args, question, answer',
    [
        (BrainEvenQABuilder, [5], '5', 'no'),
        (BrainEvenQABuilder, [6], '6', 'yes'),
        (PrimeQABuilder, [5], '5', 'yes'),
        (PrimeQABuilder, [6], '6', 'no'),
        (CalculatorQABuilder, [1, 2, BinaryOp.ADD], '1 + 2', '3'),
        (CalculatorQABuilder, [1, 2, BinaryOp.SUB], '1 - 2', '-1'),
        (CalculatorQABuilder, [1, 2, BinaryOp.MUL], '1 * 2', '2'),
        (GCDQABuilder, [3, 9], '3 9', '3'),
        (GCDQABuilder, [100, 52], '100 52', '4'),
        (ProgressionQABuilder, [5, 2, 5], '5 7 9 11 13 .. 17 19 21 23', '15'),
    ]
)
def test_qa_builder_generates_correctly(builder_class, args, question, answer):
    builder = builder_class(*args)
    qa = builder.get_result()
    assert qa.question == question
    assert qa.correct_answer == answer

@pytest.mark.parametrize(
    'builder_class',
    [
        BrainEvenQABuilder, PrimeQABuilder, CalculatorQABuilder, GCDQABuilder,
        ProgressionQABuilder
    ]
)
def test_qa_builder_from_random_not_failing(builder_class):
    builder_class.from_random().get_result()
