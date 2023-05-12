import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

PlantEditorBase {
    signal saveClicked

    onUpdateSoilMoistureValue: function(value) {
        soilMoistureValue = value
    }

    onUpdatePhValue: function(value) {
        phValue = value
    }

    onUpdateTemperatureValue: function(value) {
        temperatureValue = value
    }

    onUpdateSalinityValue: function(value) {
        salinityValue = value
    }

    onUpdateLightLevelValue: function(value) {
        lightLevelValue = value
    }

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
        enabled: plantName !== "" && iconSourceExists
        text: "Save"
        onClicked: {
            saveClicked()
        }
    }
}