import json
from dataclasses import asdict
from typing import TYPE_CHECKING

import app
from app.model.schemas.config_schema import ConfigSchema, GameSchema

if TYPE_CHECKING:
    from pathlib import Path


class ConfigManager:
    """Configuration manager module for the games in this program."""

    def __init__(self) -> None:
        """file_name: Name of the JSON file, including extension."""
        self.config: ConfigSchema
        self._config_path: Path = app.SETTINGS_DIR / "config.json"
        self._load()

    def _load(self) -> None:
        """Loads game config from JSON file to memory."""
        if self._config_path.exists():
            with self._config_path.open("r", encoding="utf-8") as f:
                data: dict = json.load(f)
                self.config = ConfigSchema(
                    **{k: GameSchema(**v) for k, v in data.items()},
                )
        else:
            self.config = ConfigSchema()
            self.save()

    def save(self) -> None:
        """Saves changes from memory to JSON file."""
        with self._config_path.open("w", encoding="utf-8") as f:
            json.dump(asdict(self.config), f, indent=4)
