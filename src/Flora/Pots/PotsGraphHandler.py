from PySide2.QtCore import QObject, Signal, Slot, Property
from PySide2.QtCharts import QtCharts

from Flora.Plants.Plant import PlantData
from Utils.Enums import Enums

from typing import List

class PotsGraphHandler(QObject):

    graphChanged = Signal()

    @Property(int, notify=graphChanged)
    def graphType(self):
        return self.selectedGraphType

    def __init__(self, parent=None):
        super().__init__(parent)

        self.sensorData = None
        self.selectedGraphType = Enums.GraphType.Line

    def resetGraph(self):
        self.sensorData = None
        self.selectedGraphType = Enums.GraphType.Line
        self.graphChanged.emit()        

    def sensorDataValid(self) -> bool:
        return self.sensorData is not None

    def setSensorData(self, sensorData: List[PlantData]):
        self.sensorData = sensorData
        self.setLineGraph()

    @Slot()
    def setLineGraph(self):
        self.selectedGraphType = Enums.GraphType.Line
        self.graphChanged.emit()

    @Slot()
    def setBarGraph(self):
        self.selectedGraphType = Enums.GraphType.Bar
        self.graphChanged.emit()

    @Slot()
    def setScatterGraph(self):
        self.selectedGraphType = Enums.GraphType.Scatter
        self.graphChanged.emit()

    @Slot(result=int)
    def numberOfSensors(self) -> int:
        return PlantData.propertiesCount()
    
    @Slot(result=int)
    def sensorDataCount(self) -> int:
        if (self.sensorDataValid):
            return len(self.sensorData)
        return 0
    
    @Slot(QtCharts.QAbstractSeries, int)
    def updateGraphSeries(self, series: QtCharts.QAbstractSeries, sensorIndex: int):
        series.clear()
        if (self.sensorData is None):
            return None
        if (sensorIndex > (self.numberOfSensors() - 1) or sensorIndex < 0):
            return None
        if (sensorIndex == 0):
            series.setName("Temperature")
            for i in range(len(self.sensorData)):
                series.append(i, self.sensorData[i].temperature)
        elif (sensorIndex == 1):
            series.setName("Salinity")
            for i in range(len(self.sensorData)):
                series.append(i, self.sensorData[i].salinity)
        elif (sensorIndex == 2):
            series.setName("Light level")
            for i in range(len(self.sensorData)):
                series.append(i, self.sensorData[i].lightLevel)
        elif (sensorIndex == 3):
            series.setName("Soil moisture")
            for i in range(len(self.sensorData)):
                series.append(i, self.sensorData[i].soilMoisture)
        elif (sensorIndex == 4):
            series.setName("Ph")
            for i in range(len(self.sensorData)):
                series.append(i, self.sensorData[i].ph)

    @Slot(QtCharts.QAbstractBarSeries)
    def updateGraphBarSeries(self, series: QtCharts.QAbstractBarSeries):
        series.clear()
        if (not self.sensorDataValid()):
            return None
        barSetTemperature = QtCharts.QBarSet("Temperature")
        barSetSalinity = QtCharts.QBarSet("Salinity")
        barSetLight = QtCharts.QBarSet("Light level")
        barSetSoil = QtCharts.QBarSet("Soil moisture")
        barSetPh = QtCharts.QBarSet("Ph")
        for data in self.sensorData:
            barSetTemperature.append(data.temperature)
            barSetSalinity.append(data.salinity)
            barSetLight.append(data.lightLevel)
            barSetSoil.append(data.soilMoisture)
            barSetPh.append(data.ph)
        series.append(barSetTemperature)
        series.append(barSetSalinity)
        series.append(barSetLight)
        series.append(barSetSoil)
        series.append(barSetPh)