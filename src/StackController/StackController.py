from enum import IntEnum

from PySide2.QtCore import QObject, Property, Signal, Slot

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return
        return self.items.pop()

    def clear(self):
        self.items = []

    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
    


class StackController(QObject):
    @Signal
    def screenChanged(self):
         pass

    class Screen(IntEnum):
        Welcome, Registration, Login, ForgottenPassword = range(4)

    @Property(int, notify=screenChanged)
    def currentScreen(self):
        if (self.stack.peek()):
            return self.stack.peek().value
        return 0

    def __init__(self, parent=None):
        super().__init__(parent)

        self.stack = Stack()
        self.stack.push(StackController.Screen.Welcome)

    @Slot()
    def openRegistrationScreen(self):
        self.stack.push(StackController.Screen.Registration)
        self.screenChanged.emit()

    @Slot()
    def openLoginScreen(self):
        self.stack.push(StackController.Screen.Login)
        self.screenChanged.emit()

    @Slot()
    def openForgottenPasswordScreen(self):
        self.stack.push(StackController.Screen.ForgottenPassword)
        self.screenChanged.emit()

    @Slot()
    def goBack(self):
        self.stack.pop()
        self.screenChanged.emit()
