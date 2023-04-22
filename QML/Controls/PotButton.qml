import QtQuick 2.15

ButtonBackground {
    property alias potName: potName.text
    property alias plantIconSource: plantIcon.source

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
    }

    Text {
        id: potName
        anchors {
            right: parent.right
            top: parent.top
            rightMargin: parent.width * 0.05
            topMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        height: parent.height * 0.4
        font {
            pixelSize: height / 4
            bold: true
        }
        maximumLineCount: 2
        elide: Text.ElideRight
        wrapMode: Text.WordWrap
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignTop
        color: "#333333"
    }
}
