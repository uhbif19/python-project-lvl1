#!/usr/bin/env python
"""Script for Brain Even Game."""

from brain_games import cli, games_logic


def main():
    """Start Brain Even game in CLI."""
    user_name = cli.welcome_user()
    cli.do_quiz(
        qa_builder=games_logic.BrainEvenQABuilder,
        user_name=user_name,
        until_correct_answers=3,
    )


if __name__ == '__main__':
    main()
