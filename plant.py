import plantdata as PlantData

from PIL import Image

class Plant:
    def __init__(self, id: int, name: str, photo_path: str, plant_care: PlantData):
        self.id = id
        self.name = name
        self.photo = self._load_image(photo_path)
        self.plant_care = plant_care

    def _load_image(self, path: str) -> Image:
        try:
            return Image.open(path)
        except IOError:
            print(f"Failed to load image from {path}")
            return None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "photo_path": self.photo_path,
            "plant_care": self.plant_care.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        id = data["id"]
        name = data["name"]
        photo_path = data["photo_path"]
        plant_care = PlantData.from_dict(data["plant_care"])
        return cls(id=id, name=name, photo_path=photo_path, plant_care=plant_care)
