
import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    id: root

    anchors.fill: parent

    signal openPotView(int potId)

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
            delegate: Item {
                width: gridView.mainGrid.cellWidth 
                height: gridView.mainGrid.cellHeight
                PotButton {
                    anchors.fill: parent
                    anchors.margins: 10
                    potName: name
                    plantIconSource: plantImagePath !== undefined ? "file://" + plantImagePath : ""
                    mouseArea.onClicked: {
                        root.openPotView(potId)
                    }
                    Rectangle {
                        anchors.fill: parent
                        anchors.margins: 5
                        color: "red"
                        opacity: 0.25
                        radius: height * 0.1
                        visible: broken
                    }
                }    

            }
        }
    }
}