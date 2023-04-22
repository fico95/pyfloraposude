import QtQuick 2.14
import QtQuick.Controls 2.12

Item {
    readonly property bool registeredUsers: userHandler.numUsers > 0

    signal registerClicked
    signal loginClicked
    signal forgottenPasswordClicked
    
    anchors.fill: parent

    Column {
        id: mainColumn

        width: parent.width / 2
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

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

        Button {
            visible: !registeredUsers
            anchors.horizontalCenter: parent.horizontalCenter
            width: mainColumn.width / 2
            text: "Register"
            onClicked: registerClicked()
        }

        Row {
            id: buttonRow

            visible: registeredUsers
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter

            Button {
                width: mainColumn.width / 2 - buttonRow.spacing / 2
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
                width: mainColumn.width / 2 - buttonRow.spacing / 2
                text: "Forgotten Password"
                onClicked: forgottenPasswordClicked()
            }
        }
    }
}
