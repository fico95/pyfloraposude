from Flora.Plants.Plant import Plant
from Flora.Plants.PlantData import PlantData

class Pot:
    def __init__(self, potName : str, plant : Plant=None):
        self.id = None
        self.potName = potName
        self.plant = plant
        self.sensorData = []
        self.isBroken = False

    def setId(self, id: int):
        self.id = id