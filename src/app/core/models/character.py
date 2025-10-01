from pathlib import Path
from typing import TYPE_CHECKING

from app.core.models.game import Game

if TYPE_CHECKING:
    from app.core.models.mod import Mod


class Character:
    """Model class representation of a character."""

    def __init__(self, path: Path, name: str, game: Game) -> None:
        """Model class representation of a character.

        Args:
            path (Path): full path to the character folder.
            name (str): name of the character.
            game (Game): game this character belongs to.

        """
        self.path: Path = path
        self.name: str = name
        self.game: Game = game
        self.mods: list[Mod] = []

    def enable_all(self) -> None:
        """Enables all mods for this character."""
        for mod in self.mods:
            mod.enable()

    def disable_all(self) -> None:
        """Disables all mods for this character."""
        for mod in self.mods:
            mod.disable()
