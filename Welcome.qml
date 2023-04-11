import QtQuick 2.14
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12

Item {
    width: 400
    height: 300

    readonly property bool registeredUsers: userHandler.num_users > 0

    signal registerClicked
    signal loginClicked
    signal forgottenPasswordClicked

    ColumnLayout {
        id: welcomeLayout
        anchors.centerIn: parent

        Label {
            text: "Welcome"
            font.pixelSize: 36
            Layout.alignment: Qt.AlignHCenter
        }

        Label {
            id: noUserLabel
            text: "No registered user found."
            visible: !registeredUsers
            Layout.alignment: Qt.AlignHCenter
        }

        Label {
            id: registeredUserLabel
            text: "Registered user found."
            visible: registeredUsers
            Layout.alignment: Qt.AlignHCenter
        }

        RowLayout {
            id: buttonRow
            Layout.alignment: Qt.AlignHCenter

            Button {
                id: registerButton
                text: "Register"
                visible: !registeredUsers
                onClicked: registerClicked()
            }

            Button {
                id: loginButton
                text: "Login"
                visible: registeredUsers
                onClicked: loginClicked()
            }

            Button {
                id: forgottenPasswordButton
                text: "Forgotten Password"
                visible: registeredUsers
                onClicked: forgottenPasswordClicked()
            }
        }

        Button {
            id: quitButton
            text: "Quit"
            onClicked: Qt.quit()
            Layout.alignment: Qt.AlignHCenter
        }
    }
}
