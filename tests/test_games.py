import pytest
from brain_games.games import calculator, even, gcd, prime, progression


@pytest.mark.parametrize(
    'gen_function, args, question, answer',
    [
        (calculator.gen_calculator_qa, [1, 2, '+'], '1 + 2', '3'),
        (calculator.gen_calculator_qa, [1, 2, '-'], '1 - 2', '-1'),
        (calculator.gen_calculator_qa, [1, 2, '*'], '1 * 2', '2'),
        (gcd.gen_gcd_qa, [3, 9], '3 9', '3'),
        (gcd.gen_gcd_qa, [100, 52], '100 52', '4'),
        (even.gen_even_qa, [5], '5', 'no'),
        (even.gen_even_qa, [6], '6', 'yes'),
        (prime.gen_prime_qa, [5], '5', 'yes'),
        (prime.gen_prime_qa, [6], '6', 'no'),  # noqa: WPS317
        (
            progression.gen_progression_qa, [5, 2, 5],
            '5 7 9 11 13 .. 17 19 21 23', '15',
        ),
    ],
)
def test_gen_qa(gen_function, args, question, answer):
    qa = gen_function(*args)
    assert qa.question == question
    assert qa.correct_answer == answer


@pytest.mark.parametrize(
    'gen_function',
    [
        calculator.gen_random_qa,
        gcd.gen_random_qa,
        even.gen_random_qa,
        prime.gen_random_qa,
        progression.gen_random_qa,
    ],
)
def test_gen_random_qa_not_failing(gen_function):
    gen_function()
