import QtQuick 2.14
import QtQuick.Window 2.14

import "Screens/Main"

Window {
    visible: true

    width: 1280
    height: 960

    minimumWidth: 640
    minimumHeight: 480

    CustomHeader {
        id: header
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        onBackButtonClicked: stackController.goBack()
        onDrawerButtonClicked: drawer.toggle()
    }    

    Main {
        anchors {
            top: header.bottom
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }
    }

    CustomDrawer {
        id: drawer
        edge: Qt.RightEdge
        y: header.height
        width: parent.width / 2
        height: parent.height - header.height
        onHomeClicked: {
            stackController.goToWelcomeScreen(); 
            drawer.close() 
        }
        onProfileClicked: {
            stackController.openUserEditorScreen()
            drawer.close()
        }
        onSyncClicked: {
            floraManager.updatePotsSensorData()
        }
        onAddPotClicked: {
            stackController.openPotLoaderScreen()
            drawer.close()
        }
        onRemovePotClicked: {
            if (floraManager.removeCurrentPot()) {
                stackController.handlePotRemove()
                drawer.close()
            }
        }
        onTogglePotVisibilityClicked: {
            floraManager.tooglePotVisibility()
            drawer.close()
        }
        onShowPlantsClicked: {
            stackController.openPlantsScreen()
            drawer.close()
        }
        onAddPlantClicked: {
            stackController.openPlantLoaderScreen()
            drawer.close()
        }
        onRemovePlantClicked: {
            if (floraManager.removeCurrentPlant()) {
                stackController.handlePlantRemove()
                drawer.close()
            }
        }
        onQuitClicked: {
            Qt.quit()
        }
    }
}
