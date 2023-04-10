import plantdata as PlantData

import random

import temperature

def generate_random_data(latitude, longitude, number_of_samples):
    # Get current temperature from OpenMeteo API, or generate random data if API call fails
    temperature_celsius = temperature.get_temperature(latitude, longitude)
    if temperature_celsius is None:
        temperature_celsius = min(max(round(random.uniform(-10, 40), 1), -10), 40)
    else:
        temperature_celsius = round(temperature_celsius, 1)

    data = []
    for i in range(number_of_samples):
        # Generate random data for soil moisture
        soil_moisture = round(random.uniform(0, 100), 1)

        # Generate random data for pH values
        ph_value = round(random.uniform(0, 14), 1)

        # Generate random data for salinity
        salinity = round(random.uniform(0, 100), 1)

        # Generate random data for light level
        light_level = round(random.uniform(0, 100), 1)

        plant_data = PlantData(soil_moisture=soil_moisture, ph_value=ph_value, salinity=salinity,
                            light_level=light_level, temperature=temperature_celsius)
        data.append(plant_data)

    return data