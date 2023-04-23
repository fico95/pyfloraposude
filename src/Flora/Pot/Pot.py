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