from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import PicrossModel

import numpy as np
import copy


__all__ = ['PicrossModel']


class PicrossModel():

    @staticmethod
    def fromGrid(name: str, grid: list[list[int]]) -> PicrossModel:
        for row in grid:
            if len(row) != len(grid[0]):
                raise ValueError('Grid must be a rectangle')
        p = PicrossModel(name, len(grid[0]), len(grid))
        p.__grid = np.array(grid)
        # Check if grid contains only 0 and 1
        if not np.all(np.isin(p.__grid, [0, 1])):
            raise ValueError('Grid must only contain 0 and 1')
        return p

    def __init__(self, name: str, width: int, height: int) -> None:
        self.__name = name
        self.__grid: np.ndarray = np.full((height, width), -1)

    # Properties

    @property
    def name(self) -> str:
        return self.__name

    @property
    def grid(self) -> np.ndarray:
        return self.__grid

    @property
    def width(self) -> int:
        return self.__grid.shape[1]
    
    @property
    def height(self) -> int:
        return self.__grid.shape[0]
    
    # Methods

    def blankCopy(self) -> PicrossModel:
        return PicrossModel(self.name, self.width, self.height)
    
    def fillCell(self, x: int, y: int) -> None:
        self.__grid[y][x] = 1

    def emptyCell(self, x: int, y: int) -> None:
        self.__grid[y][x] = 0

    def clearCell(self, x: int, y: int) -> None:
        self.__grid[y][x] = -1

    def clear(self) -> None:
        self.__grid.fill(-1)

    def isCorrect(self, reference: PicrossModel, strictCheck: bool = False) -> bool:

        if strictCheck:
            if np.any(self.__grid == -1):
                return False
            
        if self.name != reference.name:
            raise ValueError('Models must share the same name')
        if self.width != reference.width or self.height != reference.height:
            raise ValueError('Grids must have the same size')
        
        norm = copy.deepcopy(self.__grid)
        norm[norm == -1] = 0
        return np.array_equal(norm, reference.grid)