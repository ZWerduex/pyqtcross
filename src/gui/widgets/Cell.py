
import math

from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid


__all__ = ['Cell']


class Cell(wid.QGraphicsView):

    def __init__(self, size: int) -> None:
        wid.QGraphicsView.__init__(self)

        self.cellSize = size
        self.__crossOffset = math.ceil(self.cellSize * 0.25)
        self.__fillOffset = math.ceil(self.cellSize * 0.07)
        
        # QGraphicsView properties
        self.setFixedSize(self.cellSize, self.cellSize)
        
        self.setFrameShape(wid.QFrame.Shape.NoFrame)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.setRenderHint(gui.QPainter.RenderHint.Antialiasing)
        self.setRenderHint(gui.QPainter.RenderHint.TextAntialiasing)

        # QGraphicsScene properties
        self.__scene = wid.QGraphicsScene()
        self.setScene(self.__scene)
        self.__scene.setSceneRect(0, 0, self.cellSize, self.cellSize)
    
    def setBackgroundRGB(self, r: int, g: int, b: int) -> None:
        self.setStyleSheet(f'background-color: rgb({r}, {g}, {b});')
    
    def drawBorder(self, r: int, g: int, b: int, alpha: int = 255) -> wid.QGraphicsRectItem:
        w, h = self.width(), self.height()
        return self.__scene.addRect(
            0, 0, w, h,
            pen = gui.QPen(gui.QColor(r, g, b, alpha), 0.5, Qt.PenStyle.SolidLine)
        )
    
    def drawCross(self, r: int, g: int, b: int, alpha: int = 255) -> tuple[wid.QGraphicsLineItem, wid.QGraphicsLineItem]:
        w, h = self.width(), self.height()
        return (
            self.__scene.addLine(
                self.__crossOffset, self.__crossOffset,
                w - self.__crossOffset, h - self.__crossOffset,
                pen = gui.QPen(gui.QColor(r, g, b, alpha), 1.5, Qt.PenStyle.SolidLine)
            ), 
            self.__scene.addLine(
                self.__crossOffset, h - self.__crossOffset,
                w - self.__crossOffset, self.__crossOffset,
                pen = gui.QPen(gui.QColor(r, g, b, alpha), 1.5, Qt.PenStyle.SolidLine)
            )
        )

    def drawRectangle(self,
                      r: int, g: int, b: int,
                      alpha: int = 255,
                      withOffset: bool = True
    ) -> wid.QGraphicsRectItem:
        x = self.__fillOffset if withOffset else 0
        y = self.__fillOffset if withOffset else 0
        w, h = self.width(), self.height()
        w = w - 2 * self.__fillOffset if withOffset else w
        h = h - 2 * self.__fillOffset if withOffset else h
        return self.__scene.addRect(
            x, y, w, h,
            brush = gui.QBrush(gui.QColor(r, g, b, alpha), Qt.BrushStyle.SolidPattern)
        )
    
    def drawText(self, text: str, r: int, g: int, b: int) -> wid.QGraphicsTextItem:
        font = gui.QFont()
        font.setFamily('Segoe UI')
        font.setPixelSize(12)

        item = self.__scene.addText(text, font)
        item.setPos(
            (self.width() - item.boundingRect().width()) / 2,
            (self.height() - item.boundingRect().height()) / 2
        )
        item.setDefaultTextColor(gui.QColor(r, g, b))
        return item
    
    def clear(self, itemsToKeep: list[wid.QGraphicsItem] = ...) -> None:
        if itemsToKeep is ...:
            itemsToKeep = []
        for item in self.__scene.items():
            if item not in itemsToKeep:
                self.__scene.removeItem(item)