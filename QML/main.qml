import QtQuick 2.14
import QtQuick.Window 2.14

import "Screens/Main"

Window {
    visible: true

    width: 1280
    height: 960

    minimumWidth: 640
    minimumHeight: 480

    Header {
        id: header
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
    }    

    Main {
        anchors {
            top: header.bottom
            bottom: footer.top
            left: parent.left
            right: parent.right
        }
    }

    Footer {
        id: footer
        anchors {
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }
    }
}
