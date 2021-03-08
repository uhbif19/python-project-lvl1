#!/usr/bin/env python
"""Script for Brain Even Game."""

from brain_games import cli
from brain_games.games import even


def main():
    """Start Brain Even game in CLI."""
    cli.perform_quiz_as_standalone_cli_app(even)


if __name__ == '__main__':
    main()
