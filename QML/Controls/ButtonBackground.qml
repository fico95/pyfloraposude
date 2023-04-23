import QtQuick 2.15
import QtGraphicalEffects 1.15

Rectangle {
    id: root

    property alias mouseArea: mouseArea

    width: parent.width
    height: parent.height

    radius: height * 0.1

    gradient: Gradient {
        GradientStop { position: 0; color: mouseArea.containsMouse ? "#e5e5e5" : "#f5f5f5" }
        GradientStop { position: 0.5; color: mouseArea.containsMouse ? "#e0e0e0" : "#f0f0f0" }
        GradientStop { position: 1; color: mouseArea.containsMouse ? "#d5d5d5" : "#e5e5e5" }
    }

    border.width: 1
    border.color: mouseArea.containsMouse ? "#aaaaaa" : "#cccccc"

    DropShadow {
        anchors.centerIn: parent
        source: root
        radius: 10
        samples: 8
        color: "#555555"
        opacity: 0.3
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
    }
}
