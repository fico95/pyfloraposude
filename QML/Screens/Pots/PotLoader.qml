import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

FloraLoader {
    readonly property string potName: nameTextField.text
    
    signal saveClicked

    function updatePlantData() {
        iconSource = plantsHandler.currentPlantImagePath() !== "" ? "file://" + plantsHandler.currentPlantImagePath() : ""
    }

    onRemoveTriggered: {
        floraManager.resetCurrentPlant()
    }

    nameTextField.placeholderText: "Pot name"

    CustomButton {
        id: saveButton
        anchors {
            bottom: parent.bottom
            bottomMargin: parent.height * 0.1
            right: parent.right
            rightMargin: parent.width * 0.05
        }
        width: parent.width * 0.4
        height: parent.height * 0.05
        enabled: potName !== ""
        text: "Save"
        onClicked: {
            saveClicked()
        }
    }

    Connections {
        target: plantsHandler
        function onCurrentPlantChanged() {
            updatePlantData()
        }
    }

    Component.onCompleted: {
        updatePlantData()
    }
}