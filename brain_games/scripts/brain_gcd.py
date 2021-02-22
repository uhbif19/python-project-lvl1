#!/usr/bin/env python
"""Starting Brain GCD game."""

from brain_games import cli, games_logic


def main():
    """Start Brain GCD game in CLI."""
    cli.do_quiz_as_cli_app(games_logic.GCDQABuilder)


if __name__ == '__main__':
    main()
