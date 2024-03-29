from PySide2.QtCore import QObject, Slot, Signal, Property

from Flora.Plants.Plant import Plant

class PlantsHandler(QObject):

    currentPlantChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentPlant = None

    def setCurrentPlant(self, plant: Plant):
        self.currentPlant = plant
        self.currentPlantChanged.emit()
    
    def resetCurrentPlant(self):
        self.currentPlant = None
        self.currentPlantChanged.emit()

    @Slot(result=bool)
    def currentPlantValid(self) -> bool:
        return self.currentPlant != None

    @Slot(result=int)
    def curentPlantId(self) -> int:
        if (self.currentPlantValid()):
            return self.currentPlant.id
        return -1

    @Slot(result=str)
    def currentPlantName(self) -> str:
        if (self.currentPlantValid()):
            return self.currentPlant.name
        return ""
    
    @Slot(result=str)
    def currentPlantImagePath(self) -> str:
        if (self.currentPlantValid()):
            return self.currentPlant.imagePath
        return ""
    
    @Slot(result=float)
    def currentPlantDesiredSoilMoisture(self) -> float:
        if (self.currentPlantValid()):
            return self.currentPlant.plantCare.soilMoisture
        return 0.0
    
    @Slot(result=float)
    def currentPlantDesiredPh(self) -> float:
        if (self.currentPlantValid()):
            return self.currentPlant.plantCare.ph
        return 0.0
    
    @Slot(result=float)
    def currentPlantDesiredSalinity(self) -> float:
        if (self.currentPlantValid()):
            return self.currentPlant.plantCare.salinity
        return 0.0
    
    @Slot(result=float)
    def currentPlantDesiredLightLevel(self) -> float:
        if (self.currentPlantValid()):
            return self.currentPlant.plantCare.lightLevel
        return 0.0
    
    @Slot(result=float)
    def currentPlantDesiredTemperature(self) -> float:
        if (self.currentPlantValid()):
            return self.currentPlant.plantCare.temperature
        return 0.0