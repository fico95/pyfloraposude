from Flora.Plants.Plant import Plant

class Pot:
    def __init__(self, id : int, potName : str, plantId : int, sensorData : list, isBroken : bool):
        self.id = id
        self.potName = potName
        self.plantId = plantId
        self.plant = None
        self.sensorData = sensorData if sensorData else []
        self.isBroken = isBroken
        self.maxSensorData = 50

    def setPlant(self, plant: Plant):
        self.plant = plant

    def addSensorData(self, sensorData):
        if (len(self.sensorData) >= self.maxSensorData):
            self.sensorData.pop(0)
        self.sensorData.append(sensorData)

    def setBroken(self, isBroken : bool):
        self.isBroken = isBroken

    def getPlantId(self) -> int:
        if (self.plant):
            return self.plant.id
        return -1

    def getPlantName(self) -> str:
        if (self.plant):
            return self.plant.name
        return ""
    
    def getPlantImagePath(self) -> str:
        if (self.plant):
            return self.plant.imagePath
        return ""
    
    def getPlantSoilMoisture(self) -> float:
        if (self.plant):
            return self.plant.plantCare.soilMoisture
        return 0.0
    
    def getPlantTemperature(self) -> float:
        if (self.plant):
            return self.plant.plantCare.temperature
        return 0.0
    
    def getPlantLightLevel(self) -> float:
        if (self.plant):
            return self.plant.plantCare.lightLevel
        return 0.0
    
    def getPlantSalinity(self) -> float:
        if (self.plant):
            return self.plant.plantCare.salinity
        return 0.0

    def getPlantPh(self) -> float:
        if (self.plant):
            return self.plant.plantCare.ph
        return 0.0
    
    def getLastMeasuredSoilMoisture(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].soilMoisture
        return 0.0
    
    def getLastMeasuredTemperature(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].temperature
        return 0.0
    
    def getLastMeasuredLightLevel(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].lightLevel
        return 0.0
    
    def getLastMeasuredSalinity(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].salinity
        return 0.0
    
    def getLastMeasuredPh(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].ph
        return 0.0
    
    def getSoilMoistureOk(self) -> bool:
        if (self.plant):
            return self.plant.plantCare.soilMoistureOk(self.getLastMeasuredSoilMoisture())
        return True
    
    def getTemperatureOk(self) -> bool:
        if (self.plant):
            return self.plant.plantCare.temperatureOk(self.getLastMeasuredTemperature())
        return True
    
    def getLightLevelOk(self) -> bool:
        if (self.plant):
            return self.plant.plantCare.lightLevelOk(self.getLastMeasuredLightLevel())
        return True
    
    def getSalinityOk(self) -> bool:
        if (self.plant):
            return self.plant.plantCare.salinityOk(self.getLastMeasuredSalinity())
        return True
    
    def getPhOk(self) -> bool:
        if (self.plant):
            return self.plant.plantCare.phOk(self.getLastMeasuredPh())
        return True

    def sensorDataExists(self) -> bool:
        return len(self.sensorData) > 0