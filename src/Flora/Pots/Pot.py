from Flora.Plants.Plant import Plant
from Flora.Plants.PlantData import PlantData

from typing import List

class Pot:
    def __init__(self, id: int, potName: str, plantId: int, sensorData: List[PlantData], isBroken: bool):
        self.id = id
        self.potName = potName
        self.plantId = plantId
        self.plant = None
        self.sensorData = sensorData if sensorData else []
        self.isBroken = isBroken
        self.maxSensorData = 50

    def plantValid(self) -> bool:
        return self.plant != None

    def setPlant(self, plant: Plant):
        self.plant = plant

    def addSensorData(self, sensorData: PlantData):
        if (len(self.sensorData) >= self.maxSensorData):
            self.sensorData.pop(0)
        self.sensorData.append(sensorData)

    def setBroken(self, isBroken: bool):
        self.isBroken = isBroken

    def plantName(self) -> str:
        if (self.plantValid()):
            return self.plant.name
        return ""
    
    def plantImagePath(self) -> str:
        if (self.plantValid()):
            return self.plant.imagePath
        return ""
    
    def plantSoilMoisture(self) -> float:
        if (self.plantValid()):
            return self.plant.plantCare.soilMoisture
        return 0.0
    
    def plantTemperature(self) -> float:
        if (self.plantValid()):
            return self.plant.plantCare.temperature
        return 0.0
    
    def plantLightLevel(self) -> float:
        if (self.plantValid()):
            return self.plant.plantCare.lightLevel
        return 0.0
    
    def plantSalinity(self) -> float:
        if (self.plantValid()):
            return self.plant.plantCare.salinity
        return 0.0

    def plantPh(self) -> float:
        if (self.plantValid()):
            return self.plant.plantCare.ph
        return 0.0
    
    def sensorDataExists(self) -> bool:
        return len(self.sensorData) > 0
    
    def lastSensorSoilMoisture(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].soilMoisture
        return 0.0
    
    def lastSensorTemperature(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].temperature
        return 0.0
    
    def lastSensorLightLevel(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].lightLevel
        return 0.0
    
    def lastSensorSalinity(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].salinity
        return 0.0
    
    def lastSensorPh(self) -> float:
        if (self.sensorDataExists()):
            return self.sensorData[-1].ph
        return 0.0
    
    def soilMoistureOk(self) -> bool:
        if (self.plantValid()):
            return self.plant.plantCare.soilMoistureOk(self.lastSensorSoilMoisture())
        return True
    
    def temperatureOk(self) -> bool:
        if (self.plantValid()):
            return self.plant.plantCare.temperatureOk(self.lastSensorTemperature())
        return True
    
    def lightLevelOk(self) -> bool:
        if (self.plantValid()):
            return self.plant.plantCare.lightLevelOk(self.lastSensorLightLevel())
        return True
    
    def salinityOk(self) -> bool:
        if (self.plantValid()):
            return self.plant.plantCare.salinityOk(self.lastSensorSalinity())
        return True
    
    def phOk(self) -> bool:
        if (self.plantValid()):
            return self.plant.plantCare.phOk(self.lastSensorPh())
        return True

