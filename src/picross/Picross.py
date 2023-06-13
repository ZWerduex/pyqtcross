import copy
import numpy as np

from .PicrossModel import PicrossModel


__all__ = ['Picross']


class Picross():

    def __init__(self, model: PicrossModel) -> None:
        self.__modelResp = model
        self.__userModel = model.blankCopy()
        self.__rowHints = self.__computeHints(model.grid.tolist())
        self.__colHints = self.__computeHints(model.grid.T.tolist())

    @property
    def name(self) -> str:
        return self.__modelResp.name

    @property
    def width(self) -> int:
        return self.__modelResp.width
    
    @property
    def height(self) -> int:
        return self.__modelResp.height
    
    @property
    def rowHints(self) -> list[list[int]]:
        return copy.deepcopy(self.__rowHints)
    
    @property
    def colHints(self) -> list[list[int]]:
        return copy.deepcopy(self.__colHints)
    
    @property
    def model(self) -> PicrossModel:
        return self.__modelResp

    def __computeHints(self, grid: list[list[int]]) -> list[list[int]]:
        # Compute hints for each row
        hints = []
        for seq in grid:
            counts = []
            cpt = 0
            # Count length of each sequence
            for cell in seq:
                # If cell is filled, a sequence is still going
                if cell == 1:
                    cpt += 1
                # If cell is empty, a sequence is over
                elif cpt > 0:
                    counts.append(cpt)
                    cpt = 0
            # Do not forget to add last counter to list
            if cpt > 0:
                counts.append(cpt)
            # If sequence is an empty line, add 0 to list
            if len(counts) == 0:
                counts.append(0)
            hints.append(counts)
        return hints
    
    def isCompleted(self, strictCheck: bool = False) -> bool:
        return self.__userModel.isCorrect(self.__modelResp, strictCheck)
    
    def fillCell(self, x: int, y: int) -> None:
        self.__userModel.fillCell(x, y)

    def emptyCell(self, x: int, y: int) -> None:
        self.__userModel.emptyCell(x, y)

    def clearCell(self, x: int, y: int) -> None:
        self.__userModel.clearCell(x, y)

    def clear(self) -> None:
        self.__userModel.clear()