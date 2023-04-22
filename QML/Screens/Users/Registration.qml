import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: root
    width: 400
    height: 300

    signal registrationSuccessful
    signal close

    property string username: ""
    property string password: ""
    property string confirmPassword: ""
    property string message: ""

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 10

        Label {
            text: "Registration"
            font.pixelSize: 20
        }

        TextField {
            placeholderText: "Username"
            onTextChanged: username = text
        }

        TextField {
            placeholderText: "Password"
            echoMode: TextInput.Password
            onTextChanged: password = text
        }

        TextField {
            placeholderText: "Confirm Password"
            echoMode: TextInput.Password
            onTextChanged: confirmPassword = text
        }

        Label {
            visible: message !== ""
            color: "red"
            text: message
        }

        Button {
            text: "Register"
            onClicked: {
                if (password !== confirmPassword) {
                    message = "Passwords do not match."
                } else if (userHandler.addUser(username, '123')) {
                    message = "Registration successful."
                    registrationSuccessful()
                } else {
                    message = "Registration failed."
                }
            }
        }

        Button {
            text: "Back to Login"
            onClicked: close()
        }
    }
}
