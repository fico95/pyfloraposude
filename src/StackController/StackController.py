from PySide2.QtCore import QObject, Property, Signal, Slot

from Utils.Enums import Enums

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def clear(self):
        self.items = []

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
    


class StackController(QObject):
    @Signal
    def screenChanged(self):
        pass

    @Property(int, notify=screenChanged)
    def currentScreen(self):
        if (self.stack.peek()):
            return self.stack.peek().value
        return 0

    @Property(bool, notify=screenChanged)
    def userEditable(self):
        screen = self.currentScreen
        return screen == Enums.Screen.Pots \
               or screen == Enums.Screen.Plants \
               or screen == Enums.Screen.PotEditor \
               or screen == Enums.Screen.PlantEditor \
               or screen == Enums.Screen.PlantLoader \
               or screen == Enums.Screen.PotLoader

    def __init__(self, parent=None):
        super().__init__(parent)

        self.stack = Stack()
        self.stack.push(Enums.Screen.Plants)

    @Slot()
    def openRegistrationScreen(self):
        self.stack.push(Enums.Screen.Registration)
        self.screenChanged.emit()

    @Slot()
    def openLoginScreen(self):
        self.stack.push(Enums.Screen.Login)
        self.screenChanged.emit()

    @Slot()
    def openForgottenPasswordScreen(self):
        self.stack.push(Enums.Screen.ForgottenPassword)
        self.screenChanged.emit()

    @Slot()
    def openPotsScreen(self):
        self.stack.push(Enums.Screen.Pots)
        self.screenChanged.emit()

    @Slot()
    def openPlantsScreen(self):
        self.stack.push(Enums.Screen.Plants)
        self.screenChanged.emit()

    @Slot()
    def openPotEditorScreen(self):
        self.stack.push(Enums.Screen.PotEditor)
        self.screenChanged.emit()

    @Slot()
    def openPlantEditorScreen(self):
        self.stack.push(Enums.Screen.PlantEditor)
        self.screenChanged.emit()

    @Slot()
    def openUserEditorScreen(self):
        self.stack.push(Enums.Screen.UserEditor)
        self.screenChanged.emit()

    @Slot()
    def openUserPasswordChangeScreen(self):
        self.stack.push(Enums.Screen.UserPasswordChange)
        self.screenChanged.emit()

    @Slot()
    def openUserDeleteScreen(self):
        self.stack.push(Enums.Screen.UserDelete)
        self.screenChanged.emit()

    @Slot()
    def openPlantLoaderScreen(self):
        self.stack.push(Enums.Screen.PlantLoader)
        self.screenChanged.emit()

    @Slot()
    def openPotLoaderScreen(self):
        self.stack.push(Enums.Screen.PotLoader)
        self.screenChanged.emit()

    @Slot()
    def openPlantSelectScreen(self):
        self.stack.push(Enums.Screen.PlantSelect)
        self.screenChanged.emit()

    @Slot()
    def handlePlantRemove(self):
        if (self.stack.peek() == Enums.Screen.PlantEditor):
            self.goBack()

    @Slot()
    def handlePotRemove(self):
        if (self.stack.peek() == Enums.Screen.PotEditor):
            self.goBack()

    @Slot()
    def goToWelcomeScreen(self):
        self.stack.clear()
        self.stack.push(Enums.Screen.Welcome)
        self.screenChanged.emit()

    @Slot()
    def goBack(self):
        self.stack.pop()
        self.screenChanged.emit()
