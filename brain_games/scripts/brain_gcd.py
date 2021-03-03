#!/usr/bin/env python
"""Starting Brain GCD game."""

from brain_games import cli
from brain_games.games import gcd


def main():
    """Start Brain GCD game in CLI."""
    cli.do_quiz_as_cli_app(gcd)


if __name__ == '__main__':
    main()
