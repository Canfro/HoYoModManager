from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GameConfigSchema:
    """Schema for game config.

    Args:
        mods_path (str): path to the XXMI mods folder for the game.

    """

    mods_path: str = ""

@dataclass
class FullConfigSchema:
    """Schema for config file.

    Args:
        gi (GameConfigSchema): Genshin Impact config schema.
        hsr (GameConfigSchema): Honkai Star Rail config schema.
        zzz (GameConfigSchema): Zenless Zone Zero config schema.
        wuwa (GameConfigSchema): Wuthering Waves config schema.

    """

    gi: GameConfigSchema = field(default_factory=GameConfigSchema)
    hsr: GameConfigSchema = field(default_factory=GameConfigSchema)
    zzz: GameConfigSchema = field(default_factory=GameConfigSchema)
    wuwa: GameConfigSchema = field(default_factory=GameConfigSchema)
