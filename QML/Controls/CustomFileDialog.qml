import QtQuick.Dialogs 1.3

FileDialog {
    id: fileDialog

    title: "Load image"
    folder: shortcuts.home
    nameFilters: [ "Image files (*.jpg, *.jpeg, *.png)" ]
    defaultSuffix: ".png"
}