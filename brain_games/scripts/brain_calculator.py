#!/usr/bin/env python
"""Starting Brain Calculator game."""

from brain_games import cli
from brain_games.games import calculator


def main():
    """Start Brain Calculator game in CLI."""
    cli.perform_quiz_as_standalone_cli_app(calculator)


if __name__ == '__main__':
    main()
