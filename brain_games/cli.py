"""Helpers for working with CLI."""

import prompt
from brain_games.games_logic import QA, GameQABuilder


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
        answer_correct = ask_question(qa)
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
    user_name = welcome_user()
    do_quiz(
        qa_builder=qa_builder,
        user_name=user_name,
    )
