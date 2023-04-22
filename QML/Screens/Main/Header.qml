import QtQuick 2.14
import QtQuick.Controls 2.12

Rectangle {
    id: header

    width: parent.width
    height: parent.height / 10
    color: "lightgrey"

    Button {
        anchors {
            right: parent.right
            rightMargin: width
            verticalCenter: parent.verticalCenter
        }
        height: parent.height * 0.5
        width: parent.width * 0.1
        text: "Back"
        visible: stackController.currentScreen !== 0
        onClicked: stackController.goBack()
    }

    Text {
        anchors {
            left: parent.left
            leftMargin: parent.width / 5
            verticalCenter: parent.verticalCenter
        }
        text: "PyFloraPosude"
        font.pixelSize: 20
    }
}