import json

from typing import Tuple, List

class PlantData:
    def __init__(self, soilMoisture: float, ph: float, salinity: float,
                 lightLevel: float, temperature: float):
        self.soilMoisture = soilMoisture
        self.ph = ph
        self.salinity = salinity
        self.lightLevel = lightLevel
        self.temperature = temperature

    @staticmethod
    def propertiesCount() -> int:
        return 5

    @staticmethod
    def soilMoistureRange() -> Tuple[float, float]:
        return (0.0, 100.0)
    
    @staticmethod
    def phRange() -> Tuple[float, float]:
        return (0.0, 14.0)
    
    @staticmethod
    def salinityRange() -> Tuple[float, float]:
        return (0.0, 100.0)
    
    @staticmethod
    def lightLevelRange() -> Tuple[float, float]:
        return (0.0, 100.0)
    
    @staticmethod
    def temperatureRange() -> Tuple[float, float]:
        return (-10.0, 40.0)
    
    @staticmethod
    def soilMouistureOkTolerance() -> float:
        return 20.0
    
    @staticmethod
    def phOkTolerance() -> float:
        return 1.5
    
    @staticmethod
    def salinityOkTolerance() -> float:
        return 20.0
    
    @staticmethod
    def lightLevelOkTolerance() -> float:
        return 20.0
    
    @staticmethod
    def temperatureOkTolerance() -> float:
        return 5.0

    def soilMoistureOk(self, soilMoisture: float) -> bool:
        return ((soilMoisture >= self.soilMoisture - self.soilMouistureOkTolerance()) and \
                (soilMoisture <= self.soilMoisture + self.soilMouistureOkTolerance()))
    
    def phOk(self, ph: float) -> bool:
        return ((ph >= self.ph - self.phOkTolerance()) and \
                (ph <= self.ph + self.phOkTolerance()))

    def salinityOk(self, salinity: float) -> bool:
        return ((salinity >= self.salinity - self.salinityOkTolerance()) and \
                (salinity <= self.salinity + self.salinityOkTolerance()))
    
    def lightLevelOk(self, lightLevel: float) -> bool:
        return ((lightLevel >= self.lightLevel - self.lightLevelOkTolerance()) and \
                (lightLevel <= self.lightLevel + self.lightLevelOkTolerance()))

    def temperatureOk(self, temperature: float) -> bool:
        return ((temperature >= self.temperature - self.temperatureOkTolerance()) and \
                (temperature <= self.temperature + self.temperatureOkTolerance()))

    @classmethod
    def fromJson(cls, jsonData: str) -> 'PlantData':
        plantData = cls(0.0, 0.0, 0.0, 0.0, 0.0)
        plantData.__dict__ = json.loads(jsonData)
        return plantData

    def toJson(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def listFromJson(cls, jsonData: str) -> List['PlantData']:
        return [cls.fromJson(plantDataJson) for plantDataJson in json.loads(jsonData)]

    @classmethod
    def listToJson(cls, plantDataList: List['PlantData']) -> str:
        return json.dumps([plantData.toJson() for plantData in plantDataList])