from plant import Plant
from plantdata import PlantData

import sqlite3
from typing import List, Optional
from PIL import Image

class PlantDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                picture BLOB,
                desired_moisture REAL,
                desired_ph REAL,
                desired_salinity REAL,
                desired_light REAL,
                desired_temperature REAL
            )
        """)
        self.conn.commit()

    def add_plant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO plants (name, picture, desired_moisture, desired_ph, desired_salinity, desired_light, desired_temperature)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (plant.name, plant.photo.tobytes(), plant.plant_care.soil_moisture, plant.plant_care.ph, plant.plant_care.salinity, plant.plant_care.light_level, plant.plant_care.temperature))
        self.conn.commit()

    def update_plant(self, plant: Plant):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE plants
            SET name=?, picture=?, desired_moisture=?, desired_ph=?, desired_salinity=?, desired_light=?, desired_temperature=?
            WHERE id=?
        """, (plant.name, plant.photo.tobytes(), plant.plant_care.soil_moisture, plant.plant_care.ph, plant.plant_care.salinity, plant.plant_care.light_level, plant.plant_care.temperature, plant.id))
        self.conn.commit()

    def remove_plant(self, plant_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            DELETE FROM plants
            WHERE id=?
        """, (plant_id,))
        self.conn.commit()

    def get_plant_by_id(self, plant_id) -> Optional[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM plants WHERE id=?
        """, (plant_id,))
        data = cursor.fetchone()
        if data is None:
            return None
        name, photo_blob, desired_moisture, desired_ph, desired_salinity, desired_light, desired_temperature = data
        photo = Image.frombytes('RGB', (300,300), photo_blob)
        plant_care = PlantData(desired_moisture, desired_ph, desired_salinity, desired_light, desired_temperature)
        return Plant(id=plant_id, name=name, photo=photo, plant_care=plant_care)

    def get_all_plants(self) -> List[Plant]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM plants
        """)
        plants = []
        for data in cursor.fetchall():
            plant_id, name, photo_blob, desired_moisture, desired_ph, desired_salinity, desired_light, desired_temperature = data
            photo = Image.frombytes('RGB', (300,300), photo_blob)
            plant_care = PlantData(desired_moisture, desired_ph, desired_salinity, desired_light, desired_temperature)
            plants.append(Plant(id=plant_id, name=name, photo=photo, plant_care=plant_care))
        return plants

    def close(self):
        self.conn.close()
