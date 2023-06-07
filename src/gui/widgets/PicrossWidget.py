
import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import picross as p
from .HintCell import HintCell
from .GridCell import GridCell


__all__ = ['PicrossWidget']


class PicrossWidget(wid.QWidget):

    completed = core.pyqtSignal()

    def __init__(self, cellSize: int, picross: p.Picross) -> None:
        wid.QWidget.__init__(self)
        self.__picross = picross
        self.__layout = wid.QGridLayout()
        self.__layout.setSpacing(0)
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSizeConstraint(wid.QLayout.SizeConstraint.SetFixedSize)
        self.__strictCheck = False

        maxLenRowHints = max([len(hints) for hints in picross.rowHints])
        maxLenColHints = max([len(hints) for hints in picross.colHints])

        # Row hints
        for row, hints in enumerate(picross.rowHints):
            # Add empty hints to the left to right align
            while len(hints) < maxLenRowHints:
                hints.insert(0, -1)
            for i, hint in enumerate(hints):
                cell = HintCell(cellSize, str(hint) if hint != -1 else '')
                self.__layout.addWidget(cell, maxLenColHints + row, i)

        # Col hints
        for col, hints in enumerate(picross.colHints):
            # Add empty hints to the top to bottom align
            while len(hints) < maxLenColHints:
                hints.insert(0, -1)
            for i, hint in enumerate(hints):
                cell = HintCell(cellSize, str(hint) if hint != -1 else '')
                self.__layout.addWidget(cell, i, maxLenRowHints + col)

        # Grid cells
        whiteCell = False
        for y in range(picross.height):
            for x in range(picross.width):
                whiteCell = (x // 5) % 2 != (y // 5) % 2 # Thanks ChatGPT, I was stuck on this for 2 hours
                cell = GridCell(cellSize, x, y, whiteCell)
                cell.clicked.connect(self.onGridCellClicked)
                self.__layout.addWidget(cell, y + maxLenColHints, x + maxLenRowHints)

        self.setLayout(self.__layout)

    def setStrictCheck(self, strictCheck: bool) -> None:
        self.__strictCheck = strictCheck

    def onGridCellClicked(self, x: int, y: int, state: int) -> None:
        if state == 1:
            self.__picross.fillCell(x, y)
        elif state == 0:
            self.__picross.emptyCell(x, y)
        else:
            self.__picross.clearCell(x, y)
            
        if self.__picross.isCompleted(self.__strictCheck):
            self.completed.emit()