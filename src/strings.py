import os

import PyQt6.QtGui as gui


__all__ = ['Path', 'Strings', 'Colors', 'Styles', 'Fonts']


class Strings():

    APPLICATION_NAME = 'PyQtCross'


class Path():

    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA = os.path.join(ROOT, 'data')

    LOG = os.path.join(ROOT, f'{Strings.APPLICATION_NAME.lower()}.log')
    MODELS = os.path.join(DATA, 'models.json')

class Colors():

    BLACK = (34, 34, 34)

    WHITE = (255, 255, 255)
    GREY = (170, 170, 170)

    HINT_CELL_BACKGROUND = (148, 51, 121)
    GRID_CELL_WHITE_BACKGROUND = WHITE
    GRID_CELL_GREY_BACKGROUND = (221, 221, 221)
    CELL_DRAW_COLOR = (23, 27, 37)

class Styles():

    BACKGROUND = f'background-color: rgb{Colors.BLACK};'

    TITLE = f'color: rgb{Colors.WHITE};'
    SUBTITLE = f'color: rgb{Colors.GREY};'
    TEXT = f'color: rgb{Colors.WHITE};'

    DARK_THEME = f'{BACKGROUND} {TEXT}'

class Fonts():

    @staticmethod
    def bold(size: int) -> gui.QFont:
        font = gui.QFont('Arial', size)
        font.setBold(True)
        return font
    
    @staticmethod
    def normal(size: int) -> gui.QFont:
        font = gui.QFont('Arial', size)
        font.setBold(False)
        return font

    TITLE = bold(24)

    SUBTITLE = normal(16)

    TEXT = normal(12)


