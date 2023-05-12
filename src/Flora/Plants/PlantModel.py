from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex
from Flora.Plants.Plant import Plant

from typing import List

class PlantModel(QAbstractListModel):

    Name = Qt.UserRole + 1
    Id = Qt.UserRole + 2
    ImagePath = Qt.UserRole + 3

    def __init__(self, parent=None):
        super().__init__(parent)

        self.plants = []
    
    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.plants)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.plants):
            return None

        plant = self.plants[index.row()]

        if role == PlantModel.Name:
            return plant.name
        elif role == PlantModel.Id:
            return plant.id
        elif role == PlantModel.ImagePath:
            return plant.imagePath
        
        return None

    def roleNames(self):
        return {
            PlantModel.Name: b'name',
            PlantModel.Id: b'id',
            PlantModel.ImagePath: b'imagePath'
        }
    
    def updateModel(self, plants: List[Plant]):
        self.beginResetModel()
        self.plants = plants
        self.endResetModel()