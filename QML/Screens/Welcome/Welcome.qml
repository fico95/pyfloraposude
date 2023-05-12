import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

Item {
    readonly property bool registeredUsers: userHandler.usersCount > 0

    signal registerClicked
    signal loginClicked
    
    anchors.fill: parent

    Column {
        id: mainColumn

        width: parent.width / 2
        anchors {
            top: parent.top
            topMargin: parent.height / 4
            bottom: parent.bottom
        }
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: 20

        CustomText {
            height: parent.height / 4
            text: "Welcome"
            textBold: true
        }

        CustomText {
            height: parent.height / 20
            text: registeredUsers ? "Registered user found." : "No registered user found."
        }

        Item {
            width: parent.width
            height: parent.height / 12
        }

        CustomButton {
            anchors.horizontalCenter: parent.horizontalCenter
            text: registeredUsers ? "Login" : "Register"
            onClicked: {
                if (registeredUsers) {
                    loginClicked()
                }
                else {
                    registerClicked()
                }
            }
        }
    }
}
