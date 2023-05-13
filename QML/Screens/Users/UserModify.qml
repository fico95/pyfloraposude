import QtQuick 2.15

import "../../Controls"

Item {
    id: root

    property alias userNameText: textFieldUsername.text
    property alias passwordText: textFieldPassword.text
    property alias newPasswordText: textFieldNewPassword.text

    anchors.fill: parent

    property bool modifyFailed: false

    signal passwordChangeTriggered()

    function updateWarningText() {
        if (userNameText == "" || passwordText == "") {
            warningText.text = ""
        }
        else if (!userHandler.authenticateUser(userNameText, passwordText)) {
            warningText.text = "Incorrect username or password."
        }
        else if (!userHandler.checkPasswordStrength(passwordText)) {
            warningText.text = "Password must be at least 8 characters long and contain at least one capital letter, one lowercase letter, one number, and one special character."
        }
        else if (passwordText === newPasswordText) {
            warningText.text = "New password must be different from old password."
        }
        else if (newPasswordText !== "" && !userHandler.checkPasswordStrength(newPasswordText)) {
            warningText.text = "Password must be at least 8 characters long and contain at least one capital letter, one lowercase letter, one number, and one special character."
        }
        else if (modifyFailed) {
            warningText.text = "Failed to change password."
        }
        else {
            warningText.text = ""
        }
    }

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
            text: "Change Password"
            textBold: true
        }

        CustomTextField {
            id: textFieldUsername
            placeholderText: "Username"
            onTextChanged: updateWarningText()
        }

        CustomTextField {
            id: textFieldPassword
            placeholderText: "Password"
            enabled: userNameText !== ""
            echoMode: TextInput.Password
            onTextChanged: updateWarningText()
        }

        CustomTextField {
            id: textFieldNewPassword
            placeholderText: "New Password"
            enabled: passwordText !== ""
            echoMode: TextInput.Password
            onTextChanged: {
                modifyFailed = false
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
            id: changePasswordButton
            width: parent.width
            text: "Change Password"
            enabled: userNameText !== "" && passwordText !== "" && newPasswordText !== ""
            onClicked: {
                modifyFailed = false
                updateWarningText()
                if (warningText.text === "") {
                    passwordChangeTriggered()
                }
            }
        }
    }

    Keys.onEnterPressed: {
        if (changePasswordButton.enabled) {
            modifyFailed = false
            updateWarningText()
            if (warningText.text === "") {
                passwordChangeTriggered()
            }
        }
    }

     Keys.onReturnPressed: {
        if (changePasswordButton.enabled) {
            modifyFailed = false
            updateWarningText()
            if (warningText.text === "") {
                passwordChangeTriggered()
            }
        }
    }
}
