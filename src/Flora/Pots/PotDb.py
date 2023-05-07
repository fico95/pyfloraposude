from Flora.Plants.PlantData import PlantData

from Flora.Plants.Plant import Plant
from Flora.Pots.Pot import Pot

import sqlite3
from typing import List

class PotDb:
    def __init__(self, dbPath: str):
        self.conn = sqlite3.connect(dbPath)
        self.enableForeignKeys()
        self.createTable()

    def __del__(self):
        self.conn.close()

    def enableForeignKeys(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        self.conn.commit()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pots
                            (id INTEGER PRIMARY KEY,
                            potName TEXT,
                            plantId INTEGER REFERENCES plants(id) ON DELETE CASCADE,
                            sensorData TEXT NULL,
                            isBroken INTEGER DEFAULT 0)''')
        self.conn.commit()

    def fillTable(self, plant: Plant):
        if (plant is None):
            return
        
        pot = Pot(None, "Kitchen", plant.id, None, False)
        self.addPot(pot)

    def addPot(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO pots (potName, plantId, sensorData, isBroken) VALUES (?, ?, ?, ?)',
                        (pot.potName, 
                         pot.plantId, 
                         PlantData.listToJson(pot.sensorData) if pot.sensorData else None,
                         pot.isBroken))
        self.conn.commit()

    def updatePot(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE pots SET potName=?, plantId=?, sensorData=?, isBroken=? WHERE id=?',
                    (pot.potName, 
                     pot.plant.id if pot.plant else None, 
                     PlantData.listToJson(pot.sensorData) if pot.sensorData else None,
                     pot.isBroken, 
                     pot.id))
        self.conn.commit()

    def updatePotName(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE pots SET potName=? WHERE id=?',
                    (pot.potName, pot.id))
        self.conn.commit()

    def updatePotSensorDataAndBroken(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE pots SET sensorData=?, isBroken=? WHERE id=?',
                    (PlantData.listToJson(pot.sensorData) if pot.sensorData else None,
                     pot.isBroken, 
                     pot.id))
        self.conn.commit()

    def removePlantFromPot(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE pots SET plantId=?, sensorData=?, isBroken=? WHERE id=?',
                    (None, None, False, pot.id))
        self.conn.commit()

    def removePot(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM pots WHERE id=?', (pot.id,))
        self.conn.commit()

    def removePotById(self, potId: int):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM pots WHERE id=?', (potId,))
        self.conn.commit()

    def getPotById(self, potId: int) -> Pot:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pots WHERE id=?', (potId,))
        row = cursor.fetchone()
        if row is None:
            return None
        potId, potName, plantId, sensorDataJson, isBroken = row
        sensorData = PlantData.listFromJson(sensorDataJson) if sensorDataJson else None
        pot = Pot(potId, potName, plantId, sensorData, isBroken)
        return pot

    def getAllPots(self) -> List[Pot]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pots')
        pots = []
        for row in cursor.fetchall():
            potId, potName, plantId, sensorDataJson, isBroken = row
            sensorData = PlantData.listFromJson(sensorDataJson) if sensorDataJson else None
            pot = Pot(potId, potName, plantId, sensorData, isBroken)
            pots.append(pot)
        return pots
    
    def getAllPotsWithoutPlants(self) -> List[Pot]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pots WHERE plantId IS NULL')
        pots = []
        for row in cursor.fetchall():
            potId, potName, plantId, sensorDataJson, isBroken = row
            sensorData = PlantData.listFromJson(sensorDataJson) if sensorDataJson else None
            pot = Pot(potId, potName, plantId, sensorData, isBroken)
            pots.append(pot)
        return pots

    def getNumPots(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM pots')
        return cursor.fetchone()[0]