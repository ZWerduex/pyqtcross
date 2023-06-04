from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

from .Cell import Cell


__all__ = ['HintCell']


class HintCell(Cell):

    def __init__(self, hint: str) -> None:
        Cell.__init__(self)
        self.__isEmpty = hint == ''
        self.__text = self.__scene.addText(
            hint,
            gui.QFont('Arial', 10, 1)
        )

        self.setStyleSheet('background-color: #ddb07a;')

        self.setFrameShape(wid.QFrame.Shape.NoFrame)
        self.setRenderHint(gui.QPainter.RenderHint.TextAntialiasing)

    def crossout(self) -> None:
        if not self.__isEmpty:
            self.clear()
            super().crossout()

    def clear(self) -> None:
        for item in self.__scene.items():
            if item != self.__text:
                self.__scene.removeItem(item)