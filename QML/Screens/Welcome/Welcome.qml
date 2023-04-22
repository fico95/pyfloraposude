import QtQuick 2.14
import QtQuick.Controls 2.12

Item {
    anchors.fill: parent

    readonly property bool registeredUsers: userHandler.numUsers > 0

    signal registerClicked
    signal loginClicked
    signal forgottenPasswordClicked
    signal quitClicked

    Column {
        id: welcomeLayout
        anchors.centerIn: parent
        spacing: 10

        Label {
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 36
            text: "Welcome"
        }

        Label {
            visible: !registeredUsers
            anchors.horizontalCenter: parent.horizontalCenter
            text: registeredUsers ? "Registered user found." : "No registered user found."
        }

        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 10

            Button {
                visible: !registeredUsers
                text: "Register"
                onClicked: registerClicked()
            }

            Button {
                visible: registeredUsers
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

            Button {
                visible: registeredUsers
                text: "Forgotten Password"
                onClicked: forgottenPasswordClicked()
            }
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            text: "Quit"
            onClicked: quitClicked()
        }
    }
}
