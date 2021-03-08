#!/usr/bin/env python
"""Script for Brain Progression Game."""

from brain_games import cli
from brain_games.games import progression


def main():
    """Start Brain Progression game in CLI."""
    cli.perform_quiz_as_standalone_cli_app(progression)


if __name__ == '__main__':
    main()
