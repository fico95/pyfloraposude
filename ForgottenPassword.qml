import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: forgottenPasswordScreen

    width: parent.width
    height: parent.height

    signal acceptClicked
    signal cancelClicked

    Column {
        spacing: 10
        anchors.centerIn: parent

        Text {
            text: "There is no option to restore password. All accounts will be deleted. Are you sure you want to continue?"
            font.pixelSize: 20
            wrapMode: Text.Wrap
            horizontalAlignment: Text.AlignHCenter
            width: parent.width - 20
        }

        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter

            Button {
                id: acceptButton
                text: "Accept"
                width: 100
                onClicked: {
                    acceptClicked()
                }
            }

            Button {
                id: cancelButton
                text: "Cancel"
                width: 100
                onClicked: {
                    cancelClicked()
                }
            }
        }
    }
}
