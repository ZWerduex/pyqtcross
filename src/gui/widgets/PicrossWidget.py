
import PyQt6.QtWidgets as wid

import picross as p
from .HintCell import HintCell
from .GridCell import GridCell


__all__ = ['PicrossWidget']


class PicrossWidget(wid.QWidget):

    def __init__(self, picross: p.Picross) -> None:
        wid.QWidget.__init__(self)
        self.__picross = picross
        self.__layout = wid.QGridLayout()
        self.__layout.setSpacing(0)

        maxLenRowHints = max([len(hints) for hints in picross.rowHints])
        maxLenColHints = max([len(hints) for hints in picross.colHints])

        # Row hints
        for row, hints in enumerate(picross.rowHints):
            # Add empty hints to the left to right align
            while len(hints) < maxLenRowHints:
                hints.insert(0, -1)
            for i, hint in enumerate(hints):
                cell = HintCell(str(hint) if hint != -1 else '')
                cell.setFixedSize(20, 20)
                self.__layout.addWidget(cell, maxLenColHints + row, i)

        # Col hints
        for col, hints in enumerate(picross.colHints):
            # Add empty hints to the top to bottom align
            while len(hints) < maxLenColHints:
                hints.insert(0, -1)
            for i, hint in enumerate(hints):
                cell = HintCell(str(hint) if hint != -1 else '')
                cell.setFixedSize(20, 20)
                self.__layout.addWidget(cell, i, maxLenRowHints + col)

        # Grid cells
        group = True
        for i in range(picross.height):
            if i % 5 == 0:
                group = not group
            for j in range(picross.width):
                if j % 5 == 0:
                    group = not group
                cell = GridCell(group)
                cell.setFixedSize(20, 20)
                self.__layout.addWidget(cell, i + maxLenColHints, j + maxLenRowHints)

        self.setLayout(self.__layout)