from PySide2.QtCore import QObject, Slot, Signal, Property

from Flora.Plants.Plant import Plant

class PlantsHandler(QObject):

    currentPlantChanged = Signal()

    @Property(Plant, notify=currentPlantChanged)
    def currentPlant(self):
        return self.selectedPlant

    def __init__(self, parent=None):
        super().__init__(parent)

        self.selectedPlant = None

    @Slot(result=QObject)
    def getCurrentPlant(self):
        return self.selectedPlant

    def setCurrentPlant(self, plant: Plant):
        self.selectedPlant = plant
        self.currentPlantChanged.emit()
    
    def resetCurrentPlant(self):
        self.selectedPlant = None
        self.currentPlantChanged.emit()

    @Slot(result=int)
    def getCurrentPlantId(self):
        if (self.selectedPlant):
            return self.selectedPlant.id
        return -1

    @Slot(result=str)
    def getCurrentPlantName(self):
        if (self.selectedPlant):
            return self.selectedPlant.name
        return ""
    
    @Slot(result=str)
    def getCurrentPlantImagePath(self):
        if (self.selectedPlant):
            return self.selectedPlant.imagePath
        return ""
    
    @Slot(result=float)
    def getCurrentPlantDesiredSoilMoisture(self):
        if (self.selectedPlant):
            return self.selectedPlant.plantCare.soilMoisture
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredPh(self):
        if (self.selectedPlant):
            return self.selectedPlant.plantCare.ph
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredSalinity(self):
        if (self.selectedPlant):
            return self.selectedPlant.plantCare.salinity
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredLightLevel(self):
        if (self.selectedPlant):
            return self.selectedPlant.plantCare.lightLevel
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredTemperature(self):
        if (self.selectedPlant):
            return self.selectedPlant.plantCare.temperature
        return 0.0