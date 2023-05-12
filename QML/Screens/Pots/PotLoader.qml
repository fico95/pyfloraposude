import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

Item {
    property bool isPlantSet: plantsHandler.currentPlantValid()
    property string plantImagePath: plantsHandler.currentPlantImagePath() === "" ?  "" : "file://" + plantsHandler.currentPlantImagePath()

    signal plantSelectTriggered
    signal plantClearTriggered
    signal potLoaded

    function updatePlantData() {
        isPlantSet = plantsHandler.currentPlantValid()
        plantImagePath = plantsHandler.currentPlantImagePath() === "" ?  "" : "file://" + plantsHandler.currentPlantImagePath()
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
        source: plantImagePath

        Rectangle {
            visible: plantIcon.source === ""
            anchors.fill: parent
            color: "lightgray"
        }

        Text {
            visible: plantIcon.source === ""
            anchors.centerIn: parent
            text: "No plant"
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
        text: "Pot name"
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
            if (floraManager.addPot(name.text, plantsHandler.curentPlantId())) {
                potLoaded()
            }
        }
    }

    Connections {
        target: plantsHandler
        function onCurrentPlantChanged() {
            updatePlantData()
        }
    }
}