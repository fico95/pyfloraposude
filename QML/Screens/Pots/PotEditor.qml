import QtQuick 2.14
import QtQuick.Controls 2.12
import QtCharts 2.5

import "../../Controls"

Item {
    property bool isPlantSet: potsHandler.getCurrentPotPlantExists()

    signal plantSelectTriggered
    signal plantClearTriggered

    function updateData() {
        isPlantSet = potsHandler.getCurrentPotPlantExists()
        plantIcon.source = potsHandler.getCurrentPotPlantImagePath() !== "" ? "file://" + potsHandler.getCurrentPotPlantImagePath() : ""
        name.text = potsHandler.getCurrentPotName()
        potAndPlantData.visible = isPlantSet

        let potBroken = potsHandler.getCurrentPotIsBroken()
        rectBroken.visible = potBroken

        temperatureData.plantValueText = potsHandler.getCurrentPotPlantTemperature()
        temperatureData.dataExists = potsHandler.sensorDataExists()
        temperatureData.sensorValueText = potsHandler.getLastSensorTemperature()
        temperatureData.potBroken = potBroken
        temperatureData.dataOk = potsHandler.getCurrentPotPlantTemperatureOk()

        soilMoistureData.plantValueText = potsHandler.getCurrentPotPlantSoilMoisture()
        soilMoistureData.dataExists = potsHandler.sensorDataExists()
        soilMoistureData.sensorValueText = potsHandler.getLastSensorSoilMoisture()
        soilMoistureData.potBroken = potBroken
        soilMoistureData.dataOk = potsHandler.getCurrentPotPlantSoilMoistureOk()

        lightLevelData.plantValueText = potsHandler.getCurrentPotPlantLightLevel()
        lightLevelData.dataExists = potsHandler.sensorDataExists()
        lightLevelData.sensorValueText = potsHandler.getLastSensorLightLevel()
        lightLevelData.potBroken = potBroken
        lightLevelData.dataOk = potsHandler.getCurrentPotPlantLightLevelOk()

        phData.plantValueText = potsHandler.getCurrentPotPlantPh()
        phData.dataExists = potsHandler.sensorDataExists()
        phData.sensorValueText = potsHandler.getLastSensorPh()
        phData.potBroken = potBroken
        phData.dataOk = potsHandler.getCurrentPotPlantPhOk()

        salinityData.plantValueText = potsHandler.getCurrentPotPlantSalinity()
        salinityData.dataExists = potsHandler.sensorDataExists()
        salinityData.sensorValueText = potsHandler.getLastSensorSalinity()
        salinityData.potBroken = potBroken
        salinityData.dataOk = potsHandler.getCurrentPotPlantSalinityOk()
    }

    function updateGraph() {
        chart.removeAllSeries()

        if (potsGraphHandler.graphType < 1 || potsGraphHandler.graphType > 3) {
            return
        }

        axisX.min = -0.5
        axisX.max = potsGraphHandler.getNumberOfSensorDataValues() + 0.5

        let gt = potsGraphHandler.graphType == 1 ? ChartView.SeriesTypeLine : potsGraphHandler.graphType == 2 ? ChartView.SeriesTypeBar : ChartView.SeriesTypeScatter
        if (potsGraphHandler.graphType == 2) {
            let series = chart.createSeries(gt, "" , axisX, axisY)
            potsGraphHandler.updateSeriesForSensorBars(series)
        }
        else {
            let numberOfSensors = potsGraphHandler.getNumberOfSensors()
            for (let i = 0; i < numberOfSensors; ++i) {
                let series = chart.createSeries(gt, "" , axisX, axisY)
                potsGraphHandler.updateSeriesForSensor(series, i)
            }
        }
    }

    Item {
        anchors {
            top: parent.top
            topMargin: parent.height * 0.1
        }
        height: parent.height * 0.35
        width: parent.width 

        Image {
            id: plantIcon
            anchors {
                left: parent.left
                top: parent.top
                bottom: parent.bottom
                leftMargin: parent.width * 0.1
            }
            width: parent.width * 0.4

            Rectangle {
                visible: plantIcon.source == ""
                anchors.fill: parent
                color: "lightgray"
            }

            Text {
                visible: !isPlantSet
                anchors.centerIn: parent
                text: "No Plant"
                height: parent.height * 0.1
                width: parent.width * 0.4
                font {
                    pixelSize: height
                    bold: true
                }
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                color: "black"
            }

            Button {
                text: isPlantSet ? "X" : "..."
                anchors {
                    top: parent.top
                    right: parent.right
                    margins: 10
                }
                width: parent.width * 0.1
                height: width
                onClicked: {
                    if (isPlantSet) {
                        plantClearTriggered()
                    }
                    else {
                        plantSelectTriggered()
                    }
                }
            }
        }

        TextEdit {
            id: name
            anchors {
                right: parent.right
                top: parent.top
                rightMargin: parent.width * 0.05
            }
            width: parent.width * 0.4
            height: parent.height * 0.2
            font {
                pixelSize: height
                bold: true
            }
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            color: "black"
            text: potsHandler.getCurrentPotName()
            onTextChanged: {
                floraManager.updateCurrentPotName(name.text)
            }

            Rectangle {
                id: rectBroken
                anchors.fill: parent
                color: "red"
                opacity: 0.5
            }
        }

        Item {
            id: potAndPlantData
            anchors {
                right: parent.right
                top: name.bottom
                bottom: parent.bottom
                topMargin: parent.height * 0.05
                rightMargin: parent.width * 0.05
                bottomMargin: parent.height * 0.05
            }
            width: parent.width * 0.4
            
            Column {
                anchors.fill: parent

                spacing: parent.height * 0.01

                PotDataInfo {
                }

                PotData {
                    id: temperatureData
                    nameText: "Temperature"
                }

                PotData {
                    id: soilMoistureData
                    nameText: "Soil Moisture"
                }

                PotData {
                    id: lightLevelData
                    nameText: "Light Level"
                }

                PotData {
                    id: phData
                    nameText: "Ph"
                }

                PotData {
                    id: salinityData
                    nameText: "Salinity"
                }
            }
        }
    }

    Item {
        id: graphItem
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
            leftMargin: parent.width * 0.1
            rightMargin: parent.width * 0.1
            bottomMargin: parent.height * 0.1
        }
        height: parent.height * 0.35

        ChartView {
            id: chart
            title: "Graph"
            anchors.fill: parent
            legend.alignment: Qt.AlignBottom
            antialiasing: true

            ValueAxis{
                id: axisX
                min: 0
                max: 1
                tickType: ValueAxis.TicksFixed
            }

            ValueAxis{
                id: axisY
                min: -10
                max: 100
            }
        }

        Row {
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
            }
            spacing: 10
            height: parent.height * 0.05
            Button {
                height: parent.height
                width: parent.width / 3 - spacing / 2
                text: "Line"
                onClicked: potsGraphHandler.setLineGraph()
            }
            Button {
                height: parent.height
                width: parent.width / 3 - spacing / 2
                text: "Bar"
                onClicked: potsGraphHandler.setBarGraph()
            }
            Button {
                height: parent.height
                width: parent.width / 3 - spacing / 2
                text: "Scatter"
                onClicked: potsGraphHandler.setScatterGraph()
            }
        }
    }

    Connections {
        target: potsHandler
        function onCurrentPotChanged() {
            updateData()
            updateGraph()
        }
    }

    Connections {
        target: potsGraphHandler
        onGraphChanged: {
            updateGraph()
        }
    }

    Component.onCompleted: {
        if (!potsHandler.isCurrentPotSet()) {
            stackController.goBack()
            return
        }
        updateGraph()
        updateData()
        if (plantsHandler.currentPlantValid() && plantsHandler.curentPlantId() >= 0) {
            floraManager.addPlantToCurrentPot(plantsHandler.curentPlantId())
        }
    }
}