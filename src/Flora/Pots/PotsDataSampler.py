from DataGenerator.PlantDataGenerator import generatePlantDataCampus

from Flora.Pots.PotDb import PotDb

import random

class PotsDataSampler:
    def __init__(self):
        pass
    
    @staticmethod
    def updateSensorData(potDb: PotDb) -> bool:
        try:
            pots = potDb.pots()
        except Exception as e:
            print(f"Error getting pots: {e}")
            return False
        
        try:
            potsSensorData = generatePlantDataCampus(len(pots))
        except Exception as e:
            print(f"Error getting pots sensor data: {e}")
            return False
        
        success = True
        for pot, potSensorData in zip(pots, potsSensorData):
            if (pot.isBroken or pot.plantId is None):
                continue
            try:
                broken = PotsDataSampler.generateBrokenProbability()
                pot.setBroken(broken)
                if (not pot.isBroken):
                    pot.addSensorData(potSensorData)
                potDb.updatePotSensorDataAndBroken(pot)
            except Exception as e:
                print(f"Error updating pot sensor data: {e}")
                success = False
                continue
        
        return success
    
    @staticmethod
    def generateBrokenProbability() -> bool:
        return random.random() > 0.95
