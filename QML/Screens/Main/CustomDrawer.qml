import QtQuick 2.14
import QtQuick.Controls 2.12

Drawer {
    id: drawer

    function toggle() {
        if(!drawer.opened) {
            drawer.open()
        }
        if(drawer.opened) {
            drawer.close()
        }
    }

    enter: Transition { SmoothedAnimation { velocity: 1 } }
    exit: Transition { SmoothedAnimation { velocity: 1 } }

    Rectangle {
        anchors.fill: parent
        color: "white"
    }

    Column {
        anchors {
            fill: parent
            margins: 5
        }
        spacing: 5
        Button {
            visible: stackController.currentScreen !== 0
            width: parent.width
            height: parent.height / 10
            text: "Home"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.goToWelcomeScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 4
            width: parent.width
            height: parent.height / 10
            text: "Sync"
            font.pixelSize: height * 0.75
            onClicked: {
                floraManager.updatePotsSensorData()
            }
        }
        Button {
            visible: stackController.currentScreen !== 0 && stackController.currentScreen !== 1 && stackController.currentScreen !== 2 && stackController.currentScreen !== 3 && stackController.currentScreen !== 8
            width: parent.width
            height: parent.height / 10
            text: "Profile"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.openUserEditorScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 4
            width: parent.width
            height: parent.height / 10
            text: "Add pot"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.openPotLoaderScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 4
            width: parent.width
            height: parent.height / 10
            text: floraManager.allPotsShown ? "Show empty" : "Show all"
            font.pixelSize: height * 0.75
            onClicked: {
                floraManager.tooglePotVisibility()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 12
            width: parent.width
            height: parent.height / 10
            text: "Edit pot"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.openPotEditorScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 12
            width: parent.width
            height: parent.height / 10
            text: "Edit pot"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.openPotEditorScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 4
            width: parent.width
            height: parent.height / 10
            text: "Show plants"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.openPlantsScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 5
            width: parent.width
            height: parent.height / 10
            text: "Add plant"
            font.pixelSize: height * 0.75
            onClicked: {
                stackController.openPlantLoaderScreen()
                drawer.close()
            }
        }
        Button {
            visible: stackController.currentScreen === 7
            width: parent.width
            height: parent.height / 10
            text: "Remove plant"
            font.pixelSize: height * 0.75
            onClicked: {
                if (floraManager.removeCurrentPlant()) {
                    stackController.handlePlantRemove()
                    drawer.close()
                }
            }
        }
    }
                
    Button {
        anchors.bottom: parent.bottom
        width: parent.width
        height: parent.height / 10
        text: "Quit"
        font.pixelSize: height * 0.75
        onClicked: {
            Qt.quit()
        }
    }
}
