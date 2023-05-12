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
        if (self.potDb.getNumPots() == 0):
            self.potDb.fillTable(self.plantDb.randomPlant())

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
        if (self.plantsHandler.currentPlant):
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
    def setCurrentPlant(self, id):
        try:
            plant = self.plantDb.fetchPlantById(id)
            self.plantsHandler.setCurrentPlant(plant)
            return True
        except Exception as e:
            self.plantsHandler.setCurrentPlant(None)
            print(f"Error setting current plant: {e}")
            return False
        
    @Slot(str, float, float, float, float, float, result = bool)
    def updateCurrentPlantData(self, name, soilMoisture, ph, salinity, lightLevel, temperature):
        if (self.plantsHandler.currentPlant):
            self.plantsHandler.currentPlant.name = name
            self.plantsHandler.currentPlant.plantCare.soilMoisture = soilMoisture
            self.plantsHandler.currentPlant.plantCare.ph = ph
            self.plantsHandler.currentPlant.plantCare.salinity = salinity
            self.plantsHandler.currentPlant.plantCare.lightLevel = lightLevel
            self.plantsHandler.currentPlant.plantCare.temperature = temperature
            try:
                self.plantDb.updatePlant(self.plantsHandler.currentPlant)

                self.updateCurrentPlant()
                self.updatePlants()

                return False
            except Exception as e:
                print(f"Error updating plant: {e}")
                self.setCurrentPlant(self.plantsHandler.currentPlant.id)
                return False
        return False
    
    @Slot(str, result = bool)
    def updateCurrentPlantImage(self, imagePath):
        if (self.plantsHandler.currentPlant):
            self.plantsHandler.currentPlant.imagePath = imagePath
            try:
                self.plantDb.updatePlant(self.plantsHandler.currentPlant)

                self.updateCurrentPlant()
                self.updatePlants()

                return True
            except Exception as e:
                print(f"Error updating plant image: {e}")
                self.setCurrentPlant(self.plantsHandler.currentPlant.id)
                return False
        return False
    
    @Slot()
    def resetCurrentPlant(self):
        self.plantsHandler.resetCurrentPlant()

    def updateCurrentPlant(self):
        if (self.plantsHandler.currentPlant):
            try:
                self.plantsHandler.setCurrentPlant(self.plantDb.fetchPlantById(self.plantsHandler.currentPlant.id))
                return True
            except Exception as e:
                print(f"Error updating current plant: {e}")
                return False

    def updatePlantsAndResetCurrentPlant(self):
        self.updatePlants()
        self.resetCurrentPlant()

    def updatePlants(self):
        self.plantModel.updateModel(self.plantDb.plants())

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

            plant = self.plantDb.fetchPlantById(pot.plantId)
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

    @Slot(int, result=bool)
    def addPlantToCurrentPot(self, plantId):
        if (self.potsHandler.selectedPot):
            try:
                plant = self.plantDb.fetchPlantById(plantId)
                if (plant == None):
                    return False
                self.potDb.addPlantToPot(self.potsHandler.selectedPot, plant)

                self.updateCurrentPot()
                # TODO: MOVEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                self.resetCurrentPlant()

                self.updatePots()
                
                return True
            except Exception as e:
                print(f"Error adding plant to pot: {e}")
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
    
    @Slot(str, result=bool)
    def updateCurrentPotName(self, name):
        if (self.potsHandler.selectedPot):
            self.potsHandler.selectedPot.potName = name
            try:
                self.potDb.updatePotName(self.potsHandler.selectedPot)

                self.updateCurrentPot()
                self.updatePots()

                return True
            except Exception as e:
                print(f"Error updating pot: {e}")
                self.setCurrentPot(self.potsHandler.selectedPot.id)
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
            return self.setCurrentPot(self.potsHandler.selectedPot.id)
        return False

    def updatePots(self):
        pots = self.potDb.getAllPots() if self.allPotsVisible else self.potDb.getAllPotsWithoutPlants()
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

    def updatePotsAndResetCurrentPot(self):
        self.updatePots()
        self.resetCurrentPot()    