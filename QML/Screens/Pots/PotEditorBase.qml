import QtQuick 2.14
import QtQuick.Controls 2.12

import "../../Controls"

FloraLoader {
    readonly property string potName: nameTextField.text
    
    nameTextField.placeholderText: "Pot name"
}