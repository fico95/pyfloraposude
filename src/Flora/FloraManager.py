from PySide2.QtCore import QObject, Slot, Signal, Property

from Flora.Plants.PlantData import PlantData
from Flora.Plants.Plant import Plant
from Flora.Plants.PlantDb import PlantDb
from Flora.Plants.PlantsHandler import PlantsHandler
from Flora.Plants.PlantModel import PlantModel

from Flora.Pots.Pot import Pot
from Flora.Pots.PotDb import PotDb
from Flora.Pots.PotsHandler import PotsHandler
from Flora.Pots.PotModel import PotModel

from Flora.Pots.PotsDataSampler import PotsDataSampler

class FloraManager(QObject):

    allPotsShownChanged = Signal()

    @Property(bool, notify=allPotsShownChanged)
    def allPotsShown(self):
        return self.allPotsVisible

    def __init__(self, dbPath, imagesPath, parent=None):
        super().__init__(parent)

        self.allPotsVisible = True

        self.plantDb = PlantDb(dbPath)
        if (self.plantDb.getNumPlants() == 0):
            self.plantDb.fillTable(imagesPath)

        self.plantModel = PlantModel(self)
        self.plantsHandler = PlantsHandler(self)

        self.potDb = PotDb(dbPath)
        if (self.potDb.getNumPots() == 0):
            self.potDb.fillTable(self.plantDb.getRandomPlant())

        self.potModel = PotModel(self)
        self.potsHandler = PotsHandler(self)

        self.updatePlantsAndResetCurrentPlant()
        self.updatePotsAndResetCurrentPot()

    @Slot(str, str, float, float, float, float, float, result = bool)
    def addPlant(self, name, imagePath, soilMoisture, ph, salinity, lightLevel, temperature):
        try:
            plant = Plant(None, name, imagePath, PlantData(soilMoisture, ph, salinity, lightLevel, temperature))
            self.plantDb.addPlant(plant)

            self.updatePlantsAndResetCurrentPlant()

            return True
        except Exception as e:
            print(f"Error adding plant: {e}")
            return False
        
    @Slot(result = bool)
    def removeCurrentPlant(self):
        if (self.plantsHandler.selectedPlant):
            try:
                self.plantDb.removePlantById(self.plantsHandler.selectedPlant.id)

                self.updatePlantsAndResetCurrentPlant()
                self.updatePotsAndResetCurrentPot()
                
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
    def updateCurrentPlantData(self, name, soilMoisture, ph, salinity, lightLevel, temperature):
        if (self.plantsHandler.selectedPlant):
            self.plantsHandler.selectedPlant.name = name
            self.plantsHandler.selectedPlant.plantCare.soilMoisture = soilMoisture
            self.plantsHandler.selectedPlant.plantCare.ph = ph
            self.plantsHandler.selectedPlant.plantCare.salinity = salinity
            self.plantsHandler.selectedPlant.plantCare.lightLevel = lightLevel
            self.plantsHandler.selectedPlant.plantCare.temperature = temperature
            try:
                self.plantDb.updatePlant(self.plantsHandler.selectedPlant)

                self.updateCurrentPlant()
                self.updatePlants()

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

                self.updateCurrentPlant()
                self.updatePlants()

                return True
            except Exception as e:
                print(f"Error updating plant image: {e}")
                self.setCurrentPlant(self.plantsHandler.selectedPlant.id)
                return False
        return False
    
    @Slot()
    def resetCurrentPlant(self):
        self.plantsHandler.resetCurrentPlant()

    def updateCurrentPlant(self):
        if (self.plantsHandler.selectedPlant):
            try:
                self.plantsHandler.setCurrentPlant(self.plantDb.getPlantById(self.plantsHandler.selectedPlant.id))
                return True
            except Exception as e:
                print(f"Error updating current plant: {e}")
                return False

    def updatePlantsAndResetCurrentPlant(self):
        self.updatePlants()
        self.resetCurrentPlant()

    def updatePlants(self):
        self.plantModel.updateModel(self.plantDb.getAllPlants())

    @Slot()
    def tooglePotVisibility(self):
        self.allPotsVisible = not self.allPotsVisible
        self.allPotsShownChanged.emit()
        self.updatePotsAndResetCurrentPot()

    @Slot(str, int, result = bool)
    def addPot(self, potName: str, plantId: int):
        try: 
            pot = Pot(None, potName, None if plantId < 0 else plantId, None, False)
            self.potDb.addPot(pot)

            self.updatePotsAndResetCurrentPot()

            return True
        except Exception as e:
            print(f"Error adding pot: {e}")
            return False
        
    @Slot(int, result=bool)
    def setCurrentPot(self, id):
        try:
            pot = self.potDb.getPotById(id)

            plant = self.plantDb.getPlantById(pot.plantId)
            pot.setPlant(plant)

            self.potsHandler.setCurrentPot(pot)
            return True
        except Exception as e:
            self.potsHandler.setCurrentPot(None)
            print(f"Error setting current pot: {e}")
            return False
        
    @Slot(result=bool)
    def removeCurrentPot(self):
        if (self.potsHandler.selectedPot):
            try:
                self.potDb.removePotById(self.potsHandler.selectedPot.id)

                self.updatePotsAndResetCurrentPot()
                
                return True
            except Exception as e:
                print(f"Error removing pot: {e}")
                return False
        return False
    
    @Slot(result=bool)
    def removePlantFromCurrentPot(self):
        if (self.potsHandler.selectedPot):
            try:
                self.potDb.removePlantFromPot(self.potsHandler.selectedPot)

                self.updateCurrentPot()

                self.updatePots()
                
                return True
            except Exception as e:
                print(f"Error removing plant from pot: {e}")
                return False
        return False

    @Slot()
    def resetCurrentPot(self):
        self.potsHandler.resetCurrentPot()

    @Slot()
    def updatePotsSensorData(self):
        if (PotsDataSampler.updateSensorData(self.potDb)):
            self.updatePotsAndResetCurrentPot()

    def updateCurrentPot(self):
        if (self.potsHandler.selectedPot):
            try:
                self.potsHandler.setCurrentPot(self.potDb.getPotById(self.potsHandler.selectedPot.id))
                return True
            except Exception as e:
                print(f"Error updating current pot: {e}")
                return False
        return False

    def updatePots(self):
        pots = self.potDb.getAllPots() if self.allPotsVisible else self.potDb.getAllPotsWithoutPlants()
        potsMerged = []    
        self.plantDb.getAllPlantsDict()
        for pot in pots:
            plant = self.plantDb.getPlantById(pot.plantId)
            if (pot.plantId is not None and plant is None):
                Exception(f"Pot {pot.id} has invalid plant id {pot.plantId}, cascade delete not working")
                exit(1)
            if plant:
                pot.setPlant(plant)
            potsMerged.append(pot)

        self.potModel.updateModel(potsMerged)

    def updatePotsAndResetCurrentPot(self):
        self.updatePots()
        self.resetCurrentPot()    