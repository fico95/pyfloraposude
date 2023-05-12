import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

PlantEditorBase {
    readonly property string initialPlantName: plantsHandler.currentPlantName()
    readonly property string initialPlantImagePath: plantsHandler.currentPlantImagePath()

    function updateCurrentPlantData() {
        floraManager.updateCurrentPlantData(plantName == "" ? initialPlantName : plantName, soilMoistureValue, phValue, salinityValue, lightLevelValue, temperatureValue)
    }

    function updateShownPlantData() {
        nameTextField.text = plantsHandler.currentPlantName()
        iconSource = plantsHandler.currentPlantImagePath() !== "" ? "file://" + plantsHandler.currentPlantImagePath() : ""
        soilMoistureValue = plantsHandler.currentPlantDesiredSoilMoisture()
        phValue = plantsHandler.currentPlantDesiredPh()
        salinityValue = plantsHandler.currentPlantDesiredSalinity()
        lightLevelValue = plantsHandler.currentPlantDesiredLightLevel()
        temperatureValue = plantsHandler.currentPlantDesiredTemperature()
    }

    function handleFileDialogClose(filePath) {
        filePath = filePath.replace("file://", "")
        let destinationPath = imageManager.copyImage(filePath)
        if (destinationPath !== "") {
            floraManager.updateCurrentPlantImage(destinationPath)
        }
    }

    onIconSourceChanged: {
        if (iconSource == "") {
            return
        }
        floraManager.updateCurrentPlantImage(iconSource.toString().replace("file://", ""))
    }

    onPlantNameChanged: {
        updateCurrentPlantData()
    }

    onUpdateSoilMoistureValue: function(value) {
        soilMoistureValue = value
        updateCurrentPlantData()
    }

    onUpdatePhValue: function(value) {
        phValue = value
        updateCurrentPlantData()
    }

    onUpdateTemperatureValue: function(value) {
        temperatureValue = value
        updateCurrentPlantData()
    }

    onUpdateSalinityValue: function(value) {
        salinityValue = value
        updateCurrentPlantData()
    }

    onUpdateLightLevelValue: function(value) {
        lightLevelValue = value
        updateCurrentPlantData()
    }

    Connections {
        target: plantsHandler
        function onCurrentPlantChanged() {
            updateShownPlantData()
        }
    }

    Component.onCompleted: {
        updateShownPlantData()
    }
    Component.onDestruction: {
        updateCurrentPlantData()
    }
}