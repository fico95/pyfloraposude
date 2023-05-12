from PySide2.QtCore import QObject, QEnum

from enum import IntEnum

class Enums(QObject):

    @QEnum
    class Screen(IntEnum):
        Welcome, \
        Registration, \
        Login, \
        ForgottenPassword, \
        UserEditor, \
        UserPasswordChange, \
        UserDelete, \
        Pots, \
        PotEditor, \
        PotLoader, \
        Plants, \
        PlantEditor, \
        PlantLoader, \
        PlantSelect = range(14)

    @QEnum
    class GraphType(IntEnum):
        Line, \
        Bar, \
        Scatter = range(3)

    def __init__(self, parent=None):
        super().__init__(parent)