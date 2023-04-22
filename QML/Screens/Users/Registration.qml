import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    signal registrationSuccessful

    anchors.fill: parent   

    Column {
        width: parent.width / 2
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: 10

        Label {
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            horizontalAlignment: Text.AlignHCenter
            text: "Registration"
            font.pixelSize: 20
        }

        TextField {
            id: textFieldUsername
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            placeholderText: "Username"
        }

        TextField {
            id: textFieldPassword
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            placeholderText: "Password"
            echoMode: TextInput.Password
        }

        TextField {
            id: textFieldConfirmPassword
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            placeholderText: "Confirm Password"
            echoMode: TextInput.Password
        }

        Label {
            id: warningText
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            color: "red"
            visible: text !== ""
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            text: "Register"
            onClicked: {
                if (textFieldPassword.text !== textFieldConfirmPassword.text) {
                    warningText.text = "Passwords do not match."
                } else if (userHandler.addUser(textFieldUsername.text, textFieldPassword.text)) {
                    warningText.text = "Registration successful."
                    registrationSuccessful()
                } else {
                    warningText.text = "Registration failed."
                }
            }
        }
    }
}
