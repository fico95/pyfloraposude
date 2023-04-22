import random

from Flora.Plants.PlantData import PlantData
from DataGenerator import TemperatureGenerator

def getPlantDataCampus(numberOfSamples, differentTemperature = False):
    latitudeCampus = 45.8102
    longitudeCampus = 15.9411
    return getPlantDataForPosition(latitudeCampus, longitudeCampus, numberOfSamples, differentTemperature)

def getRandomPlantData(numberOfSamples):
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
    # Get current temperature from OpenMeteo API, or generate random data if API call fails
    temperatureCelsius = TemperatureGenerator.getTemperature(latitude, longitude)
    if temperatureCelsius is not None:
        return round(temperatureCelsius, 1)
    return getTemperature()

def getTemperature():
    # Generate random data for temperature
    temperatureCelsius = round(random.uniform(-10, 40), 1)
    return temperatureCelsius

def getSoilMoisture():
    # Generate random data for soil moisture
    soilMoisture = round(random.uniform(0, 100), 1)
    return soilMoisture

def getPh():
    # Generate random data for pH values
    ph = round(random.uniform(0, 14), 1)
    return ph

def getSalinity():
    # Generate random data for salinity
    salinity = round(random.uniform(0, 100), 1)
    return salinity

def getLightLevel():
    # Generate random data for light level
    lightLevel = round(random.uniform(0, 100), 1)
    return lightLevel
