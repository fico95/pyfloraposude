import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    signal acceptClicked
    signal cancelClicked

    anchors.fill: parent

    Column {
        id: mainColumn

        width: parent.width / 2
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: 10

        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            text: "There is no option to restore password. All accounts will be deleted. Are you sure you want to continue?"
            font.pixelSize: 20
            wrapMode: Text.Wrap
            horizontalAlignment: Text.AlignHCenter
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            width: mainColumn.width / 2
            text: "Accept"
            onClicked: acceptClicked()
        }
    }
}
