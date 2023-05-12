import QtQuick 2.14
import QtQuick.Controls 2.12
import Enums 1.0

import "../../Controls"

Drawer {
    id: drawer

    readonly property int currentScreen: stackController.currentScreen

    signal homeClicked()
    signal profileClicked()
    signal syncClicked()
    signal addPotClicked()
    signal removePotClicked()
    signal togglePotVisibilityClicked()
    signal showPlantsClicked()
    signal addPlantClicked()
    signal removePlantClicked()
    signal quitClicked()

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

    ListModel {
        id: model
        ListElement {
            buttonText: function() {
                return "Home"
            }
            shown: function() { 
                return currentScreen !== Enums.Screen.Welcome 
            }
            action: function() {
                homeClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Profile"
            }
            shown: function() { 
                return currentScreen !== Enums.Screen.Welcome
                    && currentScreen !== Enums.Screen.Login
                    && currentScreen !== Enums.Screen.Registration
                    && currentScreen !== Enums.Screen.ForgottenPassword
                    && currentScreen !== Enums.Screen.UserEditor 
            }
            action: function() {
                profileClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Sync"
            }
            shown: function() { 
                return currentScreen === Enums.Screen.Pots 
            }
            action: function() {
                syncClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Add pot"
            }
            shown: function() { 
                return currentScreen  === Enums.Screen.Pots 
            }
            action: function() {
                addPotClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Remove pot"
            }
            shown: function() { 
                return currentScreen  === Enums.Screen.PotEditor 
            }
            action: function() {
                removePotClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return floraManager.allPotsShown ? "Show empty" : "Show all"
            }
            shown: function() { 
                return currentScreen  === Enums.Screen.Pots 
            }
            action: function() {
                togglePotVisibilityClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Show plants"
            }
            shown: function() { 
                return currentScreen  === Enums.Screen.Pots 
            }
            action: function() {
                showPlantsClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Add plant"
            }
            shown: function() { 
                return currentScreen  === Enums.Screen.Plants 
            }
            action: function() {
                addPlantClicked()
            }
        }
        ListElement {
            buttonText: function() {
                return "Remove plant"
            }
            shown: function() { 
                return currentScreen  === Enums.Screen.PlantEditor 
            }
            action: function() {
                removePlantClicked()
            }
        }
    }

    ListView {
        id: listView
        anchors.fill: parent
        interactive: false
        model: model
        spacing: 5
        delegate: CustomButton {
            height: visible ? listView.height / 10 : -listView.spacing
            onClicked: model.action()
            Component.onCompleted: {
                text = Qt.binding(buttonText)
                visible = Qt.binding(model.shown)
            }
        }
    }
               
    CustomButton {
        anchors.bottom: parent.bottom
        text: "Quit"
        onClicked: {
            quitClicked()
        }
    }
}
