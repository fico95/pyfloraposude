from Flora.Plants.PlantData import PlantData

import os

class Plant:
    def __init__(self, name: str, imagePath: str, plantCare: PlantData):
        self.id = None
        self.name = name
        self.plantCare = plantCare
        if (len(imagePath) > 0) and (not os.path.isfile(imagePath)):
            print("Invalid image path provided.")
            return
        self.imagePath = imagePath

    def setId(self, id: int):
        self.id = id