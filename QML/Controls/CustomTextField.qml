import QtQuick 2.15
import QtQuick.Controls 2.15

TextField {
    width: parent.width
    height: parent.height / 10
    font.pixelSize: Math.max(10, height / 2)
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter
}