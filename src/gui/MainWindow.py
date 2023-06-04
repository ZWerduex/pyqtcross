
import PyQt6.QtWidgets as wid

import gui.widgets as w
import picross as p

__all__ = ['MainWindow']


class MainWindow(wid.QMainWindow):

    def __init__(self, windowTitle: str) -> None:
        wid.QMainWindow.__init__(self)
        self.setWindowTitle(windowTitle)
        
        # Layout
        self.__layout = wid.QGridLayout()
        self.__layout.setSpacing(0)

        # Widgets
        picross = p.Picross(p.PicrossModel.fromGrid('test', [
            [1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 1]
        ]))

        group = False
        for i in range(picross.width):
            if i % 5 == 0:
                group = not group
            for j in range(picross.height):
                if j % 5 == 0:
                    group = not group
                cell = w.Cell(group)
                cell.setFixedSize(50, 50)
                self.__layout.addWidget(cell, i, j)

        central = wid.QWidget()
        central.setLayout(self.__layout)
        self.setCentralWidget(central)