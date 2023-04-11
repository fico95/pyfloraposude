import QtQuick 2.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.15

Window {
    width: 1280
    height: 960
    visible: true

    minimumWidth: 640
    minimumHeight: 480

    Loader {
        id: loader
        anchors.fill: parent
        sourceComponent: welcomeComponent
    }

    Component {
        id: registrationComponent
        Registration {
            onRegistrationSuccessful: {
                loader.sourceComponent = loginComponent
            }
            onClose: {
                loader.sourceComponent = welcomeComponent
            }
        }
    }

    Component {
        id: welcomeComponent
        Welcome {
            onLoginClicked: {
                loader.sourceComponent = loginComponent
            }
            onRegisterClicked: {
                loader.sourceComponent = registrationComponent
            }
        }
    }

    Component {
        id: loginComponent
        Login {
            onLoginSuccessful: {
                loader.sourceComponent = null
            }
            onClose: {
                loader.sourceComponent = welcomeComponent
            }
        }
    }
}
