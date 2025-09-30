from dataclasses import dataclass, field


@dataclass
class GameSchema:
    """Schema for game config."""

    path: str = ""

@dataclass
class ConfigSchema:
    """Available games."""

    gi: GameSchema = field(default_factory=GameSchema)
    hsr: GameSchema = field(default_factory=GameSchema)
    zzz: GameSchema = field(default_factory=GameSchema)
    wuwa: GameSchema = field(default_factory=GameSchema)
