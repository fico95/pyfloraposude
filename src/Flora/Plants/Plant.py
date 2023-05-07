from Flora.Plants.PlantData import PlantData

import os

class Plant:
    def __init__(self, id: int, name: str, imagePath: str, plantCare: PlantData):
        self.id = id
        self.name = name
        self.plantCare = plantCare
        if ((len(imagePath) == 0) or (not os.path.isfile(imagePath))):
            print("Invalid image path provided.")
            self.imagePath = ""
            return
        self.imagePath = imagePath