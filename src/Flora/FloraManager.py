from PySide2.QtCore import QObject, Slot

from Flora.Plants.PlantData import PlantData
from Flora.Plants.Plant import Plant
from Flora.Plants.PlantDb import PlantDb
from Flora.Plants.PlantsHandler import PlantsHandler
from Flora.Plants.PlantModel import PlantModel

class FloraManager(QObject):

    def __init__(self, dbPath, imagesPath, parent=None):
        super().__init__(parent)

        self.plantDb = PlantDb(dbPath)
        if (self.plantDb.getNumPlants() == 0):
            self.plantDb.fillTable(imagesPath)

        self.plantModel = PlantModel(self.plantDb, self)
        self.plantsHandler = PlantsHandler(self)

    @Slot(str, str, float, float, float, float, float, result = bool)
    def addPlant(self, name, imagePath, soilMoisture, ph, salinity, lightLevel, temperature):
        try:
            plant = Plant(None, name, imagePath, PlantData(soilMoisture, ph, salinity, lightLevel, temperature))
            self.plantDb.addPlant(plant)

            self.plantModel.updateModel()
            self.plantsHandler.resetCurrentPlant()

            return True
        except Exception as e:
            print(f"Error adding plant: {e}")
            return False
        
    @Slot(result = bool)
    def removeCurrentPlant(self):
        if (self.plantsHandler.selectedPlant):
            try:
                self.plantDb.removePlantById(self.plantsHandler.selectedPlant.id)

                self.plantModel.updateModel()
                self.plantsHandler.resetCurrentPlant()
                
                return True
            except Exception as e:
                print(f"Error removing plant: {e}")
                return False
        return False
        
    @Slot(int, result=bool)
    def setCurrentPlant(self, id):
        try:
            plant = self.plantDb.getPlantById(id)
            self.plantsHandler.setCurrentPlant(plant)
            return True
        except Exception as e:
            self.plantsHandler.setCurrentPlant(None)
            print(f"Error setting current plant: {e}")
            return False
        
    @Slot(str, float, float, float, float, float, result = bool)
    def updateCurrentPlant(self, name, soilMoisture, ph, salinity, lightLevel, temperature):
        if (self.plantsHandler.selectedPlant):
            self.plantsHandler.selectedPlant.name = name
            self.plantsHandler.selectedPlant.plantCare.soilMoisture = soilMoisture
            self.plantsHandler.selectedPlant.plantCare.ph = ph
            self.plantsHandler.selectedPlant.plantCare.salinity = salinity
            self.plantsHandler.selectedPlant.plantCare.lightLevel = lightLevel
            self.plantsHandler.selectedPlant.plantCare.temperature = temperature
            try:
                self.plantDb.updatePlant(self.plantsHandler.selectedPlant)

                self.plantModel.updateModel()
                self.setCurrentPlant(self.plantsHandler.selectedPlant.id)

                return False
            except Exception as e:
                print(f"Error updating plant: {e}")
                self.setCurrentPlant(self.plantsHandler.selectedPlant.id)
                return False
        return False
    
    @Slot(str, result = bool)
    def updateCurrentPlantImage(self, imagePath):
        if (self.plantsHandler.selectedPlant):
            self.plantsHandler.selectedPlant.imagePath = imagePath
            try:
                self.plantDb.updatePlant(self.plantsHandler.selectedPlant)

                self.plantModel.updateModel()
                self.setCurrentPlant(self.plantsHandler.selectedPlant.id)

                return True
            except Exception as e:
                print(f"Error updating plant image: {e}")
                self.setCurrentPlant(self.plantsHandler.selectedPlant.id)
                return False
        return False
    
    @Slot()
    def resetCurrentPlant(self):
        self.plantsHandler.resetCurrentPlant()
