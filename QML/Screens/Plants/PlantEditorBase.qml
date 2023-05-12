import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

FloraLoader {
    readonly property string plantName: nameTextField.text
    property real soilMoistureValue: 50
    property real phValue: 7
    property real salinityValue: 50
    property real lightLevelValue: 50
    property real temperatureValue: 15

    signal updateSoilMoistureValue(real value)
    signal updatePhValue(real value)
    signal updateSalinityValue(real value)
    signal updateLightLevelValue(real value)
    signal updateTemperatureValue(real value)

    function handleFileDialogClose(filePath) {
        iconSource = filePath
    }

    onRemoveTriggered: {
        iconSource = ""
    }

    iconRemoveAllowed: false
    nameTextField.placeholderText: "Plant name"

    ListModel {
        id: valueModel

        ListElement {
            buttonText: "Soil moisture [0-100]%"
            from: 0
            to: 100
            sufix: " %"
            currentValue: function() { return soilMoistureValue }
            updateValue: function(value) { 
                updateSoilMoistureValue(value)
            }
        }
        ListElement {
            buttonText: "PH [0-14]"
            from: 0
            to: 14
            sufix: ""
            currentValue: function() { return phValue }
            updateValue: function(value) { 
                updatePhValue(value)
            }
        }
        ListElement {
            buttonText: "Salinity [0-100]%"
            from: 0
            to: 100
            sufix: " %"
            currentValue: function() { return salinityValue }
            updateValue: function(value) { 
                updateSalinityValue(value)
            }
        }
        ListElement {
            buttonText: "Light level [0-100]%"
            from: 0
            to: 100
            sufix: " %"
            currentValue: function() { return lightLevelValue }
            updateValue: function(value) { 
                updateLightLevelValue(value)
            }
        }
        ListElement {
            buttonText: "Temperature [-10,40]°C"
            from: -10
            to: 40
            sufix: " °C"
            currentValue: function() { return temperatureValue }
            updateValue: function(value) { 
                updateTemperatureValue(value)
            }
        }
    }

    ListView {
        id: listView
        anchors {
            right: parent.right
            top: nameTextField.bottom
            rightMargin: parent.width * 0.05
            topMargin: parent.height * 0.1        
            bottom: parent.bottom
            bottomMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        interactive: false
        spacing: parent.height * 0.05
        model: valueModel
        delegate: Item {
            height: listView.height * 0.05
            width: parent.width
            CustomText {
                anchors.left: parent.left
                height: parent.height
                text: model.buttonText
                horizontalAlignment: Text.AlignLeft
            }
            DoubleSpinBox {
                width: parent.width / 3
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                from: model.from
                to: model.to
                decimals: 1
                wrap: false
                onValueChanged: {
                    model.updateValue(value)
                    value = Qt.binding(function() { return model.currentValue() })
                }
                Component.onCompleted: {
                    value = Qt.binding(function() { return model.currentValue() })
                }
            }
        }
    }
}