from abc import abstractmethod
from pathlib import Path

from .base_sprite_loader import BaseSpriteLoader


class AbstractFloorSheet(BaseSpriteLoader):
    @property
    @abstractmethod
    def biome_name(self) -> str:
        raise NotImplementedError

    @property
    def _sprite_sheet_path(self) -> Path:
        return Path(f"Data/Textures/floor_{self.biome_name}.png")

    """
    Biome sheets are 12x12 128 pixel squares
    """
    _chunk_size = 128
    _chunk_map = {
        "push_block": (7, 0, 8, 1),
        "bone_block": (10, 2, 11, 3),
        "ladder": (4, 0, 5, 2),
        "ladder_plat": (4, 2, 5, 4),
        "entrance": (0, 7, 3, 9),
        # Exit is not on even 128 pixel boundaries RIP even numbers
        "exit": (9.5, 0, 11.5, 3),
        "door2": (8, 6, 10, 8),
        # door2_secret is the same as door2, but gets dirt/push_block in front
        "door2_secret": (8, 6, 10, 8),
        "spikes": (5, 9, 6, 10),
        "altar": (10, 0, 12, 2),
        "dirt": (0, 0, 4, 7),
        "ghist_door2": (10, 6, 12, 8),
    }