#!/usr/bin/env python
"""Starting Brain Calculator game."""

from brain_games import engine
from brain_games.games import calculator


def main():
    """Start Brain Calculator game in CLI."""
    engine.do_quiz_as_cli_app(
        calculator.HELP_TEXT,
        calculator.gen_random_calculator_qa,
    )


if __name__ == '__main__':
    main()
