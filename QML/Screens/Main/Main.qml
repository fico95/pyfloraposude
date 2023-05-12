import QtQuick 2.14
import Enums 1.0

import "../../Controls"
import "../Users"
import "../Welcome"
import "../Pots"
import "../Plants"

Item {
    id: root

    signal registrationSuccessful
    signal loginSuccessful
    signal plantAdded
    signal potAdded
    signal plantSelected
    signal actionCanceled
    signal userModified
    signal loginClicked
    signal registerClicked
    signal forgottenPasswordClicked
    signal plantSelectClicked
    signal plantEditClicked
    signal potEditClicked
    signal userModifyClicked
    signal userDeleteClicked
    signal openImageLoadDialog

    function handleFileDialogClose(filePath) {
        if (loader.item.handleFileDialogClose !== undefined) {
            loader.item.handleFileDialogClose(filePath)
        }
    }

    Loader {
        id: loader
        anchors.fill: parent
        sourceComponent: {
            switch (stackController.currentScreen) {
                case Enums.Screen.Welcome:
                   return welcomeComponent
                case Enums.Screen.Registration:
                    return registrationComponent
                case Enums.Screen.Login:
                   return loginComponent
                case Enums.Screen.ForgottenPassword:
                   return forgottenPasswordComponent
                case Enums.Screen.UserEditor:
                    return editComponent
                case Enums.Screen.UserPasswordChange:
                    return modifyComponent
                case Enums.Screen.UserDelete:
                    return deleteComponent
                case Enums.Screen.Pots:
                    return potsViewComponent
                case Enums.Screen.PotLoader:
                    return potLoaderComponent
                case Enums.Screen.PotEditor:
                    return potEditorComponent
                case Enums.Screen.Plants:
                    return plantsViewComponent
                case Enums.Screen.PlantEditor:
                    return plantEditorComponent
                case Enums.Screen.PlantLoader:
                    return plantLoaderComponent
                case Enums.Screen.PlantSelect:
                    return plantSelectComponent
                default:
                    return Qt.quit()
            }
        }
    }

    Component {
        id: welcomeComponent
        Welcome {
            onLoginClicked: {
                root.loginClicked()
            }
            onRegisterClicked: {
                root.registerClicked()
            }
        }
    }

    Component {
        id: registrationComponent
        UserRegistration {
            onRegistrationTriggered: {
                if (userHandler.addUser(userNameText, passwordText)) {
                    root.registrationSuccessful()
                }
                else {
                    registrationFailed = true
                    updateWarningText()
                }
            }
        }
    }

    Component {
        id: loginComponent
        UserLogin {
            onLoginTriggered: {
                if (userHandler.authenticateUser(userNameText, passwordText)) {
                    root.loginSuccessful()
                }
                else {
                    loginFailed = true
                    updateWarningText()
                }
            }
            onForgottenPasswordClicked: {
                root.forgottenPasswordClicked()
            }
        }
    }

    Component {
        id: forgottenPasswordComponent
        UserForgottenPassword {
            onAcceptClicked: {
                if (userHandler.removeUsers()) {
                    root.userModified()
                }
            }
        }
    }

    Component {
        id: editComponent
        UserEditor {  
            onModifyClicked: {
                root.userModifyClicked()
            }
            onDeleteClicked: {
                root.userDeleteClicked()
            }
        }
    }

    Component {
        id: deleteComponent
        UserDelete {  
            onAcceptClicked: {
                if (userHandler.removeUsers()) {
                    root.userModified()
                }
            }
        }
    }

    Component {
        id: modifyComponent
        UserModify {  
            onPasswordChangeTriggered: {
                if (userHandler.updateUserPassword(userNameText, passwordText, newPasswordText)) {
                    root.userModified()
                }
                else {
                    modifyFailed = true
                    updateWarningText()
                }
            }
        }
    }

    Component {
        id: potsViewComponent
        PotsView {
            onOpenPotEdit: function(potId) {
                if (floraManager.setCurrentPot(potId)) {
                    root.potEditClicked()
                }
            }
        }
    }

    Component {
        id: potLoaderComponent
        PotLoader {
            onPlantSelectTriggered: {
                root.plantSelectClicked()
            }
            onPlantClearTriggered: {
                floraManager.resetCurrentPlant()
            }
            onPotLoaded: {
                root.potAdded()
            }
        }
    }

    Component {
        id: plantsViewComponent
        PlantsView {
            onOpenPlantEditor: function(plantId) {
                if (floraManager.setCurrentPlant(plantId)) {
                    root.plantEditClicked()
                }
            }
        }
    }

    Component {
        id: plantEditorComponent
        PlantEditor {
            onLoadTriggered: {
                root.openImageLoadDialog()
            }
        }
    }

    Component {
        id: plantLoaderComponent
        PlantLoader {
            onLoadTriggered: {
                root.openImageLoadDialog()
            }
            onSaveClicked: {
                let filePath = iconSource.toString()
                filePath = filePath.replace("file://", "")
                if (filePath !== "") {
                    filePath = imageManager.copyImage(filePath)
                    if (filePath === "") {
                        return
                    }
                }
                if (floraManager.addPlant(plantName, filePath, soilMoistureValue, phValue, salinityValue, lightLevelValue, temperatureValue)) {
                    root.plantAdded()
                }
            }
        }
    }

    Component {
        id: plantSelectComponent
        PlantSelector {
            onPlantSelected: function(plantId) {
                if (floraManager.setCurrentPlant(plantId)) {
                    root.plantSelected()
                }
            }
        }
    }

    Component {
        id: potEditorComponent
        PotEditor {
            onPlantSelectTriggered: {
                root.plantSelectClicked()
            }
            onPlantClearTriggered: {
                floraManager.removePlantFromCurrentPot()
            }
        }
    }
}
