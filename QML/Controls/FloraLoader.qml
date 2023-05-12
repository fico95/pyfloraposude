import QtQuick 2.14
import QtQuick.Controls 2.12

Item {
    readonly property bool iconSourceExists: iconSource != undefined && iconSource != ""
    property bool iconRemoveAllowed: true

    property alias iconSource: icon.source
    property alias nameTextField: nameTextField

    signal loadTriggered
    signal removeTriggered

    Image {
        id: icon
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
            leftMargin: parent.width * 0.1
            topMargin: parent.height * 0.1
            bottomMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        height: parent.height * 0.8
        source: ""

        Rectangle {
            visible: !iconSourceExists
            anchors.fill: parent
            color: "lightgray"
        }

        CustomText {
            visible: !iconSourceExists
            anchors.centerIn: parent
            text: "No image"
            height: parent.height * 0.1
            width: parent.width * 0.4
            textBold: true
        }

        CustomButton {
            text: iconSourceExists && iconRemoveAllowed ? "X" : "..."
            anchors {
                top: parent.top
                right: parent.right
                margins: 10
            }
            width: parent.width * 0.1
            height: width
            onClicked: {
                if (iconSourceExists && iconRemoveAllowed) {
                    removeTriggered()
                } else {
                    loadTriggered()
                }
            }
        }
    }

    CustomTextField {
        id: nameTextField
        anchors {
            right: parent.right
            top: parent.top
            rightMargin: parent.width * 0.05
            topMargin: parent.height * 0.1
        }
        width: parent.width * 0.4
        height: parent.height * 0.1
        font.bold: true
    }
}