#!/usr/bin/env python
"""Main script, starting the games."""

from brain_games import cli


def main():
    """Start games in CLI."""
    cli.welcome_user_and_ask_his_name()


if __name__ == '__main__':
    main()
