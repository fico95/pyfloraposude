import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    property alias userNameText: textFieldUsername.text
    property alias passwordText: textFieldPassword.text

    property bool loginFailed: false

    signal loginTriggered
    signal forgottenPasswordClicked

    function updateWarningText() {
        if (loginFailed) {
            warningText.text = "Incorrect username or password."
        } else {
            warningText.text = ""
        }
    }

    anchors.fill: parent

    Column {
        width: parent.width / 2
        anchors {
            top: parent.top
            topMargin: parent.height / 3
            bottom: parent.bottom
        }
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: 10

        CustomTextField {
            id: textFieldUsername
            placeholderText: "Username"
            onTextChanged: {
                loginFailed = false
                updateWarningText()
            }
        }

        CustomTextField {
            id: textFieldPassword
            placeholderText: "Password"
            enabled: userNameText !== ""
            echoMode: TextInput.Password
            onTextChanged: {
                loginFailed = false
                updateWarningText()
            }
        }

        CustomText {
            id: warningText
            color: "red"
            height: parent.height / 16
            opacity: text !== "" ? 1 : 0
            font.pointSize: Math.max(8, Math.min(14, parent.height * root.sizeCale))
        }

        CustomButton {
            width: parent.width
            text: "Login"
            enabled: textFieldUsername.text !== "" && textFieldPassword.text !== ""
            onClicked: {
                loginTriggered()
            }
        }

        CustomButton {
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            text: "Forgotten Password"
            onClicked: forgottenPasswordClicked()
        }
    }
}
