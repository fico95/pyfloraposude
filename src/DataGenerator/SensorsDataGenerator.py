import random

from DataGenerator import TemperatureGenerator

def getSensorsData(numberOfSamples):
    latitudeCampus = 45.8102
    longitudeCampus = 15.9411
    return getSensorsData(latitudeCampus, longitudeCampus, numberOfSamples)

def getSensorsData(latitude, longitude, numberOfSamples):
    # Get current temperature from OpenMeteo API, or generate random data if API call fails
    temperatureCelsius = TemperatureGenerator.getTemperature(latitude, longitude)
    if temperatureCelsius is None:
        temperatureCelsius = min(max(round(random.uniform(-10, 40), 1), -10), 40)
    else:
        temperatureCelsius = round(temperatureCelsius, 1)

    data = []
    for i in range(numberOfSamples):
        # Generate random data for soil moisture
        soilMoisture = round(random.uniform(0, 100), 1)

        # Generate random data for pH values
        ph = round(random.uniform(0, 14), 1)

        # Generate random data for salinity
        salinity = round(random.uniform(0, 100), 1)

        # Generate random data for light level
        lightLevel = round(random.uniform(0, 100), 1)

        plantData = {"soilMoisture": soilMoisture, 
                      "ph": ph, 
                      "salinity": salinity,
                      "lightLevel": lightLevel,
                      "temperature": temperatureCelsius}
        data.append(plantData)

    return data