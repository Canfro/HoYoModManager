import json
from dataclasses import asdict
from pathlib import Path

from app.core.config.schemas import FullConfigSchema, GameConfigSchema


class ConfigManager:
    """Configuration manager module for the games in this program."""

    def __init__(self) -> None:
        """Configuration manager module for the games in this program."""
        self.config: FullConfigSchema
        self.config_path: Path = Path("config/config.json")
        self.load()

    def load(self) -> None:
        """Loads game config from JSON file to memory."""
        if self.config_path.exists():
            with self.config_path.open("r", encoding="utf-8") as f:
                data: dict = json.load(f)
                self.config = FullConfigSchema(
                    **{k: GameConfigSchema(**v) for k, v in data.items()},
                )
        else:
            self.config = FullConfigSchema()
            self.save()

    def save(self) -> None:
        """Saves changes from memory to JSON file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with self.config_path.open("w", encoding="utf-8") as f:
            json.dump(asdict(self.config), f, indent=4)

