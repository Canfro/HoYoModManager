from dataclasses import field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.core.models.character import Character


class Game:
    """Model class representation of a game."""

    def __init__(self, path: Path, name: str) -> None:
        """Model class representation of a game.

        Args:
            path: full path to the game mods folder.
            name: name of the game.

        """
        self.path: Path = path
        self.name: str = name
        self.characters: list[Character] = field(default_factory=list)

