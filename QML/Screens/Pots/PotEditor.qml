import QtQuick 2.14
import QtQuick.Controls 2.12
import QtCharts 2.5

import "../../Controls"

Item {
    property bool isPlantSet: potsHandler.getCurrentPotPlantExists()
    property string potPlantImagePath: potsHandler.getCurrentPotPlantImagePath() !== "" ? "file://" + potsHandler.getCurrentPotPlantImagePath() : ""

    signal plantSelectTriggered
    signal plantClearTriggered

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
            height: parent.height
            source: potPlantImagePath

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
            height: parent.height * 0.1
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
        }
    }

    Item {
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
            title: "Top-5 car brand shares in Finland"
            anchors.fill: parent
            legend.alignment: Qt.AlignBottom
            antialiasing: true

            PieSeries {
                id: pieSeries
                PieSlice { label: "Volkswagen"; value: 13.5 }
                PieSlice { label: "Toyota"; value: 10.9 }
                PieSlice { label: "Ford"; value: 8.6 }
                PieSlice { label: "Skoda"; value: 8.2 }
                PieSlice { label: "Volvo"; value: 6.8 }
            }
        }
    }

    Connections {
        target: potsHandler
        function onCurrentPotChanged() {
            isPlantSet = potsHandler.getCurrentPotPlantExists()
            potPlantImagePath = potsHandler.getCurrentPotPlantImagePath() !== "" ? "file://" + potsHandler.getCurrentPotPlantImagePath() : ""
        }
    }

    Component.onCompleted: {
        if (!potsHandler.isCurrentPotSet()) {
            stackController.goBack()
        }
        if (plantsHandler.isCurrentPlantSet() && plantsHandler.getCurrentPlantId() >= 0) {
            floraManager.addPlantToCurrentPot(plantsHandler.getCurrentPlantId())
        }
    }
}