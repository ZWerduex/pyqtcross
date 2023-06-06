
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

from .Cell import Cell


__all__ = ['GridCell']


class GridCell(Cell):

    def __init__(self, colored: bool) -> None:
        Cell.__init__(self)

        self.__state = -1

        if colored:
            color = 'cecece'
        else:
            color = 'FFFFFF'

        self.setStyleSheet(f'background-color: #{color}; border: 1px solid #171b25;')
        
    def fill(self) -> None:
        self.clear()
        w, h = self.width(), self.height()
        offset = 5
        self.scene.addRect(
            0, 0, w - offset, h - offset,
            brush = gui.QBrush(gui.QColor(23, 27, 37), Qt.BrushStyle.SolidPattern)
        )

    def empty(self) -> None:
        self.clear()
        self.crossout()

    def mousePressEvent(self, event: gui.QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            if self.__state == 1:
                self.__state = -1
                self.clear()
            else:
                self.__state = 1
                self.fill()
        elif event.button() == Qt.MouseButton.RightButton:
            if self.__state == 0:
                self.__state = -1
                self.clear()
            else:
                self.__state = 0
                self.empty()