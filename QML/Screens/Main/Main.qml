import QtQuick 2.14
import QtQuick.Controls 2.15

import "../Users"
import "../Welcome"

Item {
    anchors.fill: parent

    Loader {
        id: loader
        anchors.fill: parent
        sourceComponent: {
            switch (stackController.currentScreen) {
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
                stackController.openLoginScreen()
            }
            onClose: {
                stackController.openWelcomeScreen()
            }
        }
    }

    Component {
        id: welcomeComponent
        Welcome {
            onLoginClicked: {
                stackController.openLoginScreen()
            }
            onRegisterClicked: {
                stackController.openRegistrationScreen()
            }
            onForgottenPasswordClicked: {
                stackController.openForgottenPasswordScreen()
            }
            onQuitClicked: {
                Qt.quit()
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
                stackController.openWelcomeScreen()
            }
        }
    }

    Component {
        id: forgottenPasswordComponent
        ForgottenPassword {
            onAcceptClicked: {
                if (userHandler.deleteAllUsers()) {
                    stackController.openWelcomeScreen()
                }
            }
            onCancelClicked: {
                stackController.openWelcomeScreen()
            }
        }
    }
}
