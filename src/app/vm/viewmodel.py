from pathlib import Path

from app.config_manager import ConfigManager
from app.model.character import Character
from app.model.game import Game


class ViewModel:
    """Viewmodel for the main window of the program."""

    def __init__(self) -> None:
        """Viewmodel for the main window of the program."""
        self.cm: ConfigManager = ConfigManager()
        self.games: list[Game] = [
            Game(Path(v["Mods path"]), k) for k, v in self.cm.config.items()
        ]
        self.current_game: Game | None = None
        self.current_character: Character | None = None

    def get_game_names(self) -> list[str]:
        return [game.name for game in self.games]

    def select_game(self, name: str) -> list[str]:
        self.current_game = next(
            (game for game in self.games if game.name == name), None,
        )
        if not self.current_game:
            return []
        self.current_game.fetch_characters()
        return [c.name for c in self.current_game.characters]

    def select_character(self, name: str) -> list[str]:
        if not self.current_game:
            return []
        self.current_character = next(
            (c for c in self.current_game.characters if c.name == name), None,
        )
        if not self.current_character:
            return []
        self.current_character.fetch_mods()
        return [m.name for m in self.current_character.mods]

    def update_current_game_path(self, new_path: str) -> None:
        if not self.current_game:
            return
        self.current_game.path = Path(new_path)
        self.cm.config[self.current_game.name]["Mods path"] = new_path
        self.cm.save()

    def get_game_path(self, name: str) -> str:
        game = next((g for g in self.games if g.name == name), None)
        return str(game.path) if game else ""
