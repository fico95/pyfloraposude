import QtQuick 2.14

Text {
    id: root

    property bool textBold: false
    property real sizeCale: 1.0

    anchors.horizontalCenter: parent.horizontalCenter
    width: parent.width
    height: parent.height
    font {
        bold: root.textBold
        pointSize: Math.max(8, parent.height * root.sizeCale)
    }
    fontSizeMode: Text.Fit
    wrapMode: Text.WordWrap
    maximumLineCount: 4
    elide: Text.ElideRight
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter
}