#!/usr/bin/env python
"""Starting Brain Prime game."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Start Brain Prime game in CLI."""
    engine.do_quiz_as_cli_app(prime.HELP_TEXT, prime.gen_random_prime_qa)


if __name__ == '__main__':
    main()
