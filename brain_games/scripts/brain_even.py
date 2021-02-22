#!/usr/bin/env python
"""Script for Brain Even Game."""

from brain_games import cli, qa_builders


def main():
    """Start Brain Even game in CLI."""
    cli.do_quiz_as_cli_app(qa_builders.BrainEvenQABuilder)


if __name__ == '__main__':
    main()
