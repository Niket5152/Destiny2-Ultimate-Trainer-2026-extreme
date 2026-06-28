from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class OffsetData:
    GOD_MODE: int = 0x2a4b48b
    UNLIMITED_AMMO: int = 0x2a4b5d0
    ESP_ENABLED: int = 0x2a4b631
    SPEED_HACK: int = 0x2a4b6ee
    NO_RECOIL: int = 0x2a4b824
    LOOT_UNLOCKER: int = 0x2a4b79c
    BOUNTY_COMPLETE: int = 0x2a4b837
    AIMBOT_FOV: int = 0x2a4b9bd
    PLAYER_BASE: int = 0x1e8a428
    PLAYER_OFFSETS: list = field(default_factory=lambda: [0x0, 0x30, 0x8, 0x20])
    VERSION_OFFSETS: Dict[str, Dict[str,int]] = field(default_factory=lambda: {
        "2026.06.28-856": {
            "GOD_MODE": 0x2a4b48b,
            "UNLIMITED_AMMO": 0x2a4b5d0,
        }
    })
    def get_for_version(self, ver): return self.VERSION_OFFSETS.get(ver, {})

offsets = OffsetData()
