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
def plantDataToJson(plantData: PlantData):
    return json.dumps(plantData.__dict__)
    
@staticmethod
def plantDataFromJson(jsonData: str):
    plantData = PlantData(0.0, 0.0, 0.0, 0.0, 0.0)
    plantData.__dict__ = json.loads(jsonData)
    return plantData

@staticmethod
def plantDataListToJson(plantDataList: list):
    return json.dumps([plantDataToJson(plantData) for plantData in plantDataList])

@staticmethod
def plantDataListFromJson(jsonData: str):
    return [plantDataFromJson(plantDataJson) for plantDataJson in json.loads(jsonData)]