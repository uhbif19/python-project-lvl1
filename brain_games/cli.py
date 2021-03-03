"""Working with CLI and game cycle realization."""

from types import ModuleType

import prompt
from brain_games import cli
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


def do_quiz(
    game_module: ModuleType,
    user_name: str,
    until_correct_answers: int = 3,
):
    """
    Perform quiz with questions.

    Args:
        game_module: module with game implementation, submodule of
        `brain_games.games`. Used to generate QA and QA solving help text.
        user_name: used in messages to user
        until_correct_answers: asking questions such times in row or until
          user fails
    """
    print(game_module.HOW_TO_ANSWER_INSTRUCTION)
    for _ in range(until_correct_answers):
        qa: QA = game_module.gen_random_qa()
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
        if not user_was_correct:
            print("Let's try again, {0}!".format(user_name))
            return
    print('Congratulations, {0}!'.format(user_name))


def do_quiz_as_cli_app(game_module: ModuleType):
    """
    Perform quiz with welcome dialog.

    Args:
        game_module: module with game implementation, submodule of
        `brain_games.games`. Used to generate QA and QA solving help text.
    """
    user_name = cli.welcome_user()
    do_quiz(game_module=game_module, user_name=user_name)
