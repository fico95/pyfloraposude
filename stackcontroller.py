from enum import IntEnum

from PySide2.QtCore import QEnum, QObject, Property, Signal, Slot

class StackController(QObject):
    @Signal
    def screen_changed(self):
         pass

    @QEnum
    class Screen(IntEnum):
        Welcome, Registration, Login, ForgottenPassword = range(4)

    @Property(int, notify=screen_changed)
    def current_screen(self):
        return self._current_screen

    def __init__(self, parent=None):
        super().__init__(parent)
        self.open_welcome_screen()

    @Slot()
    def open_welcome_screen(self):
        self._current_screen = StackController.Screen.Welcome
        self.screen_changed.emit()

    @Slot()
    def open_registration_screen(self):
        self._current_screen = StackController.Screen.Registration
        self.screen_changed.emit()

    @Slot()
    def open_login_screen(self):
        self._current_screen = StackController.Screen.Login
        self.screen_changed.emit()

    @Slot()
    def open_forgotten_password_screen(self):
        self._current_screen = StackController.Screen.ForgottenPassword
        self.screen_changed.emit()
