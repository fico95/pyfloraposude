import QtQuick 2.14
import QtQuick.Window 2.14

import "Screens/Main"

Window {
    visible: true

    width: 1280
    height: 960

    minimumWidth: 640
    minimumHeight: 480

    CustomHeader {
        id: header
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        onDrawerButtonClicked: drawer.toggle()
    }    

    Main {
        anchors {
            top: header.bottom
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }
    }

    CustomDrawer {
        id: drawer
        edge: Qt.RightEdge
        y: header.height
        width: parent.width / 2
        height: parent.height - header.height
    }
}
