import numpy as np

from .PicrossModel import PicrossModel


__all__ = ['Picross']


class Picross():

    def __init__(self, model: PicrossModel) -> None:
        self.__modelResp = model
        self.__userModel = model.blankCopy()
        self.__rowHints = self.__computeHints(model.grid.tolist())
        self.__colHints = self.__computeHints(model.grid.T.tolist())

    def __computeHints(self, grid: np.ndarray) -> list:
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