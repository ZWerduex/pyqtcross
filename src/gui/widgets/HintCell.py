
import PyQt6.QtGui as gui

from .Cell import Cell


__all__ = ['HintCell']


class HintCell(Cell):

    def __init__(self, size: int, hint: str) -> None:
        Cell.__init__(self, size)

        self.__crossed = False

        self.__text = self.drawText(hint, 23, 27, 37)
        self.setBackgroundHex('e0c48d')

    def mouseReleaseEvent(self, event: gui.QMouseEvent) -> None:
        self.clear([self.__text])
        if not self.__crossed:
            self.drawCross(23, 27, 37, 140)
        self.__crossed = not self.__crossed