import QtQuick 2.14
import QtQuick.Controls 2.15

Item {
    signal loginSuccessful
    signal forgottenPasswordClicked

    anchors.fill: parent

    Column {
        width: parent.width / 2
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: 10

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

        Text {
            id: warningText
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            color: "red"
            visible: text !== ""
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            text: "Login"
            onClicked: {
                if (textFieldUsername.text === "" || textFieldPassword.text === "") {
                    warningText.text = "Username and password are required."
                } else {
                    if (userHandler.authenticateUser(textFieldUsername.text, textFieldPassword.text)) {
                        loginSuccessful()
                    }
                    else {
                        warningText.text = "Incorrect username or password."
                    }
                }
            }
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            text: "Forgotten Password"
            onClicked: forgottenPasswordClicked()
        }
    }
}
