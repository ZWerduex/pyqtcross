
import PyQt6.QtCore as core
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid


__all__ = ['HintCell']


class HintCell(wid.QGraphicsItem):

    def __init__(self, size: int, hint: str) -> None:
        wid.QGraphicsItem.__init__(self)
        self.__size = size
        self.__hint = hint
        self.__crossed = False

    def boundingRect(self) -> core.QRectF:
        return core.QRectF(0, 0, self.__size, self.__size)
    
    def paint(self,
                painter: gui.QPainter,
                option: wid.QStyleOptionGraphicsItem,
                widget: wid.QWidget
        ) -> None:
            rect = self.boundingRect()
            painter.setRenderHint(gui.QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(gui.QPainter.RenderHint.TextAntialiasing)
    
            # Cell background
            painter.setBrush(gui.QBrush(gui.QColor('87CEEB'), Qt.BrushStyle.SolidPattern))
            painter.drawRect(rect)
    
            # Hint
            painter.setPen(gui.QPen(gui.QColor(23, 27, 37), 1.5, Qt.PenStyle.SolidLine))
            painter.setFont(gui.QFont('Arial', 10))
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, self.__hint)

            
            margin = int(rect.width() * 0.05)
    
            # Cross
            if self.__crossed:
                painter.drawLine(
                    rect.x() + margin, rect.y() + margin,
                    rect.x() + rect.width() - margin, rect.y() + rect.height() - margin
                )
                painter.drawLine(
                    rect.x() + rect.width() - margin, rect.y() + margin,
                    rect.x() + margin, rect.y() + rect.height() - margin
                )

    def mouseReleaseEvent(self, event: wid.QGraphicsSceneMouseEvent) -> None:
        self.__crossed = not self.__crossed
        self.update()

        return super().mouseReleaseEvent(event)