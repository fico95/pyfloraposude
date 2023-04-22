from enum import IntEnum

from PySide2.QtCore import QObject, Property, Signal, Slot

class StackController(QObject):
    @Signal
    def screenChanged(self):
         pass

    class Screen(IntEnum):
        Welcome, Registration, Login, ForgottenPassword = range(4)

    @Property(int, notify=screenChanged)
    def currentScreen(self):
        return self._current_screen

    def __init__(self, parent=None):
        super().__init__(parent)
        self.openWelcomeScreen()

    @Slot()
    def openWelcomeScreen(self):
        self._current_screen = StackController.Screen.Welcome
        self.screenChanged.emit()

    @Slot()
    def openRegistrationScreen(self):
        self._current_screen = StackController.Screen.Registration
        self.screenChanged.emit()

    @Slot()
    def openLoginScreen(self):
        self._current_screen = StackController.Screen.Login
        self.screenChanged.emit()

    @Slot()
    def openForgottenPasswordScreen(self):
        self._current_screen = StackController.Screen.ForgottenPassword
        self.screenChanged.emit()

