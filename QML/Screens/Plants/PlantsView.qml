import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    id: root
    anchors.fill: parent

    signal openPlantEditor(int plantId)

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
            model: plantModel
            delegate: Item {
                width: gridView.mainGrid.cellWidth 
                height: gridView.mainGrid.cellHeight
                GridButton {
                    anchors.fill: parent
                    anchors.margins: 10
                    nameText: name
                    iconSource: imagePath !== "" ? "file://" + imagePath : ""
                    Component.onCompleted: console.log("imagePath: " + imagePath)
                    mouseArea.onClicked: {
                        openPlantEditor(id)
                    }
                }    
            }
        }
    }
}