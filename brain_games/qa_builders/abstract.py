"""Abstract class for all QA Builders."""

from abc import ABC, abstractmethod
from typing import Optional

from brain_games.qa import QA


class GameQABuilder(ABC):
    """Building QA suitable for game."""

    help_text: Optional[str]

    @classmethod
    @abstractmethod
    def from_random(cls):
        """Create builder filled with random data."""

    @abstractmethod
    def get_result(self) -> QA:
        """Return builded QA."""
