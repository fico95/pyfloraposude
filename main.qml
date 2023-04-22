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
        sourceComponent: {
            switch (stackController.current_screen) {
                case 0:
                    return welcomeComponent
                case 1:
                    return registrationComponent
                case 2:
                    return loginComponent
                case 3:
                    return forgottenPasswordComponent
            }
        }
    }

    Component {
        id: registrationComponent
        Registration {
            onRegistrationSuccessful: {
                stackController.open_login_screen()
            }
            onClose: {
                stackController.open_welcome_screen()
            }
        }
    }

    Component {
        id: welcomeComponent
        Welcome {
            onLoginClicked: {
                stackController.open_login_screen()
            }
            onRegisterClicked: {
                stackController.open_registration_screen()
            }
            onForgottenPasswordClicked: {
                stackController.open_forgotten_password_screen()
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
                stackController.open_welcome_screen()
            }
        }
    }

    Component {
        id: forgottenPasswordComponent
        ForgottenPassword {
            onAcceptClicked: {
                if (userHandler.delete_all_users()) {
                    stackController.open_welcome_screen()
                }
            }
            onCancelClicked: {
                stackController.open_welcome_screen()
            }
        }
    }
}
