from PySide2.QtCore import QObject, Slot, Signal

from Flora.Pots.Pot import Pot
from Flora.Pots.PotsGraphHandler import PotsGraphHandler

class PotsHandler(QObject):

    currentPotChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentPot = None
        self.graphHandler = PotsGraphHandler(self)

    def setCurrentPot(self, pot: Pot):
        self.currentPot = pot
        self.graphHandler.setSensorData(pot.sensorData)
        self.currentPotChanged.emit()

    def resetCurrentPot(self):
        self.currentPot = None
        self.graphHandler.resetGraph()
        self.currentPotChanged.emit()

    @Slot(result=bool)
    def currentPotValid(self) -> bool:
        return self.currentPot != None

    @Slot(result=bool)
    def currentPotPlantValid(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.plant is not None
        return False

    @Slot(result=str)
    def currentPotName(self) -> str:
        if (self.currentPotValid()):
            return self.currentPot.potName
        return ""
    
    @Slot(result=str)
    def currentPotPlantName(self) -> str:
        if (self.currentPotValid()):
            return self.currentPot.plantName()
        return ""
    
    @Slot(result=float)
    def currentPotPlantSoilMoisture(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.plantSoilMoisture()
        return 0.0
    
    @Slot(result=float)
    def currentPotPlantTemperature(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.plantTemperature()
        return 0.0
    
    @Slot(result=float)
    def currentPotPlantLightLevel(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.plantLightLevel()
        return 0.0
    
    @Slot(result=float)
    def currentPotPlantSalinity(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.plantSalinity()
        return 0.0
    
    @Slot(result=float)
    def currentPotPlantPh(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.plantPh()
        return 0.0
    
    @Slot(result=float)
    def currentPotLastSensorSoilMoisture(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.lastSensorSoilMoisture()
        return 0.0
    
    @Slot(result=float)
    def currentPotLastSensorTemperature(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.lastSensorTemperature()
        return 0.0
    
    @Slot(result=float)
    def currentPotLastSensorLightLevel(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.lastSensorLightLevel()
        return 0.0
    
    @Slot(result=float)
    def currentPotLastSensorSalinity(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.lastSensorSalinity()
        return 0.0
    
    @Slot(result=float)
    def currentPotLastSensorPh(self) -> float:
        if (self.currentPotValid()):
            return self.currentPot.lastSensorPh()
        return 0.0
    
    @Slot(result=bool)
    def currentPotTemperatureOk(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.temperatureOk()
        return True
    
    @Slot(result=bool)
    def currentPotSoilMoistureOk(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.soilMoistureOk()
        return True
    
    @Slot(result=bool)
    def currentPotLightLevelOk(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.lightLevelOk()
        return True
    
    @Slot(result=bool)
    def currentPotSalinityOk(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.salinityOk()
        return True
    
    @Slot(result=bool)
    def currentPotPhOk(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.phOk()
        return True
    
    @Slot(result=str)
    def currentPotPlantImagePath(self) -> str:
        if (self.currentPotValid()):
            return self.currentPot.plantImagePath()
        return ""
    
    @Slot(result=bool)
    def currentPotIsBroken(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.isBroken
        return False
    
    @Slot(result = bool)
    def sensorDataExists(self) -> bool:
        if (self.currentPotValid()):
            return self.currentPot.sensorDataExists()
        return False
    