import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

Item {
    property string initialPlantName: plantsHandler.getCurrentPlantName()
    property string initialPlantImagePath: "file://" + plantsHandler.getCurrentPlantImagePath()
    property real initialDesiredSoilMoisture: plantsHandler.getCurrentPlantDesiredSoilMoisture()
    property real initialDesiredPh: plantsHandler.getCurrentPlantDesiredPh()
    property real initialDesiredSalinity: plantsHandler.getCurrentPlantDesiredSalinity()
    property real initialDesiredLightLevel: plantsHandler.getCurrentPlantDesiredLightLevel()
    property real initialDesiredTemperature: plantsHandler.getCurrentPlantDesiredTemperature()

    readonly property bool plantDataModified: initialPlantName !== name.text || 
                                             initialDesiredSoilMoisture !== spinBoxSoilMoisture.value ||
                                             initialDesiredPh !== spinBoxPh.value ||
                                             initialDesiredSalinity !== spinBoxSalinity.value ||
                                             initialDesiredLightLevel !== spinBoxLightLevel.value ||
                                             initialDesiredTemperature !== spinBoxTemperature.value
                                             
    signal imageChangeTriggered

    function updateInitialDesiredPlantData() {
        initialPlantName = plantsHandler.getCurrentPlantName()
        initialPlantImagePath = "file://" + plantsHandler.getCurrentPlantImagePath()
        initialDesiredSoilMoisture = plantsHandler.getCurrentPlantDesiredSoilMoisture()
        initialDesiredPh = plantsHandler.getCurrentPlantDesiredPh()
        initialDesiredSalinity = plantsHandler.getCurrentPlantDesiredSalinity()
        initialDesiredLightLevel = plantsHandler.getCurrentPlantDesiredLightLevel()
        initialDesiredTemperature = plantsHandler.getCurrentPlantDesiredTemperature()

        name.text = initialPlantName
        plantIcon.source = initialPlantImagePath
        spinBoxSoilMoisture.value = initialDesiredSoilMoisture
        spinBoxPh.value = initialDesiredPh
        spinBoxSalinity.value = initialDesiredSalinity
        spinBoxLightLevel.value = initialDesiredLightLevel
        spinBoxTemperature.value = initialDesiredTemperature
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
    }

    Column {
        anchors {
            right: parent.right
            top: name.bottom
            rightMargin: parent.width * 0.05
            topMargin: parent.height * 0.1        
            bottom: saveButton.top
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
            }
        }
    }

    Button {
        id: saveButton
        anchors {
            bottom: parent.bottom
            bottomMargin: parent.height * 0.1
            right: parent.right
            rightMargin: parent.width * 0.05
        }
        width: parent.width * 0.4
        height: parent.height * 0.05
        text: "Save"
        enabled: plantDataModified
        onClicked: {
            plantsHandler.updateCurrentPlant(name.text, spinBoxSoilMoisture.value, spinBoxPh.value, spinBoxSalinity.value, spinBoxLightLevel.value, spinBoxTemperature.value)
            //updateInitialDesiredPlantData()
        }
    }

    Connections {
        target: plantsHandler
        function onCurrentPlantChanged() {
            updateInitialDesiredPlantData()
        }
    }

    Component.onDestruction: {
        plantsHandler.resetCurrentPlant()
    }
}