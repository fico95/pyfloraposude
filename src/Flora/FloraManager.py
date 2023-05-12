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
        if (not self.plantDb.tableCreated()):
            self.plantDb.createTable()
            self.plantDb.fillTable(imagesPath)

        self.plantModel = PlantModel(self)
        self.plantsHandler = PlantsHandler(self)

        self.potDb = PotDb(dbPath)
        if (not self.potDb.tableCreated()):
            self.potDb.createTable()
            if (self.potDb.potsCount() == 0):
                self.potDb.fillTable(self.plantDb.randomPlant())

        self.potModel = PotModel(self)
        self.potsHandler = PotsHandler(self)

        self.updatePlantsAndResetCurrentPlant()
        self.updatePotsAndResetCurrentPot()


    @Slot()
    def tooglePotVisibility(self):
        self.allPotsVisible = not self.allPotsVisible
        self.allPotsShownChanged.emit()
        self.updatePotsAndResetCurrentPot()

    @Slot()
    def updatePotsSensorData(self):
        if (PotsDataSampler.updateSensorData(self.potDb)):
            self.updatePotsAndResetCurrentPot()


    @Slot(str, str, float, float, float, float, float, result = bool)
    def addPlant(self, name, imagePath, soilMoisture, ph, salinity, lightLevel, temperature) -> bool:
        try:
            plant = Plant(None, name, imagePath, PlantData(soilMoisture, ph, salinity, lightLevel, temperature))
            self.plantDb.addPlant(plant)

            self.updatePlantsAndResetCurrentPlant()

            return True
        except Exception as e:
            print(f"Error adding plant: {e}")
            return False
        return False
        
    @Slot(result = bool)
    def removeCurrentPlant(self) -> bool:
        if (self.plantsHandler.currentPlantValid()):
            try:
                self.plantDb.removePlantById(self.plantsHandler.currentPlant.id)

                self.updatePlantsAndResetCurrentPlant()
                self.updatePotsAndResetCurrentPot()
                
                return True
            except Exception as e:
                print(f"Error removing plant: {e}")
                return False
        return False
        
    @Slot(int, result=bool)
    def setCurrentPlant(self, id) -> bool:
        try:
            plant = self.plantDb.fetchPlantById(id)
            self.plantsHandler.setCurrentPlant(plant)
            return True
        except Exception as e:
            self.plantsHandler.setCurrentPlant(None)
            print(f"Error setting current plant: {e}")
            return False
        return False
        
    @Slot()
    def resetCurrentPlant(self):
        self.plantsHandler.resetCurrentPlant()
        
    @Slot(str, result=bool)
    def updateCurrentPlantName(self, name) -> bool:
        if (self.plantsHandler.currentPlantValid()):
            self.plantsHandler.currentPlant.name = name
            try:
                self.plantDb.updatePlant(self.plantsHandler.currentPlant)

                self.updatePlantsAndCurrentPlant()
                self.updatePotsAndResetCurrentPot()

                return True
            except Exception as e:
                print(f"Error updating plant name: {e}")
                self.updateCurrentPlant()
                return False
        return False

    @Slot(float, float, float, float, float, result = bool)
    def updateCurrentPlantData(self, soilMoisture, ph, salinity, lightLevel, temperature) -> bool:
        if (self.plantsHandler.currentPlantValid()):
            self.plantsHandler.currentPlant.plantCare.soilMoisture = soilMoisture
            self.plantsHandler.currentPlant.plantCare.ph = ph
            self.plantsHandler.currentPlant.plantCare.salinity = salinity
            self.plantsHandler.currentPlant.plantCare.lightLevel = lightLevel
            self.plantsHandler.currentPlant.plantCare.temperature = temperature
            try:
                self.plantDb.updatePlant(self.plantsHandler.currentPlant)

                self.updatePlantsAndCurrentPlant()
                self.updatePotsAndResetCurrentPot()

                return False
            except Exception as e:
                print(f"Error updating plant: {e}")
                self.updateCurrentPlant()
                return False
        return False
    
    @Slot(str, result = bool)
    def updateCurrentPlantImage(self, imagePath):
        if (self.plantsHandler.currentPlantValid()):
            self.plantsHandler.currentPlant.imagePath = imagePath
            try:
                self.plantDb.updatePlant(self.plantsHandler.currentPlant)

                self.updatePlantsAndCurrentPlant()

                return True
            except Exception as e:
                print(f"Error updating plant image: {e}")
                self.updateCurrentPlant()
                return False
        return False
    
    
    @Slot(str, int, result = bool)
    def addPot(self, potName: str, plantId: int) -> bool:
        try: 
            pot = Pot(None, potName, None if plantId < 0 else plantId, None, False)
            self.potDb.addPot(pot)

            self.updatePotsAndResetCurrentPot()

            return True
        except Exception as e:
            print(f"Error adding pot: {e}")
            return False
        return False
    
    @Slot(result=bool)
    def removeCurrentPot(self) -> bool:
        if (self.potsHandler.currentPotValid()):
            try:
                self.potDb.removePotById(self.potsHandler.currentPot.id)

                self.updatePotsAndResetCurrentPot()
                
                return True
            except Exception as e:
                print(f"Error removing pot: {e}")
                return False
        return False
        
    @Slot(int, result=bool)
    def setCurrentPot(self, id) -> bool:
        try:
            pot = self.potDb.fetchPotById(id)

            plant = self.plantDb.fetchPlantById(pot.plantId)
            pot.setPlant(plant)

            self.potsHandler.setCurrentPot(pot)
            return True
        except Exception as e:
            self.potsHandler.setCurrentPot(None)
            print(f"Error setting current pot: {e}")
            return False
        return False
        
    @Slot()
    def resetCurrentPot(self):
        self.potsHandler.resetCurrentPot()

    @Slot(str, result=bool)
    def updateCurrentPotName(self, name) -> bool:
        if (self.potsHandler.currentPotValid()):
            self.potsHandler.currentPot.potName = name
            try:
                self.potDb.updatePotName(self.potsHandler.currentPot)

                self.updatePotsAndCurrentPot()

                return True
            except Exception as e:
                print(f"Error updating pot: {e}")
                self.updateCurrentPot()
                return False
        return False

    @Slot(int, result=bool)
    def addPlantToCurrentPot(self, plantId) -> bool:
        if (self.potsHandler.currentPotValid()):
            try:
                plant = self.plantDb.fetchPlantById(plantId)
                if (plant == None):
                    return False
                self.potDb.addPlantToPot(self.potsHandler.currentPot, plant)

                self.updatePotsAndCurrentPot()
                
                return True
            except Exception as e:
                print(f"Error adding plant to pot: {e}")
                self.updateCurrentPot()
                return False
        return False

    @Slot(result=bool)
    def removePlantFromCurrentPot(self) -> bool:
        if (self.potsHandler.currentPot):
            try:
                self.potDb.removePlantFromPot(self.potsHandler.currentPot)

                self.updatePotsAndCurrentPot()
                
                return True
            except Exception as e:
                print(f"Error removing plant from pot: {e}")
                self.updateCurrentPot()
                return False
        return False


    def updatePlantsAndCurrentPlant(self):
        self.updatePlants()
        self.updateCurrentPlant()

    def updatePlantsAndResetCurrentPlant(self):
        self.updatePlants()
        self.resetCurrentPlant()

    def updatePlants(self):
        self.plantModel.updateModel(self.plantDb.plants())

    def updateCurrentPlant(self) -> bool:
        if (self.plantsHandler.currentPlant):
            try:
                self.plantsHandler.setCurrentPlant(self.plantDb.fetchPlantById(self.plantsHandler.currentPlant.id))
                return True
            except Exception as e:
                print(f"Error updating current plant: {e}")
                return False
        return False
    

    def updatePotsAndCurrentPot(self):
        self.updatePots()
        self.updateCurrentPot()

    def updatePotsAndResetCurrentPot(self):
        self.updatePots()
        self.resetCurrentPot()

    def updatePots(self):
        pots = self.potDb.pots() if self.allPotsVisible else self.potDb.potsWithoutPlants()
        potsMerged = []    
        self.plantDb.plantsDictionary()
        for pot in pots:
            plant = self.plantDb.fetchPlantById(pot.plantId)
            if (pot.plantId is not None and plant is None):
                Exception(f"Pot {pot.id} has invalid plant id {pot.plantId}, cascade delete not working")
                exit(1)
            if plant:
                pot.setPlant(plant)
            potsMerged.append(pot)
        self.potModel.updateModel(potsMerged)

    def updateCurrentPot(self) -> bool:
        if (self.potsHandler.currentPot):
            return self.setCurrentPot(self.potsHandler.currentPot.id)
        return False