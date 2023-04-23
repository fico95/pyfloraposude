class PlantData:
    def __init__(self, soilMoisture: float, ph: float, salinity: float,
                 lightLevel: float, temperature: float):
        self.update(soilMoisture, ph, salinity, lightLevel, temperature)
        
    def update(self, soilMoisture: float, ph: float, salinity: float,
               lightLevel: float, temperature: float):
        self.soilMoisture = soilMoisture
        self.ph = ph
        self.salinity = salinity
        self.lightLevel = lightLevel
        self.temperature = temperature