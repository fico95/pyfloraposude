import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

FloraLoader {
    property alias plantName: nameTextField.text
    property real soilMoistureValue: 0
    property real phValue: 0
    property real salinityValue: 0
    property real lightLevelValue: 0
    property real temperatureValue: 0

    signal saveClicked

    function handleFileDialogClose(filePath) {
        iconSource = filePath
    }

    onRemoveTriggered: {
        iconSource = ""
    }

    nameTextField.placeholderText: "Plant name"

    ListModel {
        id: valueModel

        ListElement {
            buttonText: "Soil moisture [0-100]%"
            from: 0
            to: 100
            sufix: " %"
            updateValue: function(value) { 
                soilMoistureValue = value
            }
        }
        ListElement {
            buttonText: "PH [0-14]"
            from: 0
            to: 14
            sufix: ""
            updateValue: function(value) { 
                phValue = value
            }
        }
        ListElement {
            buttonText: "Salinity [0-100]%"
            from: 0
            to: 100
            sufix: " %"
            updateValue: function(value) { 
                salinityValue = value
            }
        }
        ListElement {
            buttonText: "Light level [0-100]%"
            from: 0
            to: 100
            sufix: " %"
            updateValue: function(value) { 
                lightLevelValue = value
            }
        }
        ListElement {
            buttonText: "Temperature [-10,40]°C"
            from: -10
            to: 40
            sufix: " °C"
            updateValue: function(value) { 
                temperatureValue = value
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
            bottom: saveButton.top
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
                value: (to - from) / 2
                onValueChanged: {
                    model.updateValue(value)
                }
            }
        }
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