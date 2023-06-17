
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import gui.widgets as w
import picross as p
import strings as s

__all__ = ['MainWindow']


class MainWindow(wid.QMainWindow):

    def __init__(self, windowTitle: str) -> None:
        wid.QMainWindow.__init__(self)
        self.setWindowTitle(windowTitle)

        # Dark theme
        self.setStyleSheet(s.Styles.DARK_THEME)

        # TODO : Remove this
        manager = p.PicrossModelManager(s.Path.MODELS)
        picross = p.Picross(manager.load('A nice break'))

        self.__pWid = w.PicrossWidget(25, picross)
        self.__pWid.completed.connect(self.onPicrossCompleted)

        layout = wid.QVBoxLayout()
        layout.addWidget(w.PicrossTitleWidget(picross))
        layout.addWidget(self.__pWid)

        central = wid.QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def onPicrossCompleted(self) -> None:
        print('Completed')
        self.__pWid.setEnabled(False)