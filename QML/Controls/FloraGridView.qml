import QtQuick 2.14
import QtQuick.Controls 2.15

Flickable {
    id: flickable

    property alias mainGrid: mainGrid

    clip: true
    flickableDirection: Flickable.VerticalFlick
    contentWidth: parent.width
    contentHeight: mainGrid.contentHeight

    GridView {
        id: mainGrid
        width: parent.width
        height: contentHeight
        interactive: false
        cellHeight: flickable.height / 3
        cellWidth: flickable.width / 3
    }

    ScrollBar.vertical: ScrollBar {
        anchors.right: parent.right
        orientation: Qt.Vertical
        policy: ScrollBar.AlwaysOn
    }
}
