from pathlib import Path

from app.model.character import Character


class Game:
    def __init__(self, path: Path, name: str) -> None:
        self.path = path
        self.name = name
        self.characters: list[Character] = []

    def enable_all(self) -> None:
        for character in self.characters:
            character.enable_all()

    def disable_all(self) -> None:
        for character in self.characters:
            character.disable_all()

    def randomize(self) -> None:
        for character in self.characters:
            character.randomize()

    def fetch_characters(self) -> bool:
        self.characters.clear()
        if not self.path.exists():
            return False
        for entry in self.path.iterdir():
            if entry.is_dir():
                character = Character(
                    path=entry,
                    name=entry.name,
                    )
                self.characters.append(character)
        return True
