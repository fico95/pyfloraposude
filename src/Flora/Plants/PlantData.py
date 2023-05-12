import json

class PlantData:
    def __init__(self, soilMoisture: float, ph: float, salinity: float,
                 lightLevel: float, temperature: float):
        self.soilMoisture = soilMoisture
        self.ph = ph
        self.salinity = salinity
        self.lightLevel = lightLevel
        self.temperature = temperature

    @staticmethod
    def soilMoistureRange():
        return (0.0, 100.0)
    
    @staticmethod
    def phRange():
        return (0.0, 14.0)
    
    @staticmethod
    def salinityRange():
        return (0.0, 100.0)
    
    @staticmethod
    def lightLevelRange():
        return (0.0, 100.0)
    
    @staticmethod
    def temperatureRange():
        return (-10.0, 40.0)
    
    @staticmethod
    def soilMouistureOkTolerance():
        return 20.0
    
    @staticmethod
    def phOkTolerance():
        return 1.5
    
    @staticmethod
    def salinityOkTolerance():
        return 20.0
    
    @staticmethod
    def lightLevelOkTolerance():
        return 20.0
    
    @staticmethod
    def temperatureOkTolerance():
        return 5.0

    def soilMoistureOk(self, soilMoisture: float):
        return ((soilMoisture >= self.soilMoisture - self.soilMouistureOkTolerance()) and \
                (soilMoisture <= self.soilMoisture + self.soilMouistureOkTolerance()))
    
    def phOk(self, ph: float):
        return ((ph >= self.ph - self.phOkTolerance()) and \
                (ph <= self.ph + self.phOkTolerance()))

    def salinityOk(self, salinity: float):
        return ((salinity >= self.salinity - self.salinityOkTolerance()) and \
                (salinity <= self.salinity + self.salinityOkTolerance()))
    
    def lightLevelOk(self, lightLevel: float):
        return ((lightLevel >= self.lightLevel - self.lightLevelOkTolerance()) and \
                (lightLevel <= self.lightLevel + self.lightLevelOkTolerance()))

    def temperatureOk(self, temperature: float):
        return ((temperature >= self.temperature - self.temperatureOkTolerance()) and \
                (temperature <= self.temperature + self.temperatureOkTolerance()))

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