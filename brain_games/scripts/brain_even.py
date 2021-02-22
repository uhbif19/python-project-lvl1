#!/usr/bin/env python
"""Script for Brain Even Game."""

from brain_games import cli, games_logic


def main():
    """Start Brain Even game in CLI."""
    cli.do_quiz_as_cli_app(games_logic.BrainEvenQABuilder)


if __name__ == '__main__':
    main()
