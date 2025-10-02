from pathlib import Path
from secrets import randbelow

from app.core.models.game import Game
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

    def randomize(self) -> None:
        """Disables all mods and enables one randomly."""
        self.disable_all()
        idx: int = randbelow(len(self.mods))
        self.mods[idx].enable()

    def fetch_mods(self) -> bool:
        """Fetches mod list from disk.

        Returns:
            True: mods fetched successfully.
            False: aborted because character path doesn't exist.

        """
        self.mods.clear()
        if not self.path.exists():
            return False
        for entry in self.path.iterdir():
            if entry.is_dir():
                mod = Mod(path=entry, name=entry.name, character=self)
                self.mods.append(mod)
        return True
