import os
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle

from StackController.StackController import StackController
from Users.UserHandler import UserHandler
from Flora.Plants.PlantsHandler import PlantsHandler

class Application(QGuiApplication):
    def __init__(self, *args, **kwargs):
        QGuiApplication.__init__(self, *args, **kwargs)

        self.initialized = False

        if (len(sys.argv) < 2 or len(sys.argv[1]) == 0):
            print("No root path provided.")
            return
        
        rootPath = sys.argv[1]
        if (not os.path.exists(rootPath) or not os.path.isdir(rootPath)):
            print("Invalid root path provided.")
            return

        qmlMainPath = "QML/main.qml"
        dbPath = "database.db"
        if (not os.path.isfile(rootPath + "/" + qmlMainPath)):
            print("Invalid root path provided, main QML file not found.")
            return     

        self.engine = QQmlApplicationEngine()
        QQuickStyle.setStyle("Imagine")

        self.stackController = StackController()
        self.userHandler = UserHandler(rootPath + "/" + dbPath)
        self.plantsHandler = PlantsHandler(rootPath + "/" + dbPath)
        
        self.engine.rootContext().setContextProperty("stackController", self.stackController)
        self.engine.rootContext().setContextProperty("userHandler", self.userHandler)
        self.engine.rootContext().setContextProperty("plantsHandler", self.plantsHandler)

        self.engine.load(rootPath + "/" + qmlMainPath)

        if self.engine.rootObjects():
            self.initialized = True

    def isInitialized(self):
        return self.initialized