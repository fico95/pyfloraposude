from Plants.Plant import Plant
from Plants.PlantData import PlantData

import sqlite3
from typing import List, Optional
from PIL import Image

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
                picture BLOB,
                desiredMoisture REAL,
                desiredPh REAL,
                desiredSalinity REAL,
                desiredLight REAL,
                desiredTemperature REAL
            )
        """)
        self.conn.commit()

    def addPlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO plants (name, picture, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (plant.name, plant.photo.tobytes(), plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature))
        self.conn.commit()

    def updatePlant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE plants
            SET name=?, picture=?, desiredMoisture=?, desiredPh=?, desiredSalinity=?, desiredLight=?, desiredTemperature=?
            WHERE id=?
        """, (plant.name, plant.photo.tobytes(), plant.plantCare.soilMoisture, plant.plantCare.ph, plant.plantCare.salinity, plant.plantCare.lightLevel, plant.plantCare.temperature, plant.id))
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
        name, photoBlob, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
        photo = Image.frombytes('RGB', (300,300), photoBlob)
        plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
        return {"id": plantId, "name": name, "photo": photo, "plantCare": plantCare}

    def getAllPlants(self) -> List[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM plants
        """)
        plants = []
        for data in cursor.fetchall():
            plantId, name, photoBlob, desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature = data
            photo = Image.frombytes('RGB', (300,300), photoBlob)
            plantCare = PlantData(desiredMoisture, desiredPh, desiredSalinity, desiredLight, desiredTemperature)
            plants.append({"id": plantId, "name": name, "photo": photo, "plantCare": plantCare})
        return plants

    def close(self):
        self.conn.close()
