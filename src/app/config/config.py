import json
from typing import Any

import app


class ConfigManager:
    """Configuration manager module for the games in this program."""

    def __init__(self, file_name: str) -> None:
        """Each game should have its own separate ConfigManager instance.

        -file_name: Name of the JSON file, including extension.
        """
        self._config: dict[str, Any] = {}
        self._config_path = app.SETTINGS_DIR / file_name
        self._load_config()

    def _load_config(self) -> None:
        """Loads game config from JSON file."""
        if self._config_path.exists():
            with self._config_path.open("r", encoding="utf-8") as f:
                self._config = json.load(f)
        else:
            self._config = self._default_config()
            self._save_config()
            self._load_config()

    def _save_config(self) -> None:
        """Saves changes to JSON file."""
        with self._config_path.open("w", encoding="utf-8") as f:
            json.dump(self._config, f, indent=4)

    def _default_config(self) -> dict:
        """Default config for the current game."""
        return {"path": ""}

    def get(self, key: str) -> Any:
        """Returns config value given the key."""
        return self._config[key]

    def set(self, key: str, value: Any) -> None:
        """Set config value given the key."""
        self._config[key] = value
        self._save_config()
