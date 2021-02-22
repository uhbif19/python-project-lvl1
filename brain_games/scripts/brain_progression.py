#!/usr/bin/env python
"""Script for Brain Progression Game."""

from brain_games import cli, qa_builders


def main():
    """Start Brain Progression game in CLI."""
    cli.do_quiz_as_cli_app(qa_builders.ProgressionQABuilder)


if __name__ == '__main__':
    main()
