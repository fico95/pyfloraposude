import os
import shutil

from PySide2.QtCore import QObject, Slot
from PIL import Image

class ImageManager(QObject):
    def __init__(self, imagesPath, parent=None):
        super().__init__(parent)

        self.imagesPath = imagesPath
        os.makedirs(self.imagesPath, exist_ok=True)

    @Slot(str, result=str)
    def copyImage(self, imagePath):
        try:
            with Image.open(imagePath) as img:
                img.verify()

            baseName = os.path.basename(imagePath)
            destinationPath = os.path.join(self.imagesPath, baseName)
            shutil.copy2(imagePath, destinationPath)

            return destinationPath

        except Exception as e:
            print(f"Error copying image: {e}")
            return ""
