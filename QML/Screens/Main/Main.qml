import QtQuick 2.14
import QtQuick.Controls 2.15

import "../Users"
import "../Welcome"
import "../Pots"
import "../Plants"

Item {
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
                case 4:
                    return potsViewComponent
                case 5:
                    return plantsViewComponent
                case 8:
                    return editComponent
                case 5:
                case 6:
                case 7:
                    return plantEditorComponent
                default:
                    return null
            }
        }
    }

    Component {
        id: registrationComponent
        Registration {
            onRegistrationSuccessful: {
                stackController.goBack()
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
        }
    }

    Component {
        id: loginComponent
        Login {
            onLoginSuccessful: {
                stackController.openPotsScreen()
            }
            onForgottenPasswordClicked: {
                stackController.openForgottenPasswordScreen()
            }
        }
    }

    Component {
        id: forgottenPasswordComponent
        ForgottenPassword {
            onAcceptClicked: {
                if (userHandler.deleteAllUsers()) {
                    stackController.handleUserChange()
                }
            }
            onCancelClicked: {
                stackController.goBack()
            }
        }
    }

    Component {
        id: editComponent
        Edit {  
        }
    }

    Component {
        id: potsViewComponent
        PotsView {
            onOpenPlantsView: {
                stackController.openPlantsScreen()
            }
        }
    }

    Component {
        id: plantsViewComponent
        PlantsView {
            onOpenPlantEditor: function(plantId) {
                if (plantsHandler.setCurrentPlant(plantId)) {
                    stackController.openPlantEditorScreen()
                }
            }
        }
    }

    Component {
        id: plantEditorComponent
        PlantEditor {
            onCurrentPlantRemoved: {
                stackController.goBack()
            }
        }
    }
}
