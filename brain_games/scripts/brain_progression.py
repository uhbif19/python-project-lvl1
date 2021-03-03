#!/usr/bin/env python
"""Script for Brain Progression Game."""

from brain_games import engine
from brain_games.games import progression


def main():
    """Start Brain Progression game in CLI."""
    engine.do_quiz_as_cli_app(progression)


if __name__ == '__main__':
    main()
