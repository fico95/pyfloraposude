import QtQuick 2.14

import "../../Controls"

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
                case 6:
                    return potEditorComponent
                case 7:
                    return plantEditorComponent
                case 8:
                    return editComponent
                case 9:
                    return plantLoaderComponent
                case 10:
                    return potLoaderComponent
                case 11:
                    return plantSelectComponent
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
            onOpenPotEdit: function(potId) {
                if (floraManager.setCurrentPot(potId)) {
                    stackController.openPotEditorScreen()
                }
            }
        }
    }

    Component {
        id: potLoaderComponent
        PotLoader {
            onPlantSelectTriggered: {
                stackController.openPlantSelectScreen()
            }
            onPlantClearTriggered: {
                floraManager.resetCurrentPlant()
            }
            onPotLoaded: {
                stackController.goBack()
            }
        }
    }

    Component {
        id: plantsViewComponent
        PlantsView {
            onOpenPlantEditor: function(plantId) {
                if (floraManager.setCurrentPlant(plantId)) {
                    stackController.openPlantEditorScreen()
                }
            }
        }
    }

    Component {
        id: plantEditorComponent
        PlantEditor {
            onImageChangeTriggered: {
                plantImageLoadDialog.open()
            }
        }
    }

    Component {
        id: plantLoaderComponent
        PlantLoader {
            onImageLoadTriggered: {
                plantImageLoadDialog.open()
            }
            onPlantAdded: {
                stackController.goBack()
            }
        }
    }

    Component {
        id: plantSelectComponent
        PlantSelector {
            onPlantSelected: {
                if (floraManager.setCurrentPlant(plantId)) {
                    stackController.goBack()
                }
            }
        }
    }

    Component {
        id: potEditorComponent
        PotEditor {
        }
    }

    CustomFileDialog {
        id: plantImageLoadDialog
        onAccepted: {
            if (loader.item.handleFileDialogClose !== undefined) {
                loader.item.handleFileDialogClose(plantImageLoadDialog.fileUrl.toString())
            }
        }
    }
}
