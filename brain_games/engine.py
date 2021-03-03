"""Whole game cycle, independent of QA generated for specific game."""

from types import ModuleType

from brain_games import cli


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
        qa = game_module.gen_random_qa()
        answer_correct = cli.ask_question(qa)
        if not answer_correct:
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
