"""Module for QA dataclass."""

from dataclasses import dataclass


@dataclass
class QA:
    """
    Pair of question and expected answer.

    Exists to be asked to user in quiz game.
    """

    question: str
    correct_answer: str
