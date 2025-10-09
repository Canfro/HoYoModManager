from pathlib import Path


class Mod:
    """Model class representation of a mod."""

    def __init__(self, path: Path, name: str) -> None:
        """Model class representation of a mod.

        Args:
            path (Path): full path to the mod .ini file.
            name (str): name of the mod.
            character (Character): character this mod belongs to.

        """
        self.path: Path = path
        self.name: str = name
        self.is_enabled: bool = True

    def enable(self) -> None:
        """Enables mod."""
        if not self.is_enabled:
            new_name = self.path.name.replace("DISABLED ", "", 1)
            new_path = self.path.with_name(new_name)
            self.path = self.path.rename(new_path)
        self.is_enabled = True

    def disable(self) -> None:
        """Disables mod."""
        if self.is_enabled and not self.path.name.startswith("DISABLED "):
            new_name = f"DISABLED {self.path.name}"
            new_path = self.path.with_name(new_name)
            self.path = self.path.rename(new_path)
        self.is_enabled = False
