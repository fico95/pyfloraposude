import QtQuick 2.14

PlantsViewBase {
    Component.onCompleted: {
        floraManager.resetCurrentPot()
        floraManager.resetCurrentPlant()
    }
}