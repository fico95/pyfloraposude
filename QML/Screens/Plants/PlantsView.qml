
import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    id: root
    anchors.fill: parent

    signal openPlantEditor(int plantId)

    Rectangle {
        width: parent.width
        anchors {
            top: gridView.top
            bottom: gridView.bottom
        }
        color: "darkgray"
    }

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
            model: plantsHandler
            delegate: Item {
                width: gridView.mainGrid.cellWidth 
                height: gridView.mainGrid.cellHeight
                PotButton {
                    anchors.fill: parent
                    anchors.margins: 10
                    potName: name
                    plantIconSource: "file://" + imagePath
                    mouseArea.onClicked: {
                        openPlantEditor(id)
                    }
                }    
            }
        }
    }
}