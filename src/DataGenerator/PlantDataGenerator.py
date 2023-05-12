import random

from Flora.Plants.PlantData import PlantData
from DataGenerator import TemperatureGenerator

def getPlantDataCampus(numberOfSamples, differentTemperature = False):
    latitudeCampus = 45.8102
    longitudeCampus = 15.9411
    return getPlantDataForPosition(latitudeCampus, longitudeCampus, numberOfSamples, differentTemperature)

def randomPlantData(numberOfSamples):
    data = []
    for i in range(numberOfSamples):
        plantData = PlantData(getSoilMoisture(),
                              getPh(),
                              getSalinity(),
                              getLightLevel(),
                              getTemperature())
        data.append(plantData)

    return data

def getPlantDataForPosition(latitude, longitude, numberOfSamples, differentTemperature = False):
    temperatureCelsius = getTemperatureForPossition(latitude, longitude)

    data = []
    for i in range(numberOfSamples):
        plantData = PlantData(getSoilMoisture(),
                              getPh(),
                              getSalinity(),
                              getLightLevel(),
                              getTemperature() if differentTemperature else temperatureCelsius)
        data.append(plantData)

    return data

def getTemperatureForPossition(latitude, longitude):
    temperatureCelsiusRangeLow, temperatureCelsiusRangeHigh = PlantData.temperatureRange()
    temperatureCelsius = round(TemperatureGenerator.getTemperature(latitude, longitude), 1)
    if temperatureCelsius is not None:
        return max(min(temperatureCelsius, temperatureCelsiusRangeHigh), temperatureCelsiusRangeLow)
    return getTemperature()

def getTemperature():
    temperatureCelsiusRangeLow, temperatureCelsiusRangeHigh = PlantData.temperatureRange()
    temperatureCelsius = round(random.uniform(temperatureCelsiusRangeLow, temperatureCelsiusRangeHigh), 1)
    return temperatureCelsius

def getSoilMoisture():
    soilMoistureRangeLow, soilMoistureRangeHigh = PlantData.soilMoistureRange()
    soilMoisture = round(random.uniform(soilMoistureRangeLow, soilMoistureRangeHigh), 1)
    return soilMoisture

def getPh():
    phLevelRangeLow, phLevelRangeHigh = PlantData.phRange()
    ph = round(random.uniform(phLevelRangeLow, phLevelRangeHigh), 1)
    return ph

def getSalinity():
    salinitLevelRangeLow, salinitLevelRangeHigh = PlantData.salinityRange()
    salinity = round(random.uniform(salinitLevelRangeLow, salinitLevelRangeHigh), 1)
    return salinity

def getLightLevel():
    lightLevelRangeLow, lightLevelRangeHigh = PlantData.lightLevelRange()
    lightLevel = round(random.uniform(lightLevelRangeLow, lightLevelRangeHigh), 1)
    return lightLevel
