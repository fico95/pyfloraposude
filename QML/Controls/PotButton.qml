import QtQuick 2.15

ButtonBackground {
    Rectangle {
        id: roomIcon
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
            leftMargin: parent.width * 0.1
            topMargin: parent.height * 0.1
            bottomMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        color: "#333333"
    }

    Text {
        id: roomName
        anchors {
            right: parent.right
            top: parent.top
            rightMargin: parent.width * 0.1
            topMargin: parent.height * 0.1
        }
        height: parent.height * 0.1
        font.pixelSize: height
        text: "Living Room"
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        color: "#333333"
    }
}
