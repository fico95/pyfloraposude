import QtQuick 2.14

Text {
    id: root

    property bool textBold: false
    property real sizeCale: 1.0

    width: parent.width
    height: parent.height
    font {
        bold: root.textBold
        pointSize: Math.max(10, parent.height * root.sizeCale)
    }
    fontSizeMode: Text.Fit
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter
}