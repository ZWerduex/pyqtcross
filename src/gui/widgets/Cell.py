
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

__all__ = ['Cell']


class Cell(wid.QGraphicsView):

    def __init__(self, colored: bool) -> None:
        wid.QGraphicsView.__init__(self)

        self.__scene = wid.QGraphicsScene()
        self.__state = -1

        if colored:
            color = 'cecece'
        else:
            color = 'FFFFFF'

        self.setScene(self.__scene)
        self.setStyleSheet(f'background-color: #{color}; border: 1px solid #171b25;')
        self.setMinimumSize(50, 50)
        
    def fill(self) -> None:
        self.clear()
        w, h = self.width(), self.height()
        offset = 5
        self.__scene.addRect(
            0, 0, w - offset, h - offset,
            brush = gui.QBrush(gui.QColor(23, 27, 37), Qt.BrushStyle.SolidPattern)
        )

    def empty(self) -> None:
        self.clear()
        w, h = self.width(), self.height()
        offset = 15
        self.__scene.addLine(
            0, 0, w - offset, h - offset,
            pen = gui.QPen(gui.QColor(23, 27, 37), 2, Qt.PenStyle.SolidLine)
        )
        self.__scene.addLine(
            0, h - offset, w - offset, 0,
            pen = gui.QPen(gui.QColor(23, 27, 37), 2, Qt.PenStyle.SolidLine)
        )

    def clear(self) -> None:
        for item in self.__scene.items():
            self.__scene.removeItem(item)

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