from Flora.Plants.Plant import Plant
from Flora.Plants.PlantData import PlantData
from DataGenerator.PlantDataGenerator import getRandomPlantData

import sqlite3
from typing import List, Optional

class PlantDb:
    def __init__(self, dbPath):
        self.dbPath = dbPath
        self.conn = sqlite3.connect(dbPath)
        self.createTable()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                imagePath TEXT NULL,
                desiredMoisture REAL,
                desiredPh REAL,
                desiredSalinity REAL,
                desiredLight REAL,
                desiredTemperature REAL
            )
        """)
        self.conn.commit()
    
    def fillTable(self, imagesPath):
        plantNames = [("Monstera Deliciosa", imagesPath + "/monstera_deliciosa.png"),
                      ("Fiddle Leaf Fig", imagesPath + "/fiddle_leaf_fig.png"),
                      ("Snake Plant", imagesPath + "/snake_plant.png"),
                      ("Peace Lily", imagesPath + "/peace_lily.png"),
                      ("ZZ Plant", imagesPath + "/zz_plant.png"),
                      ("Pothos", imagesPath + "/pothos.png"),
                      ("Rubber Plant", imagesPath + "/rubber_plant.png"),
                      ("Bird of Paradise", imagesPath + "/bird_of_paradise.png"),
                      ("Chinese Money Plant", imagesPath + "/chinese_money_plant.png"),
                      ("Calathea", imagesPath + "/calathea.png")]
        plantData = getRandomPlantData(len(plantNames))

        for name, data in zip(plantNames, plantData):
            plant = Plant(name[0], name[1], data)
            self.addPlant(plant)

    def addPlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO plants (name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (plant.name, plant.imagePath, plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature))
        self.conn.commit()

    def updatePlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE plants
            SET name=?, imagePath=?, desiredMoisture=?, desiredPh=?, desiredSalinity=?, desiredLight=?, desiredTemperature=?
            WHERE id=?
        """, (plant.name, plant.imagePath, plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature, plant.id))
        self.conn.commit()

    def removePlant(self, plantId):
        cursor = self.conn.cursor()
        cursor.execute("""
            DELETE FROM plants
            WHERE id=?
        """, (plantId,))
        self.conn.commit()

    def getPlantById(self, plantId) -> Optional[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM plants WHERE id=?
        """, (plantId,))
        data = cursor.fetchone()
        if data is None:
            return None
        id, name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
        plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
        plant = Plant(name, imagePath, plantCare)
        plant.setId(id)
        return plant

    def getAllPlants(self) -> List[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM plants
        """)
        plants = []
        for data in cursor.fetchall():
            plantId, name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
            plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            plant = Plant(name, imagePath, plantCare)
            plant.setId(plantId)
            plants.append(plant)
        return plants
    
    def getNumPlants(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM plants")
        numUsers = cursor.fetchone()[0]
        return numUsers
    
    def close(self):
        self.conn.close()
