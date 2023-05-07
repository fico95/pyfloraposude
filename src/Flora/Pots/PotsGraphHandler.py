from PySide2.QtCore import QObject, Signal, Slot, Property
from PySide2.QtCharts import QtCharts

from Flora.Plants.Plant import PlantData

from enum import IntEnum
from typing import List
import random

class PotsGraphHandler(QObject):

    graphChanged = Signal()

    @Property(int, notify=graphChanged)
    def graphType(self):
        return self.selectedGraph

    class GraphType(IntEnum):
        Unknown, \
        Line, \
        Bar, \
        Scatter = range(4)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.sensorData = None

    def resetGraph(self):
        self.sensorData = None
        self.selectedGraph = PotsGraphHandler.GraphType.Unknown
        self.graphChanged.emit()        

    def setSensorData(self, sensorData: List[PlantData]):
        self.sensorData = sensorData

    @Slot()
    def setLineGraph(self):
        self.selectedGraph = PotsGraphHandler.GraphType.Line
        self.graphChanged.emit()

    @Slot()
    def setBarGraph(self):
        self.selectedGraph = PotsGraphHandler.GraphType.Bar
        self.graphChanged.emit()

    @Slot()
    def setScatterGraph(self):
        self.selectedGraph = PotsGraphHandler.GraphType.Scatter
        self.graphChanged.emit()

    @Slot(result=int)
    def getNumberOfSensors(self):
        return 5
    
    @Slot(result=int)
    def getNumberOfSensorDataValues(self):
        if (self.sensorData is None):
            return 0
        return len(self.sensorData) - 1
    
    @Slot(QtCharts.QAbstractSeries, int)
    def updateSeriesForSensor(self, series: QtCharts.QAbstractSeries, sensorIndex: int):
        series.clear()
        if (sensorIndex >= self.getNumberOfSensors() or sensorIndex < 0):
            return None
        if (self.sensorData is None):
            return None
        if (sensorIndex == 0):
            series.setName("Temperature")
            for k in range(len(self.sensorData)):
                print(self.sensorData[k].temperature)
                series.append(k, self.sensorData[k].temperature)
        elif (sensorIndex == 1):
            series.setName("Salinity")
            for k in range(len(self.sensorData)):
                series.append(k, self.sensorData[k].salinity)
        elif (sensorIndex == 2):
            series.setName("Light level")
            for k in range(len(self.sensorData)):
                series.append(k, self.sensorData[k].lightLevel)
        elif (sensorIndex == 3):
            series.setName("Soil moisture")
            for k in range(len(self.sensorData)):
                series.append(k, self.sensorData[k].soilMoisture)
        elif (sensorIndex == 4):
            series.setName("Ph")
            for k in range(len(self.sensorData)):
                series.append(k, self.sensorData[k].ph)

    @Slot(QtCharts.QAbstractBarSeries)
    def updateSeriesForSensorBars(self, series):
        series.clear()
        if (self.sensorData is None):
            return None
        barSetTemperature = QtCharts.QBarSet("Temperature")
        barSetSalinity = QtCharts.QBarSet("Salinity")
        barSetLight = QtCharts.QBarSet("Light level")
        barSetSoil = QtCharts.QBarSet("Soil moisture")
        barSetPh = QtCharts.QBarSet("Ph")
        for i in range(len(self.sensorData)):
            barSetTemperature.append(self.sensorData[i].temperature)
            barSetSalinity.append(self.sensorData[i].salinity)
            barSetLight.append(self.sensorData[i].lightLevel)
            barSetSoil.append(self.sensorData[i].soilMoisture)
            barSetPh.append(self.sensorData[i].ph)
        series.append(barSetTemperature)
        series.append(barSetSalinity)
        series.append(barSetLight)
        series.append(barSetSoil)
        series.append(barSetPh)