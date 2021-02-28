"""Helpers for working with CLI."""

import prompt
from brain_games.qa import QA


def welcome_user() -> str:
    """
    Do initial dialog, asking user for his name and welcoming him in CLI.

    Returns:
        Username returned by user
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def ask_question(qa: QA) -> bool:
    """
    Ask user question and check if answer is correct.

    Args:
        qa: QA which will be asked

    Returns:
        If user answered correctly
    """
    print('Question: {0}'.format(qa.question))
    user_answered = prompt.string('Your answer: ')
    user_was_correct = user_answered == qa.correct_answer
    correctnes_message = (
        'Correct!'
        if user_was_correct
        else (
            "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answered, qa.correct_answer,
            )
        )
    )
    print(correctnes_message)
    return user_was_correct
