from app.model.service.config_manager import ConfigManager


class ModManager:
    """Core module where mod logic is handled."""

    def __init__(self, cm: ConfigManager) -> None:
        """config: ConfigManager instance."""
        self._cm = cm
        self._config = cm.config
