
import PyQt6.QtWidgets as wid

import gui.widgets as w
import picross as p
import strings as s

__all__ = ['MainWindow']


class MainWindow(wid.QMainWindow):

    def __init__(self, windowTitle: str) -> None:
        wid.QMainWindow.__init__(self)
        self.setWindowTitle(windowTitle)
        
        # Layout
        self.__layout = wid.QVBoxLayout()

        # Widgets
        # picross = p.Picross(p.PicrossModel.fromDictData('A nice break', [
        #     # 11x15 picross
        #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        #     [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        #     [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        #     [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        #     [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        #     [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        #     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        #     [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        #     [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        #     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0]
        # ]))

        # picross = p.Picross(p.PicrossModel.fromDictData('Test', [
        #     # 5x5 picross
        #     [1, 1, 0, 0, 0],
        #     [0, 1, 0, 0, 0],
        #     [1, 0, 0, 1, 1],
        #     [0, 1, 0, 1, 0],
        #     [0, 1, 0, 1, 0]
        # ]))

        manager = p.PicrossModelManager(s.Path.MODELS)
        picross = p.Picross(manager.load('A nice break'))

        self.__label = wid.QLabel(f'{picross.name} ({picross.width}x{picross.height})')
        self.__layout.addWidget(self.__label)

        self.__pWid = w.PicrossWidget(25, picross)
        self.__pWid.completed.connect(self.onPicrossCompleted)
        self.__layout.addWidget(self.__pWid)

        central = wid.QWidget()
        central.setLayout(self.__layout)
        self.setCentralWidget(central)

    def onPicrossCompleted(self) -> None:
        self.__label.setText(self.__label.text() + ' : Completed !')
        self.__pWid.setEnabled(False)