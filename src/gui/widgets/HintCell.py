
import PyQt6.QtGui as gui

import strings as s
from .Cell import Cell


__all__ = ['HintCell']


class HintCell(Cell):

    def __init__(self, size: int, hint: str) -> None:
        Cell.__init__(self, size)

        self.__crossed = False
        self.__isEmpty = hint == ''

        if not self.__isEmpty:
            self.__text = self.drawText(hint, *s.Colors.CELL_DRAW_COLOR)

        self.setBackgroundRGB(*s.Colors.HINT_CELL_BACKGROUND)

    def mouseReleaseEvent(self, event: gui.QMouseEvent) -> None:
        if self.__isEmpty:
            return
        
        self.clear([self.__text])
        if not self.__crossed:
            self.drawCross(*s.Colors.CELL_DRAW_COLOR, alpha = 140)
        self.__crossed = not self.__crossed