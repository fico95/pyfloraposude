from PySide2.QtCore import QObject, QEnum

from enum import IntEnum

class Enums(QObject):

    @QEnum
    class Screen(IntEnum):
        Welcome, \
        Registration, \
        Login, \
        ForgottenPassword, \
        Pots, \
        Plants, \
        PotEditor, \
        PlantEditor, \
        UserEditor, \
        PlantLoader, \
        PotLoader, \
        PlantSelect = range(12)

    @QEnum
    class GraphType(IntEnum):
        Line, \
        Bar, \
        Scatter = range(3)

    def __init__(self, parent=None):
        super().__init__(parent)