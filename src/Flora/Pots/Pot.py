from Flora.Plants.Plant import Plant

class Pot:
    def __init__(self, id : int, potName : str, plantId : int, sensorData : list, isBroken : bool):
        self.id = id
        self.potName = potName
        self.plantId = plantId
        self.plant = None
        self.sensorData = sensorData if sensorData else []
        self.isBroken = isBroken

    def setPlant(self, plant: Plant):
        self.plant = plant

    def addSensorData(self, sensorData):
        self.sensorData.append(sensorData)

    def setBroken(self, isBroken : bool):
        if (self.isBroken):
            return
        self.isBroken = isBroken