import json

class PlantData:
    def __init__(self, soilMoisture: float, ph: float, salinity: float,
                 lightLevel: float, temperature: float):
        self.soilMoisture = soilMoisture
        self.ph = ph
        self.salinity = salinity
        self.lightLevel = lightLevel
        self.temperature = temperature

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