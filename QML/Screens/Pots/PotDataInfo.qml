import QtQuick 2.14

import "../../Controls"

Row {
    width: parent.width
    height: parent.height / 5 - spacing / 4

    CustomText {
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height
        textBold: true
        text: "Data"
    }

    CustomText {
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height
        textBold: true
        text: "Plant"
    }

    CustomText {
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height
        textBold: true
        text: "Sensor"
    }

    CustomText {
        anchors.horizontalCenter: undefined
        width: parent.width / 4
        height: parent.height
        textBold: true
        text: "Action"
    }
}