
import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import picross as p
import strings as s


__all__ = ['PicrossListItem']


class PicrossListItem(wid.QWidget):

    def __init__(self, picross: p.Picross) -> None:
        wid.QWidget.__init__(self)
        self.setCursor(gui.QCursor(core.Qt.CursorShape.PointingHandCursor))
        
        title = wid.QLabel(picross.name)
        title.setFont(s.Fonts.bold(16))
        title.setStyleSheet(s.Styles.TITLE)

        subtitle = wid.QLabel(f'{picross.width}x{picross.height} - {picross.width * picross.height} cells')
        subtitle.setFont(s.Fonts.normal(12))
        subtitle.setStyleSheet(s.Styles.SUBTITLE)

        layout = wid.QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.setLayout(layout)
