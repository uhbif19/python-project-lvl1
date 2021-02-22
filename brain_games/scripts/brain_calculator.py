#!/usr/bin/env python
"""Starting Brain Calculator game."""

from brain_games import cli, games_logic


def main():
    """Start Brain Calculator game in CLI."""
    cli.do_quiz_as_cli_app(games_logic.CalculatorQABuilder)


if __name__ == '__main__':
    main()
