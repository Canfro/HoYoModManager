from dataclasses import dataclass, field


@dataclass
class GameConfigSchema:
    """Schema for game config."""

    path: str = ""

@dataclass
class FullConfigSchema:
    """Schema for config file."""

    gi: GameConfigSchema = field(default_factory=GameConfigSchema)
    hsr: GameConfigSchema = field(default_factory=GameConfigSchema)
    zzz: GameConfigSchema = field(default_factory=GameConfigSchema)
    wuwa: GameConfigSchema = field(default_factory=GameConfigSchema)
