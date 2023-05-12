import QtQuick 2.14
import QtQuick.Controls 2.12
import Enums 1.0

import "../../Controls"

ToolBar {
    readonly property bool isWelcomeScreen: stackController.currentScreen === Enums.Screen.Welcome

    signal backButtonClicked
    signal drawerButtonClicked

    width: parent.width
    height: parent.height * 0.1

    CustomText {
        anchors.centerIn: parent
        text: "PyFloraPosude"
        color: "white"
        sizeCale: 0.5
    }

    CustomToolButton {
        visible: !isWelcomeScreen
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
            margins: parent.height * 0.1
        }
        text: "‹"
        onClicked: backButtonClicked()
    }

    CustomToolButton {
        anchors {
            right: parent.right
            top: parent.top
            bottom: parent.bottom
            margins: parent.height * 0.1
        }
        text: "⋮"
        onClicked: drawerButtonClicked()
    }
}