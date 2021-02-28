#!/usr/bin/env python
"""Starting Brain Calculator game."""

from brain_games import engine, qa_builders


def main():
    """Start Brain Calculator game in CLI."""
    engine.do_quiz_as_cli_app(qa_builders.CalculatorQABuilder)


if __name__ == '__main__':
    main()
