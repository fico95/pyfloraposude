import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

PlantEditorBase {
    function updateCurrentPlantData() {
        floraManager.updateCurrentPlantData(soilMoistureValue, phValue, salinityValue, lightLevelValue, temperatureValue)
    }

    function updateData() {
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
        floraManager.updateCurrentPlantImage(iconSource.toString().replace("file://", ""))
    }

    onPlantNameChanged: {
        floraManager.updateCurrentPlantName(plantName)
    }

    onUpdateSoilMoistureValue: function(value) {
        floraManager.updateCurrentPlantSoilMoisture(value)
    }

    onUpdatePhValue: function(value) {
        floraManager.updateCurrentPlantPh(value)
    }

    onUpdateTemperatureValue: function(value) {
        floraManager.updateCurrentPlantTemperature(value)
    }

    onUpdateSalinityValue: function(value) {
        floraManager.updateCurrentPlantSalinity(value)
    }

    onUpdateLightLevelValue: function(value) {
        floraManager.updateCurrentPlantLightLevel(value)
    }

    Connections {
        target: plantsHandler
        function onCurrentPlantChanged() {
            updateData()
        }
    }

    Component.onCompleted: {
        updateData()
    }
}