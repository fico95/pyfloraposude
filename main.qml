import QtQuick 2.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.15

Window {
    width: 1280
    height: 960
    visible: true

    minimumWidth: 640
    minimumHeight: 480

Rectangle {
    id: registrationScreen
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    width: parent.width * 0.8
    height: parent.height * 0.8
    color: "white"

    Column {
        id: column
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        spacing: 10
        width: parent.width

            // Username input field
    TextField {
        id: usernameInput
        placeholderText: "Username"

        anchors.horizontalCenter: parent.horizontalCenter
        width:parent.width
    }

    // Email input field
    TextField {
        id: emailInput
        placeholderText: "Email"
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width
    }

    // Password input field
    TextField {
        id: passwordInput
        placeholderText: "Password"
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width
        echoMode: TextInput.Password
    }

    // Confirm password input field
    TextField {
        id: confirmPasswordInput
        placeholderText: "Confirm password"
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width
        echoMode: TextInput.Password
        onTextChanged: {
            if (confirmPasswordInput.text !== passwordInput.text) {
                confirmPasswordInput.color = "red";
            } else {
                confirmPasswordInput.color = "black";
            }
        }
    }
    }



    // Register button
    Button {
        id: registerButton
        text: "Register"
        anchors.top: column.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width * 0.8
        onClicked: {
            // TODO: Add registration logic here
        }
    }
}

}
