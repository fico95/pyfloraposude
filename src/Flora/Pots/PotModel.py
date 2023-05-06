from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex
from Flora.Pots.Pot import Pot

from typing import List

class PotModel(QAbstractListModel):

    Name = Qt.UserRole + 1
    PotId = Qt.UserRole + 2
    PlantName = Qt.UserRole + 3
    PlantImagePath = Qt.UserRole + 4
    PlantId = Qt.UserRole + 5
    Broken = Qt.UserRole + 6

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pots = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.pots)
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.pots):
            return None

        pot = self.pots[index.row()]

        if role == PotModel.Name:
            return pot.potName
        elif role == PotModel.PotId:
            return pot.id
        elif role == PotModel.PlantName:
            return None if pot.plant is None else pot.plant.name
        elif role == PotModel.PlantImagePath:
            return None if pot.plant is None else pot.plant.imagePath
        elif role == PotModel.PlantId:
            return None if pot.plant is None else pot.plant.id
        elif role == PotModel.Broken:
            return pot.isBroken

        return None
    
    def roleNames(self):
        return {
            PotModel.Name: b'name',
            PotModel.PotId: b'potId',
            PotModel.PlantName: b'plantName',
            PotModel.PlantImagePath: b'plantImagePath',
            PotModel.PlantId: b'plantId',
            PotModel.Broken: b'broken'
        }

    def updateModel(self, pots: List[Pot]):
        self.beginResetModel()
        self.pots = pots
        self.endResetModel()