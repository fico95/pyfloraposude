import QtQuick 2.14
import QtQuick.Controls 2.12

Rectangle {
    id: header

    width: parent.width
    height: parent.height / 10
    color: "lightgrey"

    Button {
        anchors {
            left: parent.left
            leftMargin: width
            verticalCenter: parent.verticalCenter
        }
        height: parent.height * 0.5
        width: parent.width * 0.1
        text: "Quit"
        onClicked: Qt.quit()
    }
}