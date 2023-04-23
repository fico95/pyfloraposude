import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

Item {
    signal imageLoadTriggered
    signal plantAdded

    function handleFileDialogClose(filePath) {
        plantIcon.source = filePath
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
        source: ""

        Rectangle {
            visible: plantIcon.source == ""
            anchors.fill: parent
            color: "lightgray"
        }

        Text {
            visible: plantIcon.source == ""
            anchors.centerIn: parent
            text: "No image"
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
            text: "..."
            anchors {
                top: parent.top
                right: parent.right
                margins: 10
            }
            width: parent.width * 0.1
            height: width
            onClicked: {
                imageLoadTriggered()
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
        text: "Plant name"
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
                value: (to - from) / 2
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
                value: (to - from) / 2
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
                value: (to - from) / 2
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
                value: (to - from) / 2
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
                value: (to - from) / 2
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
        onClicked: {
            let filePath = plantIcon.source.toString()
            filePath = filePath.replace("file://", "")
            if (filePath !== "") {
                filePath = imageManager.copyImage(filePath)
                if (filePath === "") {
                    return
                }
            }
            if (plantsHandler.addPlant(name.text, filePath, spinBoxSoilMoisture.value, spinBoxPh.value, spinBoxSalinity.value, spinBoxLightLevel.value, spinBoxTemperature.value)) {
                plantAdded()
            }
        }
    }
}