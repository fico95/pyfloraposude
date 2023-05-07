from Flora.Plants.Plant import Plant

class Pot:
    def __init__(self, id : int, potName : str, plantId : int, sensorData : list, isBroken : bool):
        self.id = id
        self.potName = potName
        self.plantId = plantId
        self.plant = None
        self.sensorData = sensorData if sensorData else []
        self.isBroken = isBroken
        self.maxSensorData = 50

    def setPlant(self, plant: Plant):
        self.plant = plant

    def addSensorData(self, sensorData):
        if (len(self.sensorData) >= self.maxSensorData):
            self.sensorData.pop(0)
        self.sensorData.append(sensorData)

    def setBroken(self, isBroken : bool):
        self.isBroken = isBroken