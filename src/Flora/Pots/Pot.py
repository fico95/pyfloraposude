from Flora.Plants.Plant import Plant

class Pot:
    def __init__(self, id : int, potName : str, plantId : int, sensorData : list, isBroken : bool):
        self.id = id
        self.potName = potName
        self.plantId = plantId
        self.Plant = None
        self.sensorData = sensorData
        self.isBroken = isBroken

    def setPlant(self, plant: Plant):
        self.plant = plant