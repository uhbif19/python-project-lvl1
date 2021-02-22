#!/usr/bin/env python
"""Starting Brain Prime game."""

from brain_games import cli, qa_builders


def main():
    """Start Brain Prime game in CLI."""
    cli.do_quiz_as_cli_app(qa_builders.PrimeQABuilder)


if __name__ == '__main__':
    main()
