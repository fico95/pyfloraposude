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
            # Open the image file and validate it
            with Image.open(imagePath) as img:
                img.verify()

            # Construct the destination path and copy the image file
            baseName = os.path.basename(imagePath)
            destinationPath = os.path.join(self.imagesPath, baseName)
            shutil.copy2(imagePath, destinationPath)


            # Return the destination path
            return destinationPath

        except Exception as e:
            # If the image is not valid or cannot be opened, return an empty string
            print(f"Error copying image: {e}")
            return ''
