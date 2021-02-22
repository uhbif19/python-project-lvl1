#!/usr/bin/env python
"""Starting Brain GCD game."""

from brain_games import cli, qa_builders


def main():
    """Start Brain GCD game in CLI."""
    cli.do_quiz_as_cli_app(qa_builders.GCDQABuilder)


if __name__ == '__main__':
    main()
