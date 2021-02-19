"""Helpers for working with CLI."""

import prompt


def welcome_user():
    """Ask user for his name in CLI and welcome him."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
