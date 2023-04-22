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
        text: "Back"
        visible: stackController.currentScreen !== 0
        onClicked: stackController.goBack()
    }

    Button {
        anchors {
            right: parent.right
            rightMargin: width
            verticalCenter: parent.verticalCenter
        }
        height: parent.height * 0.5
        width: parent.width * 0.1
        text: "Edit user"
        visible: stackController.userEditable
        onClicked: stackController.openUserEditorScreen()
    }

    Rectangle {
        anchors.centerIn: parent
        width: title.width * 1.5
        height: title.height * 1.5
        radius: 10
        color: "grey"
        Text {
            id: title
            anchors.centerIn: parent
            text: "PyFloraPosude"
            font.pixelSize: 20
        }
    }
}