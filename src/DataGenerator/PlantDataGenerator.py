import random

from Flora.Plants.PlantData import PlantData
from DataGenerator import TemperatureGenerator

def generatePlantDataCampus(numberOfSamples, differentTemperature = False):
    latitudeCampus = 45.8102
    longitudeCampus = 15.9411
    return generatePlantDataForPosition(latitudeCampus, longitudeCampus, numberOfSamples, differentTemperature)

def generateRandomPlantData(numberOfSamples):
    data = []
    for i in range(numberOfSamples):
        plantData = PlantData(generateSoilMoisture(),
                              generatePh(),
                              generateSalinity(),
                              generateLightLevel(),
                              generateTemperature())
        data.append(plantData)

    return data

def generatePlantDataForPosition(latitude, longitude, numberOfSamples, differentTemperature = False):
    temperatureCelsius = generateTemperatureForPosition(latitude, longitude)

    data = []
    for i in range(numberOfSamples):
        plantData = PlantData(generateSoilMoisture(),
                              generatePh(),
                              generateSalinity(),
                              generateLightLevel(),
                              generateTemperature() if differentTemperature else temperatureCelsius)
        data.append(plantData)

    return data

def generateTemperatureForPosition(latitude, longitude):
    temperatureCelsiusRangeLow, temperatureCelsiusRangeHigh = PlantData.temperatureRange()
    temperatureCelsius = round(TemperatureGenerator.generateTemperature(latitude, longitude), 1)
    if temperatureCelsius is not None:
        return max(min(temperatureCelsius, temperatureCelsiusRangeHigh), temperatureCelsiusRangeLow)
    return generateTemperature()

def generateTemperature():
    temperatureCelsiusRangeLow, temperatureCelsiusRangeHigh = PlantData.temperatureRange()
    temperatureCelsius = round(random.uniform(temperatureCelsiusRangeLow, temperatureCelsiusRangeHigh), 1)
    return temperatureCelsius

def generateSoilMoisture():
    soilMoistureRangeLow, soilMoistureRangeHigh = PlantData.soilMoistureRange()
    soilMoisture = round(random.uniform(soilMoistureRangeLow, soilMoistureRangeHigh), 1)
    return soilMoisture

def generatePh():
    phLevelRangeLow, phLevelRangeHigh = PlantData.phRange()
    ph = round(random.uniform(phLevelRangeLow, phLevelRangeHigh), 1)
    return ph

def generateSalinity():
    salinitLevelRangeLow, salinitLevelRangeHigh = PlantData.salinityRange()
    salinity = round(random.uniform(salinitLevelRangeLow, salinitLevelRangeHigh), 1)
    return salinity

def generateLightLevel():
    lightLevelRangeLow, lightLevelRangeHigh = PlantData.lightLevelRange()
    lightLevel = round(random.uniform(lightLevelRangeLow, lightLevelRangeHigh), 1)
    return lightLevel
