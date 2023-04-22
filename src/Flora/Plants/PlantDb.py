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
                picture BLOB NULL,
                desiredMoisture REAL,
                desiredPh REAL,
                desiredSalinity REAL,
                desiredLight REAL,
                desiredTemperature REAL
            )
        """)
        self.conn.commit()
    
    def fillTable(self):
        plantNames = ["Monstera Deliciosa", 
                      "Fiddle Leaf Fig", 
                      "Snake Plant", 
                      "Peace Lily", 
                      "ZZ Plant", 
                      "Pothos", 
                      "Rubber Plant", 
                      "Bird of Paradise", 
                      "Chinese Money Plant", 
                      "Calathea"]
        plantData = getRandomPlantData(len(plantNames))

        for name, data in zip(plantNames, plantData):
            plant = Plant(name, "", data)
            self.addPlant(plant)

    def addPlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO plants (name, picture, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (plant.name, plant.convertImageToBytes(), plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature))
        self.conn.commit()

    def updatePlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE plants
            SET name=?, picture=?, desiredMoisture=?, desiredPh=?, desiredSalinity=?, desiredLight=?, desiredTemperature=?
            WHERE id=?
        """, (plant.name, plant.convertImageToBytes(), plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature, plant.id))
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
        name, imageBlob, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
        image = Plant.constructImageFromBytes(imageBlob) 
        plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
        plant = Plant(name, "", plantCare)
        plant.setId(plantId)
        plant.setImage(image)
        return plant

    def getAllPlants(self) -> List[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM plants
        """)
        plants = []
        for data in cursor.fetchall():
            plantId, name, imageBlob, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
            image = Plant.constructImageFromBytes(imageBlob) 
            plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            plant = Plant(name, "", plantCare)
            plant.setId(plantId)
            plant.setImage(image)
            plants.append(plant)
        return plants
    
    def getNumPlants(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM plants")
        numUsers = cursor.fetchone()[0]
        return numUsers
    
    def close(self):
        self.conn.close()
