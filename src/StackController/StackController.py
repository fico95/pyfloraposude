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
        Welcome, Registration, Login, ForgottenPassword, Pots, Plants, PotEditor, PlantEditor, UserEditor = range(9)

    @Property(int, notify=screenChanged)
    def currentScreen(self):
        if (self.stack.peek()):
            return self.stack.peek().value
        return 0

    @Property(bool, notify=screenChanged)
    def userEditable(self):
        screen = self.currentScreen
        return screen == StackController.Screen.Pots \
               or screen == StackController.Screen.Plants \
               or screen == StackController.Screen.PotEditor \
               or screen == StackController.Screen.PlantEditor

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
    def openPotsScreen(self):
        self.stack.push(StackController.Screen.Pots)
        self.screenChanged.emit()

    @Slot()
    def openPlantsScreen(self):
        self.stack.push(StackController.Screen.Plants)
        self.screenChanged.emit()

    @Slot()
    def openPotEditorScreen(self):
        self.stack.push(StackController.Screen.PotEditor)
        self.screenChanged.emit()

    @Slot()
    def openPlantEditorScreen(self):
        self.stack.push(StackController.Screen.PlantEditor)
        self.screenChanged.emit()

    @Slot()
    def openUserEditorScreen(self):
        self.stack.push(StackController.Screen.UserEditor)
        self.screenChanged.emit()

    @Slot()
    def handleUserChange(self):
        self.goToWelcomeScreen()

    @Slot()
    def handlePlantRemove(self):
        if (self.stack.peek() == StackController.Screen.PlantEditor):
            self.goBack()

    @Slot()
    def goToWelcomeScreen(self):
        self.stack.clear()
        self.stack.push(StackController.Screen.Welcome)
        self.screenChanged.emit()

    @Slot()
    def goBack(self):
        self.stack.pop()
        self.screenChanged.emit()
