"""Working with CLI and game cycle realization."""

from types import ModuleType

import prompt
from brain_games.qa import QA


def welcome_user_and_ask_his_name() -> str:
    """
    Do initial dialog, asking user for his name and welcoming him in CLI.

    Returns:
        Username returned by user
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def perform_quiz(
    game: ModuleType,
    user_name: str,
    rounds_to_win: int = 3,
):
    """
    Perform quiz asking user questions.

    Args:
        game: module with game implementation, submodule of
        `brain_games.games`. Used to generate QA and QA solving help text.
        user_name: used in messages to user
        rounds_to_win: how many question will be asked (only if user
            answers correctly) until he will be declared winner
    """
    print(game.HOW_TO_ANSWER_INSTRUCTION)
    for _ in range(rounds_to_win):
        qa: QA = game.gen_random_qa()
        print('Question: {0}'.format(qa.question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == qa.correct_answer:
            print('Correct!')
        else:
            print(
                (
                    "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
                    + "Let's try again, {2}!"
                ).format(
                    user_answer, qa.correct_answer, user_name,
                ),
            )
            return
    print('Congratulations, {0}!'.format(user_name))


def perform_quiz_as_standalone_cli_app(game: ModuleType):
    """
    Run CLI app performing quiz.

    That means asking user its name and then performing quiz.

    Args:
        game: module with game implementation, submodule of
        `brain_games.games`. Used to generate QA and QA solving help text.
    """
    user_name = welcome_user_and_ask_his_name()
    perform_quiz(game=game, user_name=user_name)
