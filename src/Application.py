import os
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle

from StackController.StackController import StackController
from Users.UserHandler import UserHandler
from Flora.FloraManager import FloraManager
from Helpers.ImageManager import ImageManager

class Application(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)

        self.setOrganizationName("None")
        self.setOrganizationDomain("None")

        self.initialized = False

        if (len(sys.argv) < 2 or len(sys.argv[1]) == 0):
            print("No root path provided.")
            return
        
        rootPath = sys.argv[1]
        if (not os.path.exists(rootPath) or not os.path.isdir(rootPath)):
            print("Invalid root path provided.")
            return

        imagesPath = "images"
        qmlMainPath = "QML/main.qml"
        dbPath = "database.db"
        if (not os.path.isfile(rootPath + "/" + qmlMainPath)):
            print("Invalid root path provided, main QML file not found.")
            return     

        self.engine = QQmlApplicationEngine()
        QQuickStyle.setStyle("Imagine")

        self.stackController = StackController(self)
        self.userHandler = UserHandler(rootPath + "/" + dbPath, self)
        self.imageManager = ImageManager(rootPath + "/" + imagesPath, self)
        self.floraManager = FloraManager(rootPath + "/" + dbPath, rootPath + "/" + imagesPath, self)

        self.engine.rootContext().setContextProperty("stackController", self.stackController)
        self.engine.rootContext().setContextProperty("userHandler", self.userHandler)
        self.engine.rootContext().setContextProperty("imageManager", self.imageManager)
        self.engine.rootContext().setContextProperty("floraManager", self.floraManager)
        self.engine.rootContext().setContextProperty("plantModel", self.floraManager.plantModel)
        self.engine.rootContext().setContextProperty("plantsHandler", self.floraManager.plantsHandler)
        self.engine.rootContext().setContextProperty("potModel", self.floraManager.potModel)
        self.engine.rootContext().setContextProperty("potsHandler", self.floraManager.potsHandler)

        self.engine.load(rootPath + "/" + qmlMainPath)

        if self.engine.rootObjects():
            self.initialized = True

    def isInitialized(self):
        return self.initialized