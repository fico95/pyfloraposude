import QtQuick 2.14
import QtQuick.Controls 2.15

Item {
    id: root

    property string name: ""
    property int potId: -1
    property string plantImagePath: ""
    property bool broken: false
    property bool temperatureOk: true
    property bool soilMoistureOk: true
    property bool phOk: true
    property bool lightLevelOk: true
    property bool salinityOk: true

    signal buttonClicked(int potId)

    width: parent.width
    height: parent.height

    ListModel {
        id: iconsModel
        ListElement {
            shown: function() {
                return broken || !temperatureOk
            }
            imgSource: "qrc:/icons/temperature.png"
        }
        ListElement {
            shown: function() {
                return broken ||!soilMoistureOk
            }
            imgSource: "qrc:/icons/moisture.png"
        }
        ListElement {
            shown: function() {
                return broken || !phOk
            }
            imgSource: "qrc:/icons/ph.png"
        }
        ListElement {
            shown: function() {
                return broken || !lightLevelOk
            }
            imgSource: "qrc:/icons/light.png"
        }
        ListElement {
            shown: function() {
                return broken || !salinityOk
            }
            imgSource: "qrc:/icons/salinity.png"
        }
    }

    GridButton {
        anchors.fill: parent
        anchors.margins: 10
        nameText: name
        iconSource: plantImagePath !== "" ? "file:///" + plantImagePath : ""
        mouseArea.onClicked: {
            root.buttonClicked(potId)
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

            Repeater {
                model: iconsModel
                delegate: Item {
                    width: parent.width / 2
                    height: parent.height / 3
                    Rectangle {
                        id: rect
                        anchors.centerIn: parent
                        width: parent.width * 0.8
                        height: parent.height * 0.8
                        radius: height * 0.1
                        Component.onCompleted: {
                            color = Qt.binding(() => { return model.shown() ? "red" : "green" })
                        }
                    }
                    Image {
                        anchors.fill: parent
                        fillMode: Image.PreserveAspectFit
                        source: model.imgSource
                    }
                }
            }
        }
        Rectangle {
            anchors.fill: parent
            anchors.margins: 1
            color: "red"
            opacity: 0.5
            radius: height * 0.1
            visible: broken
        }
    }    
}