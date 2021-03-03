#!/usr/bin/env python
"""Starting Brain Prime game."""

from brain_games import cli
from brain_games.games import prime


def main():
    """Start Brain Prime game in CLI."""
    cli.do_quiz_as_cli_app(prime)


if __name__ == '__main__':
    main()
