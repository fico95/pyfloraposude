import QtQuick 2.14

Row {
    property alias nameText: nameText.text
    property alias plantValueText: plantValueText.text
    property alias sensorValueText: sensorValueText.text
    property bool dataExists: false
    property bool potBroken: false
    property bool dataOk: false

    width: parent.width
    height: parent.height / 5 - spacing / 4

    Text {
        id: nameText
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
        }
        fontSizeMode: Text.Fit
    }

    Text {
        id: plantValueText
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
        }
        fontSizeMode: Text.Fit
    }

    Text {
        id: sensorValueText
        visible: dataExists
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
        }
        fontSizeMode: Text.Fit
    }
    
    Rectangle {
        visible: dataExists
        anchors.verticalCenter: parent.verticalCenter
        width: parent.width / 4
        height: parent.height
        color: dataOk && !potBroken ? "lightgreen" : "red"
        Image {
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            source: potBroken ? "qrc:/icons/broken.png" : dataOk ? "qrc:/icons/ok.png" : "qrc:/icons/not_ok.png"
        }
    }
}