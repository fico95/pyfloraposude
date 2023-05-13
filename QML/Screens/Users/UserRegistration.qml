import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    property alias userNameText: textFieldUsername.text
    property alias passwordText: textFieldPassword.text
    property alias confirmPasswordText: textFieldConfirmPassword.text

    property bool registrationFailed: false

    signal registrationTriggered()

    function updateWarningText() {
        if (passwordText == "") {
            warningText.text = ""
        }
        else if (!userHandler.checkPasswordStrength(passwordText)) {
            warningText.text = "Password must be at least 8 characters long and contain at least one capital letter, one lowercase letter, one number, and one special character."
        }
        else if (passwordText !== confirmPasswordText) {
            warningText.text = "Passwords do not match."
        }
        else if (registrationFailed) {
            warningText.text = "Registration failed."
        }
        else {
            warningText.text = ""
        }
    }

    anchors.fill: parent   

    Column {
        width: parent.width / 2
        anchors {
            top: parent.top
            topMargin: parent.height / 10
            bottom: parent.bottom
        }
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: 10

        CustomText {
            height: parent.height / 4
            text: "Registration"
            textBold: true
        }

        CustomTextField {
            id: textFieldUsername
            placeholderText: "Username"
        }

        CustomTextField {
            id: textFieldPassword
            placeholderText: "Password"
            enabled: userNameText !== ""
            echoMode: TextInput.Password
            onTextChanged: updateWarningText()
        }

        CustomTextField {
            id: textFieldConfirmPassword
            placeholderText: "Confirm Password"
            enabled: passwordText !== ""
            echoMode: TextInput.Password
            onTextChanged: updateWarningText()
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
            text: "Register"
            enabled: userNameText !== "" && passwordText !== "" && confirmPasswordText !== "" && passwordText === confirmPasswordText
            onClicked: {
                registrationTriggered()
            }
        }
    }
}
