"""Helpers for working with CLI."""

import prompt


def welcome_user():
    """Do initial dialog, asking user for his name and welcoming him in CLI."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
