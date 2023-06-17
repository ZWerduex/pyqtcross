
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import picross as p
from .Labels import TitleLabel, SubtitleLabel


__all__ = ['PicrossTitleWidget']


class PicrossTitleWidget(wid.QWidget):

    def __init__(self, picross: p.Picross) -> None:
        wid.QWidget.__init__(self)
        
        self.__title = TitleLabel(picross.name)
        self.__subtitle = SubtitleLabel(f'{picross.width}x{picross.height}')

        layout = wid.QVBoxLayout()

        layout.addWidget(self.__title)
        layout.addWidget(self.__subtitle)
        layout.addStretch()

        self.setLayout(layout)

    def update(self, picross: p.Picross) -> None:
        self.__title.setText(picross.name)
        self.__subtitle.setText(f'{picross.width}x{picross.height}')        