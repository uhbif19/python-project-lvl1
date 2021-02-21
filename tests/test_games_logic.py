import pytest

from brain_games.games_logic import BrainEvenQABuilder


@pytest.mark.parametrize(
    'number, answer',
    [(5, 'no'), (6, 'yes')]
)
def test_brain_even_qa_builder_generates_correctly(number, answer):
    builder = BrainEvenQABuilder(number)
    qa = builder.get_result()
    assert qa.question == str(number)
    assert qa.correct_answer == answer

def test_qa_builder_from_random_not_failing():
    BrainEvenQABuilder.from_random().get_result()
