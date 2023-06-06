from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

from .Cell import Cell


__all__ = ['GridCell']


class GridCell(Cell):

    def __init__(self, size: int, colored: bool) -> None:
        Cell.__init__(self, size)

        self.__state = -1
        self.__border = self.drawBorder(23, 27, 37)

        self.setBackgroundHex('cecece' if colored else 'FFFFFF')

    def mouseReleaseEvent(self, event: gui.QMouseEvent) -> None:
        self.clear(itemsToKeep=[self.__border])
        if event.button() == Qt.MouseButton.LeftButton:
            if self.__state == 1:
                self.__state = -1
            else:
                self.__state = 1
                self.drawRectangle(23, 27, 37)
        elif event.button() == Qt.MouseButton.RightButton:
            if self.__state == 0:
                self.__state = -1
            else:
                self.__state = 0
                self.drawCross(23, 27, 37)