from PySide2.QtCore import QObject

from Flora.Plants.PlantDb import PlantDb

class PlantsHandler(QObject):
    def __init__(self, dbPath, parent=None):
        super().__init__(parent)

        self.plantDb = PlantDb(dbPath)
        if (self.plantDb.getNumPlants() == 0):
            self.plantDb.fillTable()
