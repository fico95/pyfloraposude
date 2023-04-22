from Flora.Plants.PlantData import PlantData

from PIL import Image

class Plant:
    def __init__(self, name: str, imagePath: str, plantCare: PlantData):
        self.id = None
        self.name = name
        self.image = None
        self.plantCare = plantCare

        image = Plant.constructImageFromPath(imagePath)
        if (image is not None):
            self.setImage(image)

    @staticmethod
    def constructImageFromPath(path: str):
        try:
            return Image.open(path)
        except Exception:
            print(f"Failed to load image from {path}")
            return None

    @staticmethod
    def constructImageFromBytes(bytes):
        try:
            return Image.frombytes('RGB', (300, 300), bytes)
        except Exception:
            print(f"Failed to load image from bytes")
            return None

    def convertImageToBytes(self):
        if (self.image is None):
            return None
        return self.image.tobytes('raw', 'RGB')

    def setId(self, id: int):
        self.id = id

    def setImage(self, image: Image):
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
