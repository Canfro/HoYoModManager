import json
from pathlib import Path


class ConfigManager:
    """Configuration manager for the games in this program."""

    def __init__(self) -> None:
        """Configuration manager module for the games in this program."""
        self.config: dict[str, dict[str, str]]
        self.config_path: Path = Path("config/config.json")
        self.load()

    def load(self) -> None:
        """Loads game config from JSON file to memory."""
        if self.config_path.exists():
            with self.config_path.open("r", encoding="utf-8") as f:
                self.config = json.load(f)
        else:
            self.config = self.games()
            self.save()

    def save(self) -> None:
        """Saves changes from memory to JSON file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with self.config_path.open("w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def games(self) -> dict[str, dict[str, str]]:
        """Games present in the program and their config.

        New games should be added here.
        """
        return {
            "Genshin Impact": self.game_config(),
            "Honkai: Star Rail": self.game_config(),
            "Zenless Zone Zero": self.game_config(),
            "Wuthering Waves": self.game_config(),
        }

    @staticmethod
    def game_config() -> dict[str, str]:
        """Default game config."""
        return {
            "Mods path": "",
        }
