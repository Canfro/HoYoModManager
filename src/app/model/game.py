from pathlib import Path

from app.model.character import Character


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
        self.characters: list[Character] = []

    def enable_all(self) -> None:
        """Enables all mods for this game."""
        for character in self.characters:
            character.enable_all()

    def disable_all(self) -> None:
        """Disables all mods for this game."""
        for character in self.characters:
            character.disable_all()

    def randomize(self) -> None:
        """Disables all mods and enables one randomly for each character."""
        for character in self.characters:
            character.randomize()

    def fetch_characters(self) -> bool:
        """Fetches character list from disk.

        Returns:
            True: characters fetched successfully.
            False: aborted because game path doesn't exist.

        """
        self.characters.clear()
        if not self.path.exists():
            return False
        for entry in self.path.iterdir():
            if entry.is_dir():
                character: Character = Character(
                    path=entry,
                    name=entry.name,
                    game=self,
                    )
                self.characters.append(character)
        return True
