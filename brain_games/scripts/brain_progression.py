#!/usr/bin/env python
"""Script for Brain Progression Game."""

from brain_games import cli, games_logic


def main():
    """Start Brain Progression game in CLI."""
    cli.do_quiz_as_cli_app(games_logic.ProgressionQABuilder)


if __name__ == '__main__':
    main()
