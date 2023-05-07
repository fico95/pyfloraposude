import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

Item {
    property bool isPotSet: potsHandler.isCurrentPotSet()
    property bool isPlantSet: potsHandler.getCurrentPotPlantExists()
    property string potName: potsHandler.getCurrentPotName()
    property string potPlantImagePath: potsHandler.getCurrentPotPlantImagePath() !== "" ? "file://" + potsHandler.getCurrentPotPlantImagePath() : ""

    signal plantClearTriggered

    function updatePotData() {
        isPlantSet = potsHandler.getCurrentPotPlantExists()
        potName = potsHandler.getCurrentPotName()
        potPlantImagePath = potsHandler.getCurrentPotPlantImagePath() !== "" ? "file://" + potsHandler.getCurrentPotPlantImagePath() : ""
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
        source: potPlantImagePath

        Rectangle {
            visible: plantIcon.source == ""
            anchors.fill: parent
            color: "lightgray"
        }

        Text {
            visible: plantIcon.source == ""
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
                    floraManager.removePlantFromCurrentPot()
                }
                else {
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
        text: potName
    }

    Connections {
        target: potsHandler
        function onCurrentPotChanged() {
            updatePotData()
        }
    }

    Component.onCompleted: {
        if (!isPotSet) {
            stackController.goBack()
        }
    }
}