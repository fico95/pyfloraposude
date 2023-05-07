from PySide2.QtCore import QObject, Slot, Signal, Property

from Flora.Pots.Pot import Pot

class PotsHandler(QObject):

    currentPotChanged = Signal()

    @Property(Pot, notify=currentPotChanged)
    def currentPot(self):
        return self.selectedPot
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.selectedPot = None

    def setCurrentPot(self, pot: Pot):
        self.selectedPot = pot
        self.currentPotChanged.emit()

    def resetCurrentPot(self):
        self.selectedPot = None
        self.currentPotChanged.emit()

    @Slot(result=bool)
    def isCurrentPotSet(self):
        return self.selectedPot != None

    @Slot(result=bool)
    def getCurrentPotPlantExists(self):
        if (self.selectedPot):
            return self.selectedPot.plant is not None
        return False

    @Slot(result=str)
    def getCurrentPotName(self):
        if (self.selectedPot):
            return self.selectedPot.potName
        return ""
    
    @Slot(result=str)
    def getCurrentPotPlantName(self):
        if (self.selectedPot and self.selectedPot.plant):
            return self.selectedPot.plant.name
        return ""
    
    @Slot(result=str)
    def getCurrentPotPlantImagePath(self):
        if (self.selectedPot and self.selectedPot.plant):
            return self.selectedPot.plant.imagePath
        return ""
    
    @Slot(result=bool)
    def getCurrentPotIsBroken(self):
        if (self.selectedPot):
            return self.selectedPot.isBroken
        return False
    