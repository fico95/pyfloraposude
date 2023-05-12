import QtQuick 2.15

import "../../Controls"

Item {
    id: root

    anchors.fill: parent

    signal modifyClicked
    signal deleteClicked

    CustomButton {
        anchors {
            horizontalCenter: parent.horizontalCenter
            verticalCenter: parent.verticalCenter
            horizontalCenterOffset: -width / 1.5
        }
        width: root.width / 4
        text: "Modify"
        onClicked: {
            modifyClicked()
        }
    }
    CustomButton {
        anchors {
            horizontalCenter: parent.horizontalCenter
            verticalCenter: parent.verticalCenter
            horizontalCenterOffset: width / 1.5
        }
        width: root.width / 4
        text: "Delete"
        onClicked: {
            deleteClicked()
        }
    }



    // function validateUserDelete() {
    //     if (textFieldUsername.text === "") {
    //         warningText.text = "Username cannot be empty."
    //         return false
    //     } else if (textFieldOldPassword.text === "") {
    //         warningText.text = "Password cannot be empty."
    //         return false
    //     }
    //     warningText.text = ""
    //     return true
    // }

    // function validatePasswordChange() {
    //     if (textFieldUsername.text === "") {
    //         warningText.text = "Username cannot be empty."
    //         return false
    //     } else if (textFieldNewPassword.text !== textFieldConfirmNewPassword.text) {
    //         warningText.text = "Passwords do not match."
    //         return false
    //     } else if (textFieldNewPassword.text.length < 8) {
    //         warningText.text = "Password must be at least 8 characters long."
    //         return false
    //     } else if (textFieldNewPassword.text === textFieldOldPassword.text) {
    //         warningText.text = "New password must be different from old password."
    //         return false
    //     }
    //     warningText.text = ""
    //     return true
    // }

    // Column {
    //     width: parent.width / 2
    //     anchors.verticalCenter: parent.verticalCenter
    //     anchors.horizontalCenter: parent.horizontalCenter

    //     spacing: 10

    //     Label {
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         horizontalAlignment: Text.AlignHCenter
    //         text: "Change Password"
    //         font.pixelSize: 20
    //     }

    //     TextField {
    //         id: textFieldUsername
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         placeholderText: "Username"
    //     }

    //     TextField {
    //         id: textFieldOldPassword
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         placeholderText: "Old Password"
    //         echoMode: TextInput.Password
    //     }

    //     TextField {
    //         id: textFieldNewPassword
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         placeholderText: "New Password"
    //         echoMode: TextInput.Password
    //     }

    //     TextField {
    //         id: textFieldConfirmNewPassword
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         placeholderText: "New Password"
    //         echoMode: TextInput.Password
    //     }

    //     Label {
    //         id: warningText
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         color: "red"
    //         visible: text !== ""
    //     }

    //     Button {
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         text: "Change Password"
    //         onClicked: {
    //             if (!validatePasswordChange()) {
    //                 return
    //             }
    //             if (!userHandler.updateUserPassword(textFieldUsername.text, textFieldOldPassword.text, textFieldNewPassword.text)) {
    //                 warningText.text = "Failed to change password."
    //                 return
    //             }
    //             stackController.handleUserChange()
    //         }
    //     }

    //     Button {
    //         anchors.horizontalCenter: parent.horizontalCenter
    //         width: parent.width
    //         text: "Delete Account"
    //         onClicked: {
    //             if (!validateUserDelete()) {
    //                 return
    //             }
    //             if (!userHandler.removeUserByUsername(textFieldUsername.text, textFieldOldPassword.text)) {
    //                 warningText.text = "Failed to delete account."
    //                 return
    //             }
    //             stackController.handleUserChange()
    //         }
    //     }
    // }
}
