
import PyQt6.QtWidgets as wid

import gui.widgets as w
import picross as p

__all__ = ['MainWindow']


class MainWindow(wid.QMainWindow):

    def __init__(self, windowTitle: str) -> None:
        wid.QMainWindow.__init__(self)
        self.setWindowTitle(windowTitle)
        
        # Layout
        self.__layout = wid.QHBoxLayout()

        # Widgets
        picross = p.Picross(p.PicrossModel.fromGrid('test', [
            [1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 1],
        ]))

        self.__picrossWidget = w.PicrossWidget(25, picross)
        self.__layout.addWidget(self.__picrossWidget)

        central = wid.QWidget()
        central.setLayout(self.__layout)
        self.setCentralWidget(central)