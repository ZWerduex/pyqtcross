
import PyQt6.QtCore as core
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid


__all__ = ['GridCell']


class GridCell(wid.QGraphicsItem):

    clicked = core.pyqtSignal()

    def __init__(self, size: int, colored: bool, x: int, y: int) -> None:
        wid.QGraphicsItem.__init__(self)
        self.__size = size
        self.__colored = colored
        self.__x = x
        self.__y = y

        self.__state = -1

    def boundingRect(self) -> core.QRectF:
        return core.QRectF(0, 0, self.__size, self.__size)
    
    def paint(self,
              painter: gui.QPainter,
              option: wid.QStyleOptionGraphicsItem,
              widget: wid.QWidget
    ) -> None:
        rect = self.boundingRect()
        painter.setRenderHint(gui.QPainter.RenderHint.Antialiasing)

        # Cell background
        color = 'cecece' if self.__colored else 'FFFFFF'
        painter.setBrush(gui.QBrush(gui.QColor(color), Qt.BrushStyle.SolidPattern))
        painter.drawRect(rect)
        # Cell border
        painter.setPen(gui.QPen(gui.QColor(23, 27, 37), 0.5, Qt.PenStyle.SolidLine))
        painter.drawRect(rect)

        margin = int(rect.width() * 0.05)

        if self.__state == 1:
            painter.setBrush(gui.QBrush(gui.QColor(23, 27, 37), Qt.BrushStyle.SolidPattern))
            painter.drawRect(
                rect.x() + margin,rect.y() + margin,
                rect.width() - 2 * margin, rect.height() - 2 * margin
            )
        elif self.__state == 0:
            painter.setPen(gui.QPen(gui.QColor(23, 27, 37), 1.5, Qt.PenStyle.SolidLine))
            painter.drawLine(
                rect.x() + margin, rect.y() + margin,
                rect.x() + rect.width() - margin, rect.y() + rect.height() - margin
            )
            painter.drawLine(
                rect.x() + rect.width() - margin, rect.y() + margin,
                rect.x() + margin, rect.y() + rect.height() - margin
            )


    def mouseReleaseEvent(self, event: wid.QGraphicsSceneMouseEvent) -> None:

        if event.button() == Qt.MouseButton.LeftButton:
            if self.__state == 1:
                self.__state = -1
            else:
                self.__state = 1
        elif event.button() == Qt.MouseButton.RightButton:
            if self.__state == 0:
                self.__state = -1
            else:
                self.__state = 0

        self.clicked.emit(self.__x, self.__y, self.__state)

        self.update()
        return super().mouseReleaseEvent(event)