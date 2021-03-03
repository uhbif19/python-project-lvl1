#!/usr/bin/env python
"""Script for Brain Even Game."""

from brain_games import engine
from brain_games.games import even


def main():
    """Start Brain Even game in CLI."""
    engine.do_quiz_as_cli_app(even)


if __name__ == '__main__':
    main()
