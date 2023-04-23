from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex, Slot, Signal, Property

from Flora.Plants.Plant import Plant
from Flora.Plants.PlantDb import PlantDb

class PlantsHandler(QAbstractListModel):
    Name = Qt.UserRole + 1
    Id = Qt.UserRole + 2
    ImagePath = Qt.UserRole + 3

    currentPlantChanged = Signal()

    @Property(Plant, notify=currentPlantChanged)
    def currentPlant(self):
        return self._currentPlant

    def __init__(self, dbPath, imagesPath, parent=None):
        super().__init__(parent)
        self.plantDb = PlantDb(dbPath)
        if (self.plantDb.getNumPlants() == 0):
            self.plantDb.fillTable(imagesPath)
        self.plants = self.plantDb.getAllPlants()
        self._currentPlant=None

    @Slot(int, result=bool)
    def setCurrentPlant(self, id):
        self._currentPlant = self.plantDb.getPlantById(id)
        self.currentPlantChanged.emit()
        return self._currentPlant != None
    
    @Slot()
    def resetCurrentPlant(self):
        self._currentPlant = None
        self.currentPlantChanged.emit()

    @Slot(result=str)
    def getCurrentPlantName(self):
        if (self._currentPlant):
            return self._currentPlant.name
        return ""
    
    @Slot(result=str)
    def getCurrentPlantImagePath(self):
        if (self._currentPlant):
            return self._currentPlant.imagePath
        return ""
    
    @Slot(result=float)
    def getCurrentPlantDesiredSoilMoisture(self):
        if (self._currentPlant):
            return self._currentPlant.plantCare.soilMoisture
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredPh(self):
        if (self._currentPlant):
            return self._currentPlant.plantCare.ph
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredSalinity(self):
        if (self._currentPlant):
            return self._currentPlant.plantCare.salinity
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredLightLevel(self):
        if (self._currentPlant):
            return self._currentPlant.plantCare.lightLevel
        return 0.0
    
    @Slot(result=float)
    def getCurrentPlantDesiredTemperature(self):
        if (self._currentPlant):
            return self._currentPlant.plantCare.temperature
        return 0.0
    
    @Slot(str, float, float, float, float, float, result = bool)
    def updateCurrentPlant(self, name, soilMoisture, ph, salinity, lightLevel, temperature):
        if (self._currentPlant):
            self._currentPlant.name = name
            self._currentPlant.plantCare.soilMoisture = soilMoisture
            self._currentPlant.plantCare.ph = ph
            self._currentPlant.plantCare.salinity = salinity
            self._currentPlant.plantCare.lightLevel = lightLevel
            self._currentPlant.plantCare.temperature = temperature
            try:
                self.plantDb.updatePlant(self._currentPlant)
                return False
            except Exception as e:
                print(f"Error updating plant: {e}")
                self.setCurrentPlant(self._currentPlant.id)
                return False
        return False
    
    @Slot(result = bool)
    def removeCurrentPlant(self):
        if (self._currentPlant):
            try:
                self.plantDb.removePlant(self._currentPlant.id)
                self.updateModel()
                return True
            except Exception as e:
                print(f"Error removing plant: {e}")
                return False
        return False
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.plants)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.plants):
            return None

        plant = self.plants[index.row()]

        if role == PlantsHandler.Name:
            return plant.name
        elif role == PlantsHandler.Id:
            return plant.id
        elif role == PlantsHandler.ImagePath:
            return plant.imagePath
        
        return None

    def roleNames(self):
        return {
            PlantsHandler.Name: b'name',
            PlantsHandler.Id: b'id',
            PlantsHandler.ImagePath: b'imagePath'
        }
    
    def updateModel(self):
        self.beginResetModel()
        self.plants = self.plantDb.getAllPlants()
        self.endResetModel()
        self.resetCurrentPlant()
