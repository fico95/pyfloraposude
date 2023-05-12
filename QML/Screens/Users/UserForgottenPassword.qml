import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../Controls"

Item {
    signal acceptClicked

    anchors.fill: parent

    Column {
        id: mainColumn

        width: parent.width / 2
        anchors {
            top: parent.top
            topMargin: parent.height / 3
            bottom: parent.bottom
        }
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: parent.height / 20

        CustomText {
            height: parent.height / 4
            text: "There is no option to restore password. All accounts will be deleted. Are you sure you want to continue?"
        }

        CustomButton {
            text: "Accept"
            onClicked: acceptClicked()
        }
    }
}
