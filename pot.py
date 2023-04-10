from plant import Plant
from plantdata import PlantData

from typing import List, Optional

class Pot:
    def __init__(self, id: int, name: str, is_broken: bool, plant: Optional[Plant] = None,
                 sensor_data: List[PlantData] = []):
        self.id = id
        self.name = name
        self.is_broken = is_broken
        self.plant = plant
        self.sensor_data = sensor_data

    def to_dict(self):
        plant_dict = None
        if self.plant:
            plant_dict = self.plant.to_dict()
        sensor_data_dicts = [data.to_dict() for data in self.sensor_data]
        return {
            "id": self.id,
            "name": self.name,
            "is_broken": self.is_broken,
            "plant": plant_dict,
            "sensor_data": sensor_data_dicts
        }

    @classmethod
    def from_dict(cls, data):
        id = data["id"]
        name = data["name"]
        is_broken = data["is_broken"]
        plant_data = data.get("plant")
        if plant_data:
            plant = Plant.from_dict(plant_data)
        else:
            plant = None
        sensor_data = [PlantData.from_dict(data_dict) for data_dict in data.get("sensor_data", [])]
        return cls(id=id, name=name, is_broken=is_broken, plant=plant, sensor_data=sensor_data)
