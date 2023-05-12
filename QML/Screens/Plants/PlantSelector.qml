import QtQuick 2.14
import QtQuick.Controls 2.15

Item {
    id: root
    anchors.fill: parent

    signal plantSelected(int plantId)

    PlantsViewBase {
        onOpenPlantEditor: {
            root.plantSelected(plantId)
        }
    }
}