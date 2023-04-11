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
    }

    Component {
        id: registrationComponent
        Registration {
            onRegistrationSuccessful: {
                loader.sourceComponent = loginComponent
            }
        }
    }

    Component {
        id: loginComponent
        Login {}
    }

    Component.onCompleted: {
        if (userHandler.user_exists())
            loader.sourceComponent = loginComponent
        else
            loader.sourceComponent = registrationComponent
    }
}
