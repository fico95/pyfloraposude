import QtQuick 2.14

import "../../Controls"

Row {
    property alias nameText: nameText.text
    property alias plantValueText: plantValueText.text
    property alias sensorValueText: sensorValueText.text
    property bool dataExists: false
    property bool potBroken: false
    property bool dataOk: false

    width: parent.width
    height: parent.height / 5 - spacing / 4

    CustomText {
        id: nameText
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height
    }

    CustomText {
        id: plantValueText
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height 
    }

    CustomText {
        id: sensorValueText
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height
    }
    
    Rectangle {
        visible: dataExists
        anchors.verticalCenter: parent.verticalCenter
        width: parent.width / 4
        height: parent.height
        color: dataOk && !potBroken ? "green" : "red"
        Image {
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            source: potBroken ? "qrc:/icons/broken.png" : dataOk ? "qrc:/icons/ok.png" : "qrc:/icons/not_ok.png"
        }
    }
}