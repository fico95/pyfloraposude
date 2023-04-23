import QtQuick 2.14
import QtQuick.Controls 2.12

ToolBar {
    readonly property bool isWelcomeScreen: stackController.currentScreen === 0

    signal drawerButtonClicked

    width: parent.width
    height: parent.height * 0.1

    Text {
        anchors.centerIn: parent
        font.pointSize: Math.max(12, parent.height * 0.5)
        text: "PyFloraPosude"
        color: "white"
    }

    ToolButton {
        id: backButton
        visible: !isWelcomeScreen
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
            margins: parent.height * 0.1
        }
        width: height
        font.pointSize: Math.max(12, parent.height * 0.5)
        text: "‹"
        onClicked: stackController.goBack()
    }

    ToolButton {
        id: toolButton
        anchors {
            right: parent.right
            top: parent.top
            bottom: parent.bottom
            margins: parent.height * 0.1
        }
        width: height
        font.pointSize: Math.max(12, parent.height * 0.5)
        text: "⋮"
        onClicked: drawerButtonClicked()
    }
}