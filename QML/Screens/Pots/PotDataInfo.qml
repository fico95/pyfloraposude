import QtQuick 2.14

Row {
    width: parent.width
    height: parent.height / 5 - spacing / 4

    Text {
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
            bold: true
        }
        text: "Data"
        fontSizeMode: Text.Fit
    }

    Text {
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
            bold: true
        }
        text: "Plant"
        fontSizeMode: Text.Fit
    }

    Text {
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
            bold: true
        }
        text: "Sensor"
        fontSizeMode: Text.Fit
    }

    Text {
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        width: parent.width / 4
        height: parent.height
        font {
            pixelSize: height / 2
            bold: true
        }
        text: "Action"
        fontSizeMode: Text.Fit
    }
}