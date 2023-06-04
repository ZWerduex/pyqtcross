
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid


__all__ = ['Cell']


class Cell(wid.QGraphicsView):

    def __init__(self) -> None:
        wid.QGraphicsView.__init__(self)

        self.__scene = wid.QGraphicsScene()
        self.setScene(self.__scene)

        self.setMinimumSize(50, 50)
        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setRenderHint(gui.QPainter.RenderHint.Antialiasing)

    @property
    def scene(self) -> wid.QGraphicsScene:
        return self.__scene

    def crossout(self) -> None:
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