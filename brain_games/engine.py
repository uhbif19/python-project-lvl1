"""Whole game cycle, independent of QA generated for specific game."""

from brain_games import cli
from brain_games.qa_builders.abstract import GameQABuilder


def do_quiz(
    qa_builder: GameQABuilder,
    user_name: str,
    until_correct_answers: int = 3,
):
    """
    Perform quiz with questions.

    Args:
        qa_builder: used to build applicable QA and show quiz help text
        user_name: used in messages to user
        until_correct_answers: asking questions such times in row or until
          user fails
    """
    if qa_builder.help_text:
        print(qa_builder.help_text)
    for _ in range(until_correct_answers):
        qa = qa_builder.from_random().get_result()
        answer_correct = cli.ask_question(qa)
        if not answer_correct:
            print("Let's try again, {0}!".format(user_name))
            return
    print('Congratulations, {0}!'.format(user_name))


def do_quiz_as_cli_app(qa_builder: GameQABuilder):
    """
    Perform quiz with welcome dialog.

    Args:
        qa_builder: used to build applicable QA and show quiz help text
    """
    user_name = cli.welcome_user()
    do_quiz(
        qa_builder=qa_builder,
        user_name=user_name,
    )
