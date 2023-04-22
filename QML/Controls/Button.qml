import QtQuick 2.15

ButtonBackground {
    property alias text: text

    Text {
        id: text
        anchors.centerIn: parent
        width: parent.width
        height: parent.height * 0.5
        font.pixelSize: height
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        elide: Text.ElideRight
        color: mouseArea.containsMouse ? "#333333" : "#555555"
    }
}
