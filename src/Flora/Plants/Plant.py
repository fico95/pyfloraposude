from Flora.Plants.PlantData import PlantData

import os

class Plant:
    def __init__(self, id: int, name: str, imagePath: str, plantCare: PlantData):
        self.id = id
        self.name = name
        self.plantCare = plantCare
        self.imagePath = ""
        if ((len(imagePath) > 0) and (os.path.isfile(imagePath))):
            self.imagePath = imagePath