
import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    id: root

    anchors.fill: parent

    signal openPotEdit(int potId)

    FloraGridView {
        id: gridView
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
            topMargin: parent.height * 0.01
            bottom: parent.bottom
        }

        mainGrid {
            model: potModel
            delegate: Item {
                width: gridView.mainGrid.cellWidth 
                height: gridView.mainGrid.cellHeight
                PotButton {
                    anchors.fill: parent
                    anchors.margins: 10
                    potName: name
                    plantIconSource: plantImagePath !== undefined ? "file://" + plantImagePath : ""
                    mouseArea.onClicked: {
                        root.openPotEdit(potId)
                    }
                    Grid {
                        anchors {
                            right: parent.right
                            rightMargin: parent.width * 0.05
                            bottom: parent.bottom
                            bottomMargin: parent.height * 0.05
                        }
                        width: parent.width * 0.4
                        height: parent.height * 0.7
                        columns: 2
                        spacing: 5
                        Image {
                            visible: broken || !temperatureOk
                            height: parent.height / 3
                            width: parent.width / 2
                            fillMode: Image.PreserveAspectFit
                            source: "qrc:/icons/temperature.png"
                        }
                        Image {
                            visible: !soilMoistureOk
                            height: parent.height / 3
                            width: parent.width / 2
                            fillMode: Image.PreserveAspectFit
                            source: "qrc:/icons/moisture.png"
                        }
                        Image {
                            visible: broken || !phOk
                            height: parent.height / 3
                            width: parent.width / 2
                            fillMode: Image.PreserveAspectFit
                            source: "qrc:/icons/ph.png"
                        }
                        Image {
                            visible: broken || !lightLevelOk
                            height: parent.height / 3
                            width: parent.width / 2
                            fillMode: Image.PreserveAspectFit
                            source: "qrc:/icons/light.png"
                        }
                        Image {
                            visible: broken || !salinityOk
                            height: parent.height / 3
                            width: parent.width / 2
                            fillMode: Image.PreserveAspectFit
                            source: "qrc:/icons/salinity.png"
                        }

                    }
                    Rectangle {
                        anchors.fill: parent
                        anchors.margins: 5
                        color: "red"
                        opacity: 0.25
                        radius: height * 0.1
                        visible: broken
                    }
                }    
            }
        }
    }
}