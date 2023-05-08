from PySide2.QtCore import QObject, Slot, Signal, Property

from Flora.Pots.Pot import Pot
from Flora.Pots.PotsGraphHandler import PotsGraphHandler

class PotsHandler(QObject):

    currentPotChanged = Signal()

    @Property(Pot, notify=currentPotChanged)
    def currentPot(self):
        return self.selectedPot
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.selectedPot = None
        self.graphHandler = PotsGraphHandler(self)

    def setCurrentPot(self, pot: Pot):
        self.selectedPot = pot
        self.graphHandler.setSensorData(pot.sensorData)
        self.graphHandler.setLineGraph()
        self.currentPotChanged.emit()

    def resetCurrentPot(self):
        self.selectedPot = None
        self.graphHandler.resetGraph()
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
        if (self.selectedPot):
            return self.selectedPot.getPlantName()
        return ""
    
    @Slot(result=float)
    def getCurrentPotPlantSoilMoisture(self):
        if (self.selectedPot):
            return self.selectedPot.getPlantSoilMoisture()
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantTemperature(self):
        if (self.selectedPot):
            return self.selectedPot.getPlantTemperature()
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantLightLevel(self):
        if (self.selectedPot):
            return self.selectedPot.getPlantLightLevel()
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantSalinity(self):
        if (self.selectedPot):
            return self.selectedPot.getPlantSalinity()
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantPh(self):
        if (self.selectedPot):
            return self.selectedPot.getPlantPh()
        return 0.0
    
    @Slot(result=float)
    def getLastSensorSoilMoisture(self):
        if (self.selectedPot):
            return self.selectedPot.getLastMeasuredSoilMoisture()
        return 0.0
    
    @Slot(result=float)
    def getLastSensorTemperature(self):
        if (self.selectedPot):
            return self.selectedPot.getLastMeasuredTemperature()
        return 0.0
    
    @Slot(result=float)
    def getLastSensorLightLevel(self):
        if (self.selectedPot):
            return self.selectedPot.getLastMeasuredLightLevel()
        return 0.0
    
    @Slot(result=float)
    def getLastSensorSalinity(self):
        if (self.selectedPot):
            return self.selectedPot.getLastMeasuredSalinity()
        return 0.0
    
    @Slot(result=float)
    def getLastSensorPh(self):
        if (self.selectedPot):
            return self.selectedPot.getLastMeasuredPh()
        return 0.0
    
    @Slot(result=bool)
    def getCurrentPotPlantTemperatureOk(self):
        if (self.selectedPot):
            return self.selectedPot.getTemperatureOk()
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantSoilMoistureOk(self):
        if (self.selectedPot):
            return self.selectedPot.getSoilMoistureOk()
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantLightLevelOk(self):
        if (self.selectedPot):
            return self.selectedPot.getLightLevelOk()
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantSalinityOk(self):
        if (self.selectedPot):
            return self.selectedPot.getSalinityOk()
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantPhOk(self):
        if (self.selectedPot):
            return self.selectedPot.getPhOk()
        return True
    
    @Slot(result=str)
    def getCurrentPotPlantImagePath(self):
        if (self.selectedPot):
            return self.selectedPot.getPlantImagePath()
        return ""
    
    @Slot(result=bool)
    def getCurrentPotIsBroken(self):
        if (self.selectedPot):
            return self.selectedPot.isBroken
        return False
    
    @Slot(result = bool)
    def sensorDataExists(self) -> bool:
        if (self.selectedPot):
            return self.selectedPot.sensorDataExists()
        return False
    