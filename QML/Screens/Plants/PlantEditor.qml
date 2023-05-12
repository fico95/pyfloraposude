import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

Item {
    property string initialPlantName: plantsHandler.currentPlantName()
    property string initialPlantImagePath: "file://" + plantsHandler.currentPlantImagePath()
    property real initialDesiredSoilMoisture: plantsHandler.currentPlantDesiredSoilMoisture()
    property real initialDesiredPh: plantsHandler.currentPlantDesiredPh()
    property real initialDesiredSalinity: plantsHandler.currentPlantDesiredSalinity()
    property real initialDesiredLightLevel: plantsHandler.currentPlantDesiredLightLevel()
    property real initialDesiredTemperature: plantsHandler.currentPlantDesiredTemperature()

    readonly property bool plantDataModified: initialPlantName !== name.text || 
                                             initialDesiredSoilMoisture !== spinBoxSoilMoisture.value ||
                                             initialDesiredPh !== spinBoxPh.value ||
                                             initialDesiredSalinity !== spinBoxSalinity.value ||
                                             initialDesiredLightLevel !== spinBoxLightLevel.value ||
                                             initialDesiredTemperature !== spinBoxTemperature.value
                                             
    signal imageChangeTriggered

    function updateCurrentPlantData() {
        floraManager.updateCurrentPlantData(name.text, spinBoxSoilMoisture.value, spinBoxPh.value, spinBoxSalinity.value, spinBoxLightLevel.value, spinBoxTemperature.value)
    }

    function updateInitialDesiredPlantData() {
        initialPlantName = plantsHandler.currentPlantName()
        initialPlantImagePath = "file://" + plantsHandler.currentPlantImagePath()
        initialDesiredSoilMoisture = plantsHandler.currentPlantDesiredSoilMoisture()
        initialDesiredPh = plantsHandler.currentPlantDesiredPh()
        initialDesiredSalinity = plantsHandler.currentPlantDesiredSalinity()
        initialDesiredLightLevel = plantsHandler.currentPlantDesiredLightLevel()
        initialDesiredTemperature = plantsHandler.currentPlantDesiredTemperature()

        name.text = initialPlantName
        plantIcon.source = initialPlantImagePath
        spinBoxSoilMoisture.value = initialDesiredSoilMoisture
        spinBoxPh.value = initialDesiredPh
        spinBoxSalinity.value = initialDesiredSalinity
        spinBoxLightLevel.value = initialDesiredLightLevel
        spinBoxTemperature.value = initialDesiredTemperature
    }

    function handleFileDialogClose(filePath) {
        filePath = filePath.replace("file://", "")
        let destinationPath = imageManager.copyImage(filePath)
        if (destinationPath !== "") {
            floraManager.updateCurrentPlantImage(destinationPath)
        }
    }

    Image {
        id: plantIcon
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
            leftMargin: parent.width * 0.1
            topMargin: parent.height * 0.1
            bottomMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        height: parent.height * 0.8
        source: initialPlantImagePath

        Button {
            text: "..."
            anchors {
                top: parent.top
                right: parent.right
                margins: 10
            }
            width: parent.width * 0.1
            height: width
            onClicked: {
                imageChangeTriggered()
            }
        }
    }

    TextEdit {
        id: name
        anchors {
            right: parent.right
            top: parent.top
            rightMargin: parent.width * 0.05
            topMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        height: parent.height * 0.1
        font {
            pixelSize: height
            bold: true
        }
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignTop
        color: "black"
        text: initialPlantName
        onTextChanged: updateCurrentPlantData()
    }

    Column {
        anchors {
            right: parent.right
            top: name.bottom
            rightMargin: parent.width * 0.05
            topMargin: parent.height * 0.1        
            bottom: parent.bottom
            bottomMargin: parent.height * 0.1
        }
        width: parent.width * 0.4

        spacing: parent.height * 0.05

        Item {
            height: parent.height * 0.05
            width: parent.width
            Text {
                anchors.left: parent.left
                text: "Soil moisture [0-100]%"
            }
            DoubleSpinBox {
                id: spinBoxSoilMoisture
                width: parent.width / 3
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                from: 0
                to: 100
                decimals: 1
                wrap: false
                suffix: " %"
                value: initialDesiredSoilMoisture
                onValueChanged: updateCurrentPlantData()
            }
        }

        Item {
            height: parent.height * 0.05
            width: parent.width
            Text {
                anchors.left: parent.left
                text: "PH [0-14]"
            }
            DoubleSpinBox {
                id: spinBoxPh
                width: parent.width / 3
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                from: 0
                to: 14
                decimals: 1
                wrap: false
                value: initialDesiredPh
                onValueChanged: updateCurrentPlantData()
            }
        }

        Item {
            height: parent.height * 0.05
            width: parent.width
            Text {
                anchors.left: parent.left
                text: "Salinity [0-100]%"
            }
            DoubleSpinBox {
                id: spinBoxSalinity
                width: parent.width / 3
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                from: 0
                to: 100
                decimals: 1
                wrap: false
                suffix: " %"
                value: initialDesiredSalinity
                onValueChanged: updateCurrentPlantData()
            }
        }

        Item {
            height: parent.height * 0.05
            width: parent.width
            Text {
                anchors.left: parent.left
                text: "Light level [0-100]%"
            }
            DoubleSpinBox {
                id: spinBoxLightLevel
                width: parent.width / 3
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                from: 0
                to: 100
                decimals: 1
                wrap: false
                suffix: " %"
                value: initialDesiredLightLevel
                onValueChanged: updateCurrentPlantData()
            }
        }

        Item {
            height: parent.height * 0.05
            width: parent.width
            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                text: "Temperature [-10,40]°C"
            }
            DoubleSpinBox {
                id: spinBoxTemperature
                width: parent.width / 3
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                from: -10
                to: 40
                decimals: 1
                wrap: false
                suffix: " °C"
                value: initialDesiredTemperature
                onValueChanged: updateCurrentPlantData()
            }
        }
    }

    Connections {
        target: plantsHandler
        function onCurrentPlantChanged() {
            updateInitialDesiredPlantData()
        }
    }
}