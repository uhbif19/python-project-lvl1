"""Whole game cycle, independent of QA generated for specific game."""

from typing import Callable

from brain_games import cli


def do_quiz(
    help_text: str,
    gen_random_qa: Callable,
    user_name: str,
    until_correct_answers: int = 3,
):
    """
    Perform quiz with questions.

    Args:
        help_text: quiz help text saying how to answer QA
        gen_random_qa: used to build applicable QA
        user_name: used in messages to user
        until_correct_answers: asking questions such times in row or until
          user fails
    """
    print(help_text)
    for _ in range(until_correct_answers):
        qa = gen_random_qa()
        answer_correct = cli.ask_question(qa)
        if not answer_correct:
            print("Let's try again, {0}!".format(user_name))
            return
    print('Congratulations, {0}!'.format(user_name))


def do_quiz_as_cli_app(help_text: str, gen_random_qa: Callable):
    """
    Perform quiz with welcome dialog.

    Args:
        help_text: quiz help text saying how to answer QA
        gen_random_qa: used to build applicable QA
    """
    user_name = cli.welcome_user()
    do_quiz(
        help_text=help_text,
        gen_random_qa=gen_random_qa,
        user_name=user_name,
    )
