import os


__all__ = ['Path', 'Strings']


class Strings():

    APPLICATION_NAME = 'Pygramme'


class Path():

    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    LOG = os.path.join(ROOT, f'{Strings.APPLICATION_NAME.lower()}.log')