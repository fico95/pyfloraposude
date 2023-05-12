import QtQuick 2.15

import "../../Controls"

Item {
    id: root

    anchors.fill: parent

    signal modifyClicked
    signal deleteClicked

    CustomButton {
        anchors {
            horizontalCenter: parent.horizontalCenter
            verticalCenter: parent.verticalCenter
            horizontalCenterOffset: -width / 1.5
        }
        width: root.width / 4
        text: "Modify"
        onClicked: {
            modifyClicked()
        }
    }
    CustomButton {
        anchors {
            horizontalCenter: parent.horizontalCenter
            verticalCenter: parent.verticalCenter
            horizontalCenterOffset: width / 1.5
        }
        width: root.width / 4
        text: "Delete"
        onClicked: {
            deleteClicked()
        }
    }
}
