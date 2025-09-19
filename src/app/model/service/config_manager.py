import json
from typing import Any

import app
from app.model.schemas.config_schema import ConfigSchema


class ConfigManager:
    """Configuration manager module for the games in this program."""

    def __init__(self, file_name: str) -> None:
        """Each game should have its own separate ConfigManager instance.

        file_name: Name of the JSON file, including extension.
        """
        self._config: ConfigSchema | None = None
        self._config_path = app.SETTINGS_DIR / file_name
        self._load_config()

    def _load_config(self) -> None:
        """Loads game config from JSON file."""
        if self._config_path.exists():
            with self._config_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self._config = ConfigSchema(**data)
        else:
            self._config = ConfigSchema()
            self._save_config()
            self._load_config()

    def _save_config(self) -> None:
        """Saves changes to JSON file."""
        with self._config_path.open("w", encoding="utf-8") as f:
            json.dump(self._config.__dict__, f, indent=4)

    def get(self, key: str) -> Any:
        """Returns config value given the key."""
        return getattr(self._config, key)

    def set(self, key: str, value: Any) -> None:
        """Set config value given the key."""
        setattr(self._config, key, value)
        self._save_config()
