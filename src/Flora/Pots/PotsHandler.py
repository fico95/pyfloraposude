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
        if (self.getCurrentPotPlantExists()):
            return self.selectedPot.plant.name
        return ""
    
    @Slot(result=float)
    def getCurrentPotPlantSoilMoisture(self):
        if (self.getCurrentPotPlantExists()):
            return self.selectedPot.plant.plantCare.soilMoisture
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantTemperature(self):
        if (self.getCurrentPotPlantExists()):
            return self.selectedPot.plant.plantCare.temperature
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantLightLevel(self):
        if (self.getCurrentPotPlantExists()):
            return self.selectedPot.plant.plantCare.lightLevel
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantSalinity(self):
        if (self.getCurrentPotPlantExists()):
            return self.selectedPot.plant.plantCare.salinity
        return 0.0
    
    @Slot(result=float)
    def getCurrentPotPlantPh(self):
        if (self.getCurrentPotPlantExists()):
            return self.selectedPot.plant.plantCare.ph
        return 0.0
    
    @Slot(result=float)
    def getLastSensorSoilMoisture(self):
        if (self.sensorDataExists()):
            return self.selectedPot.sensorData[-1].soilMoisture
        return 0.0
    
    @Slot(result=float)
    def getLastSensorTemperature(self):
        if (self.sensorDataExists()):
            return self.selectedPot.sensorData[-1].temperature
        return 0.0
    
    @Slot(result=float)
    def getLastSensorLightLevel(self):
        if (self.sensorDataExists()):
            return self.selectedPot.sensorData[-1].lightLevel
        return 0.0
    
    @Slot(result=float)
    def getLastSensorSalinity(self):
        if (self.sensorDataExists()):
            return self.selectedPot.sensorData[-1].salinity
        return 0.0
    
    @Slot(result=float)
    def getLastSensorPh(self):
        if (self.sensorDataExists()):
            return self.selectedPot.sensorData[-1].ph
        return 0.0
    
    @Slot(result=bool)
    def getCurrentPotPlantTemperatureOk(self):
        if (self.sensorDataExists()):
            return self.selectedPot.plant.plantCare.temperatureOk(self.getLastSensorTemperature())
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantSoilMoistureOk(self):
        if (self.sensorDataExists()):
            return self.selectedPot.plant.plantCare.soilMoistureOk(self.getLastSensorSoilMoisture())
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantLightLevelOk(self):
        if (self.sensorDataExists()):
            return self.selectedPot.plant.plantCare.lightLevelOk(self.getLastSensorLightLevel())
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantSalinityOk(self):
        if (self.sensorDataExists()):
            return self.selectedPot.plant.plantCare.salinityOk(self.getLastSensorSalinity())
        return True
    
    @Slot(result=bool)
    def getCurrentPotPlantPhOk(self):
        if (self.sensorDataExists()):
            return self.selectedPot.plant.plantCare.phOk(self.getLastSensorPh())
        return True
    
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
    
    @Slot(result = bool)
    def sensorDataExists(self) -> bool:
        return bool(self.selectedPot \
            and self.selectedPot.sensorData \
            and len(self.selectedPot.sensorData) > 0)
    