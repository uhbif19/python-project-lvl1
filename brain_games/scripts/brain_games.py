#!/usr/bin/env python
"""Main script, starting the games."""

from brain_games import cli


def main():
    """Start games in CLI."""
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
