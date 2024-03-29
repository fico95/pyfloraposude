
import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    id: root

    anchors.fill: parent

    signal openPotEdit(int potId)

    FloraGridView {
        id: gridView
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
            topMargin: parent.height * 0.01
            bottom: parent.bottom
        }

        mainGrid {
            model: potModel
            delegate: PotButton {
                name: model.name
                potId: model.potId
                plantImagePath: model.plantImagePath
                temperatureOk: model.temperatureOk
                soilMoistureOk: model.soilMoistureOk
                phOk: model.phOk
                lightLevelOk: model.lightLevelOk
                salinityOk: model.salinityOk
                broken: model.broken

                width: gridView.mainGrid.cellWidth 
                height: gridView.mainGrid.cellHeight

                onButtonClicked: root.openPotEdit(potId)
            }
        }
    }

    Component.onCompleted: {
        floraManager.resetCurrentPot()
        floraManager.resetCurrentPlant()
    }
}