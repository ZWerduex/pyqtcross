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

    HINT_CELL_BACKGROUND = (224, 196, 141)
    GRID_CELL_GREY_BACKGROUND = WHITE
    GRID_CELL_WHITE_BACKGROUND = (221, 221, 221)
    CELL_DRAW_COLOR = (23, 27, 37)

class Styles():

    BACKGROUND = f'background-color: rgb{Colors.BLACK};'

    TITLE = f'color: rgb{Colors.WHITE};'
    SUBTITLE = f'color: rgb{Colors.GREY};'
    TEXT = f'color: rgb{Colors.WHITE};'

    DARK_THEME = f'{BACKGROUND} {TEXT}'

class Fonts():

    TITLE = gui.QFont('Arial', 24)
    TITLE.setBold(True)

    SUBTITLE = gui.QFont('Arial', 14)
    SUBTITLE.setBold(False)

    TEXT = gui.QFont('Arial', 12)
    TEXT.setBold(False)


