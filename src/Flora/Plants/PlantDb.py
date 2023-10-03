from Flora.Plants.Plant import Plant
from Flora.Plants.PlantData import PlantData
from DataGenerator.PlantDataGenerator import generateRandomPlantData

import sqlite3
from typing import List

class PlantDb:
    def __init__(self, dbPath):
        self.conn = sqlite3.connect(dbPath)
        self.enableForeignKeys()

    def __del__(self):
        self.conn.close()

    def enableForeignKeys(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        self.conn.commit()

    def tableCreated(self) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='plants'
        """)
        return cursor.fetchone() is not None

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
        if (imagesPath == ""):
            return
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
        plantData = generateRandomPlantData(len(plantNames))

        for name, data in zip(plantNames, plantData):
            plant = Plant(None, name[0], name[1], data)
            self.addPlant(plant)

    def addPlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO plants (name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
            (plant.name, plant.imagePath, plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature))
        self.conn.commit()

    def updatePlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""UPDATE plants
                            SET name=?, imagePath=?, desiredMoisture=?, desiredPh=?, desiredSalinity=?, desiredLight=?, desiredTemperature=?
                            WHERE id=?""", 
                            (plant.name, plant.imagePath, plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature, plant.id))
        self.conn.commit()

    def removePlant(self, plant: Plant):
        self.removePlantById(plant.id)

    def removePlantById(self, plantId: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM plants WHERE id=?", (plantId,))
        self.conn.commit()

    def fetchPlantById(self, plantId: int) -> Plant:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM plants WHERE id=?", (plantId,))
        data = cursor.fetchone()
        if data is None:
            return None
        id, name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
        plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
        plant = Plant(id, name, imagePath, plantCare)
        return plant
    
    def randomPlant(self) -> Plant:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM plants ORDER BY RANDOM() LIMIT 1")
        data = cursor.fetchone()
        if data is None:
            return None
        id, name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
        plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
        plant = Plant(id, name, imagePath, plantCare)
        return plant

    def plants(self) -> List[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM plants")
        plants = []
        for data in cursor.fetchall():
            plantId, name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
            plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            plant = Plant(plantId, name, imagePath, plantCare)
            plants.append(plant)
        return plants
    
    def plantsDictionary(self) -> dict:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM plants")
        plants = {}
        for data in cursor.fetchall():
            plantId, name, imagePath, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
            plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            plant = Plant(plantId, name, imagePath, plantCare)
            plants[plantId] = plant
        return plants
    
    def plantsCount(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM plants")
        return cursor.fetchone()[0]