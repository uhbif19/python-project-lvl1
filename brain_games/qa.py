"""Module for QA dataclass."""

from collections import namedtuple

# Pair of question and expected answer. To be asked to user in quiz game.

QA = namedtuple('QA', ['question', 'correct_answer'])
