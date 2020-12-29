from typing import Optional, Union

from PIL import Image
from abc import ABC, abstractmethod
from pathlib import Path

from .types import chunk_map_type


class AbstractFloorSheet(ABC):
    _sprite_sheet: Image.Image
    _base_path: Path
    _chunk_map: chunk_map_type

    @property
    @abstractmethod
    def biome_name(self) -> str:
        raise NotImplementedError

    """
    Biome sheets are 12x12 128 pixel squares
    """
    _chunk_map = {
        "push_block": (0, 7, 1, 8),
        "bone_block": (2, 10, 3, 11),
        "ladder": (0, 4, 2, 5),
        "ladder_plat": (2, 4, 4, 5),
        "entrance": (7, 0, 9, 3),
        # Exit is not on even 128 pixel boundaries RIP even numbers
        "exit": (9.5, 0, 11.5, 3),
        "door2": (6, 8, 8, 10),
        # door2_secret is the same as door2, but gets dirt/push_block in front
        "door2_secret": (6, 8, 8, 10),
    }

    def __init__(self, base_path: Path):
        self._base_path = base_path
        self._sprite_sheet = Image.open(self._base_path / self._sheet_path)

    def _get_block(
        self,
        left: Union[int, float],
        upper: Union[int, float],
        right: Union[int, float],
        lower: Union[int, float],
    ) -> Image.Image:
        """Used to get chunks of the sprite sheet."""
        bbox = tuple(map(lambda x: x * 128, (upper, left, lower, right)))
        return self._sprite_sheet.crop(bbox)

    @property
    def _sheet_path(self):
        return Path(f"Data/Textures/floor_{self.biome_name}.png")

    def get(self, name: str) -> Optional[Image.Image]:
        coords = self._chunk_map.get(name)
        if coords:
            return self._get_block(*coords)


class CaveFloorSheet(AbstractFloorSheet):
    biome_name = "cave"


class EggplantFloorSheet(AbstractFloorSheet):
    biome_name = "eggplant"