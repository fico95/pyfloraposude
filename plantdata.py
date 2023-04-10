class PlantData:
    def __init__(self, soil_moisture: float, ph: float, salinity: float,
                 light_level: float, temperature: float):
        self.update(soil_moisture, ph, salinity, light_level, temperature)

    def update(self, soil_moisture: float, ph: float, salinity: float,
               light_level: float, temperature: float):
        self.soil_moisture = soil_moisture
        self.ph = ph
        self.salinity = salinity
        self.light_level = light_level
        self.temperature = temperature

    def to_dict(self):
        return {
            "soil_moisture": self.soil_moisture,
            "ph": self.ph,
            "salinity": self.salinity,
            "light_level": self.light_level,
            "temperature": self.temperature
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["soil_moisture"],
            data["ph"],
            data["salinity"],
            data["light_level"],
            data["temperature"]
        )