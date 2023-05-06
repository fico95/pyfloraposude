import sqlite3
from Flora.Plants.Plant import Plant
from Flora.Plants.PlantDb import PlantDb
from Flora.Plants.PlantData import PlantData
from Flora.Pots.Pot import Pot

class PotDb:
    def __init__(self, dbPath):
        self.conn = sqlite3.connect(dbPath)
        self.create_table()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pots
                            (id INTEGER PRIMARY KEY,
                            potName TEXT,
                            plantId INTEGER REFERENCES plants(id) ON DELETE CASCADE,
                            sensorData BLOB,
                            isBroken INTEGER DEFAULT 0)''')
        self.conn.commit()

    def addPot(self, pot: Pot):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO pots (potName, plantId, sensorData, isBroken) VALUES (?, ?, ?, ?)',
                        (pot.potName, 
                         pot.plant.id if pot.plant is not None else None, 
                         sqlite3.Binary(pot.sensorData),
                         pot.isBroken))
        self.conn.commit()

    def updatePot(self, pot):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE pots SET potName=?, plantId=?, sensorData=?, isBroken=? WHERE id=?',
                    (pot.potName, 
                     pot.plant.id if pot.plant else None, 
                     None, 
                     pot.isBroken, 
                     pot.id))
        self.conn.commit()

    def removePot(self, pot):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM pots WHERE id=?', (pot.id,))
        self.conn.commit()
