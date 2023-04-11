import QtQuick 2.14
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    signal loginSuccessful()

    property string username: ""
    property string password: ""
    property string message: ""

    ColumnLayout {
        anchors.centerIn: parent

        TextField {
            placeholderText: "Username"
            text: username
            onTextChanged: username = text.trim()
        }

        TextField {
            placeholderText: "Password"
            text: password
            echoMode: TextInput.Password
            onTextChanged: password = text.trim()
        }

        Text {
            text: message
            color: "red"
            visible: message !== ""
        }

        Button {
            text: "Login"
            onClicked: {
                if (username === "" || password === "") {
                    message = "Username and password are required."
                } else {
                    if (userHandler.authenticate_user(username, password)) {
                        loginSuccessful()
                    }
                    else {
                        message = "Incorrect username or password."
                    }
                }
            }
        }
    }
}
