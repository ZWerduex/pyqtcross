
import PyQt6.QtWidgets as wid

import strings as s


__all__ = ['TitleLabel', 'SubtitleLabel']


class TitleLabel(wid.QLabel):

    def __init__(self, text: str) -> None:
        wid.QLabel.__init__(self, text)
        self.setFont(s.Fonts.TITLE)
        self.setStyleSheet(s.Styles.TITLE)

class SubtitleLabel(wid.QLabel):
    
    def __init__(self, text: str) -> None:
        wid.QLabel.__init__(self, text)
        self.setFont(s.Fonts.SUBTITLE)
        self.setStyleSheet(s.Styles.SUBTITLE)
        