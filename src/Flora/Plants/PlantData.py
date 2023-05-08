import json

class PlantData:
    def __init__(self, soilMoisture: float, ph: float, salinity: float,
                 lightLevel: float, temperature: float):
        self.soilMoisture = soilMoisture
        self.ph = ph
        self.salinity = salinity
        self.lightLevel = lightLevel
        self.temperature = temperature

    def soilMoistureOk(self, soilMoisture: float):
        return ((soilMoisture >= self.soilMoisture - 20.0) and \
                (soilMoisture <= self.soilMoisture + 20.0))
    
    def phOk(self, ph: float):
        return ((ph >= self.ph - 1.5) and \
                (ph <= self.ph + 1.5))

    def salinityOk(self, salinity: float):
        return ((salinity >= self.salinity - 20) and \
                (salinity <= self.salinity + 20))
    
    def lightLevelOk(self, lightLevel: float):
        return ((lightLevel >= self.lightLevel - 20) and \
                (lightLevel <= self.lightLevel + 20))

    def temperatureOk(self, temperature: float):
        return ((temperature >= self.temperature - 5) and \
                (temperature <= self.temperature + 5))

    @classmethod
    def fromJson(cls, jsonData: str):
        plantData = cls(0.0, 0.0, 0.0, 0.0, 0.0)
        plantData.__dict__ = json.loads(jsonData)
        return plantData

    def toJson(self):
        return json.dumps(self.__dict__)

    @classmethod
    def listFromJson(cls, jsonData: str):
        return [cls.fromJson(plantDataJson) for plantDataJson in json.loads(jsonData)]

    @classmethod
    def listToJson(cls, plantDataList: list):
        return json.dumps([plantData.toJson() for plantData in plantDataList])