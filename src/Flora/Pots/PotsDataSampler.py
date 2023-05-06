from DataGenerator.PlantDataGenerator import getPlantDataCampus

from Flora.Pots.PotDb import PotDb

class PotsDataSampler:
    def __init__(self):
        pass
    
    @staticmethod
    def updateSensorData(potDb: PotDb) -> bool:
        try:
            pots = potDb.getAllPots()
        except Exception as e:
            print(f"Error getting pots: {e}")
            return False
        
        try:
            potsSensorData = getPlantDataCampus(len(pots))
        except Exception as e:
            print(f"Error getting pots sensor data: {e}")
            return False
        
        success = True
        for pot, potSensorData in zip(pots, potsSensorData):
            try:
                pot.addSensorData(potSensorData)
                potDb.updatePotSensorData(pot)
            except Exception as e:
                print(f"Error updating pot sensor data: {e}")
                success = False
                continue
        
        return success