from Plants.PlantData import PlantData

from PIL import Image

class Plant:
    def __init__(self, id: int, name: str, imagePath: str, plantCare: PlantData):
        self.id = id
        self.name = name
        self.plantCare = plantCare
        self.updateImageByPath(imagePath)

    def updateImageByPath(self, path: str):
        try:
            self.updateImage(Image.open(path))
        except IOError:
            print(f"Failed to load image from {path}")

    def updateImage(self, image: Image):
        self.image = image

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "plantCare": self.plantCare.toDict()
        }

    @classmethod
    def fromDict(cls, data):
        id = data["id"]
        name = data["name"]
        image = data["image"]
        plantCare = PlantData.fromDict(data["plantCare"])
        cls = cls(id, name, "", plantCare)
        cls.updateImage(image)
        return cls
