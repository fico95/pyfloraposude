
import QtQuick 2.14
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    id: root
    anchors.fill: parent

    signal openPlantsView

    Row {
        id: buttons

        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
            margins: parent.width * 0.01
        }
        height: parent.height * 0.1

        spacing: (width - sync.width - addPot.width - plants.width) / 2

        Button {
            id: sync
            width: parent.width / 8
            height: parent.height * 0.4
            text.text: "Sync"
        }

        Button {
            id: addPot
            anchors.bottom: parent.bottom
            width: parent.width / 2
            height: parent.height * 0.8
            text.text: "Add new pot"
        }

        Button {
            id: plants
            width: parent.width / 8
            height: parent.height * 0.4
            text.text: "Plants"
            mouseArea.onClicked: openPlantsView()
        }
    }

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
            top: buttons.bottom
            left: parent.left
            right: parent.right
            topMargin: parent.height * 0.01
            bottom: parent.bottom
        }

        // mainGrid {
        //     model: plantsHandler
        //     delegate: Item {
        //         width: gridView.mainGrid.cellWidth 
        //         height: gridView.mainGrid.cellHeight
        //         PotButton {
        //             anchors.fill: parent
        //             anchors.margins: 10
        //             potName: name
        //             plantIconSource: "file://" + imagePath
        //         }    
        //     }
        // }
    }
}