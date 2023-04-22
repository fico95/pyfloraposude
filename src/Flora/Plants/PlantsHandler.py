from PySide2.QtCore import QAbstractListModel, QObject, Qt, QModelIndex

from Flora.Plants.PlantDb import PlantDb

class PlantsHandler(QAbstractListModel):
    Name = Qt.UserRole + 1
    ImagePath = Qt.UserRole + 2

    def __init__(self, dbPath, imagesPath, parent=None):
        super().__init__(parent)
        self.plantDb = PlantDb(dbPath)
        if (self.plantDb.getNumPlants() == 0):
            self.plantDb.fillTable(imagesPath)
        self._plants = self.plantDb.getAllPlants()

    def rowCount(self, parent=QModelIndex()):
        return len(self._plants)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self._plants):
            return None

        plant = self._plants[index.row()]

        if role == PlantsHandler.Name:
            return plant.name

        if role == PlantsHandler.ImagePath:
            return plant.imagePath
        
        return None

    def roleNames(self):
        return {
            PlantsHandler.Name: b'name',
            PlantsHandler.ImagePath: b'imagePath'
        }